from __future__ import annotations

import datetime as dt
from hashlib import sha3_256
from typing import List, Tuple, Union, TypedDict, Optional

from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_init
from django.conf import settings

from server.tools import RandomString, Choices


__all__ = [
    "User",
    "Questionnaire",
    "QuestionTypes",
    "Question",
    "Answer",
    "AnswerToQuestion",
]


# ======================================================================


class User(models.Model):
    def generate_token_full(self):
        raw = str(self.token) + str(self.date_token) + settings.SALT
        return sha3_256(raw.encode()).hexdigest()

    name = models.CharField(
        verbose_name="User name",
        default="User",
        max_length=50,
        unique=True,
    )
    token = RandomString(
        verbose_name="Login token",
        unique=True,
        max_length=10,
        auto_created=True,
    )
    date_created = models.DateTimeField(
        verbose_name="Creation date",
        auto_now_add=True,
    )
    token_full = models.CharField(
        verbose_name="Cookie token",
        unique=True,
        default=generate_token_full,
        blank=True,
        auto_created=True,
        max_length=64,
    )
    date_token = models.DateTimeField(
        verbose_name="Date of token update",
        blank=True,
        auto_created=True,
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        indexes = [
            models.Index(fields=["token"], name="user_idx_token"),
            models.Index(fields=["token_full"], name="user_idx_token_full"),
        ]

    def __str__(self):
        return str(self.token)

    def __str_admin__(self) -> str:
        return f"{self.token} / {self.name} / {self.date_created:%d-%m-%YY}"

    def reissue_token_full(self):
        self.date_token = dt.datetime.now()
        self.token_full = self.generate_token_full()

    def save(self, *args, **kwargs):
        self.reissue_token_full()
        super().save(*args, **kwargs)


# ======================================================================


class Questionnaire(models.Model):
    token = RandomString(
        verbose_name="Questionnaire link",
        max_length=8,
        unique=True,
    )
    title = models.TextField(
        verbose_name="Questionnaire title",
    )
    description = models.TextField(
        verbose_name="Questionnaire description",
        null=True,
        blank=True,
    )
    date_start = models.DateTimeField(
        verbose_name="Start date",
        help_text="On this date the questionnaire becomes active",
    )
    date_end = models.DateTimeField(
        verbose_name="Date end",
        help_text="On this date the questionnaire is no longer active",
        null=True,
        blank=True,
    )
    is_hidden = models.BooleanField(
        verbose_name="Is hidden from the main page",
        default=False,
    )
    created_by = models.ForeignKey(
        verbose_name="Questionnaire author",
        to="service.Staff",
        on_delete=models.PROTECT,
    )
    is_protected = models.BooleanField(
        verbose_name="Can only be changed by the author",
        help_text="Can only be changed by the author",
        default=False,
    )

    class Meta:
        verbose_name = "Questionnaire"
        verbose_name_plural = "Questionnaires"
        indexes = [
            models.Index(fields=["token"], name="questionnaire_idx_token"),
            models.Index(fields=["date_start"], name="questionnaire_idx_date_start"),
            models.Index(fields=["is_hidden"], name="questionnaire_idx_is_hidden"),
        ]

    def __str__(self):
        return str(self.token)

    def __str_admin__(self) -> str:
        dates = f"{self.date_start:%d-%m-%YY}" + (
            f" / {self.date_end:%d-%m-%YY}"
            if self.date_end else
            ""
        )

        description = ""
        if self.description:
            description = f" / {self.description}"
            if len(description) > 53:
                description = description[:50] + "..."

        return f"{self.token} / {self.short_title} / {dates}{description}"

    @property
    def short_title(self) -> str:
        title = str(self.title)
        if len(title) > 33:
            title = title[:30] + "..."
        return title


# ======================================================================


class QuestionTypes(Choices):
    text = "Answer as text"
    string = "Answer as small text"
    single = "Answer as choice"
    multi = "Answer as multichoice"

    _DEFAULT = text


_LENGTH_TYPE = Optional[int]
_VARIANT_TYPE = TypedDict("_VARIANT_TYPE", {"order": int, "text": str})
QUESTION_STRUCTURE = Union[
    TypedDict("_TEXT_STRUCTURE", {"maxLength": _LENGTH_TYPE, "minLength": _LENGTH_TYPE}),
    TypedDict("_STRING_STRUCTURE", {"maxLength": _LENGTH_TYPE}),
    TypedDict("_SINGLE_STRUCTURE", {"variants": List[_VARIANT_TYPE]}),
    TypedDict("_MULTI_STRUCTURE", {"variants": List[_VARIANT_TYPE]}),
]


def _get_question_default_structure(instance: Question = None) -> dict:
    type_ = Question.type.field.get_default()
    if instance:
        type_ = instance.type
    return Question.get_structure_by_type(type_)


class Question(models.Model):
    Types = QuestionTypes

    questionnaire = models.ForeignKey(
        verbose_name="Questionnaire",
        to="questionnaire.Questionnaire",
        on_delete=models.CASCADE,
        related_name="questions",
    )
    type = models.CharField(
        verbose_name="Question type",
        choices=Types.as_tuple(),
        max_length=6,
        default=Types.DEFAULT(),
    )
    title = models.TextField(
        verbose_name="Question title",
    )
    order = models.IntegerField(
        verbose_name="Order in the question",
        validators=[MinValueValidator(0)],
        default=0,
    )
    description = models.TextField(
        verbose_name="Detailed description of the question",
        null=True,
        blank=True,
    )
    is_required = models.BooleanField(
        verbose_name="Answer is required",
        default=False,
    )
    structure = models.JSONField(
        verbose_name="Response parameters",
        default=_get_question_default_structure,
    )

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return str(self.title) or "<unknown>"

    def __str_admin__(self) -> str:
        questionnaire = self.questionnaire.short_title
        params_list = [
            self.short_title,
            ("required" if self.is_required else ""),
        ]
        params = "; ".join(str(p) for p in filter(bool, params_list))
        return f"{questionnaire} / {self.type} - {params}"

    @staticmethod
    def get_default_structure(instance: Question = None) -> dict:
        return _get_question_default_structure(instance)

    @property
    def short_title(self) -> str:
        title = str(self.title)
        if len(title) > 33:
            title = title[:30] + "..."
        return title

    @classmethod
    def get_structure_by_type(cls, type_) -> QUESTION_STRUCTURE:
        if type_ == cls.Types.text.name:
            return {"maxLength": None, "minLength": None}
        if type_ == cls.Types.string.name:
            return {"maxLength": None}
        if type_ == cls.Types.single.name:
            return {"variants": []}
        if type_ == cls.Types.multi.name:
            return {"variants": []}
        return dict()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.structure:
            self.structure = self.get_default_structure(self)


# ======================================================================


class Answer(models.Model):
    user = models.ForeignKey(
        verbose_name="User who answered",
        to="questionnaire.User",
        on_delete=models.CASCADE,
    )
    questionnaire = models.ForeignKey(
        verbose_name="Questionare",
        to="questionnaire.Questionnaire",
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(
        verbose_name="Date of answers",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        unique_together = [
            ["user", "questionnaire"],
        ]


# ======================================================================


class AnswerToQuestion(models.Model):
    answer = models.ForeignKey(
        verbose_name="Answer",
        to="questionnaire.Answer",
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        verbose_name="Question from questionnaire",
        to="questionnaire.Question",
        on_delete=models.CASCADE,
    )
    value = models.JSONField(
        verbose_name="Answer data",
        default=dict,
    )

    class Meta:
        verbose_name = "Answer to question"
        verbose_name_plural = "Answers to question"
        unique_together = [
            ["answer", "question"],
        ]
