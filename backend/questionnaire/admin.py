from django.contrib import admin

from .models import *
from .forms import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = [
        "token",
        "token_full",
    ]
    fields = [
        "name",
        ("date_created", "token",),
        ("date_token", "token_full"),
    ]


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    search_fields = [
        "title",
        "token",
    ]
    list_filter = [
        "is_hidden",
        "is_protected",
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    search_fields = [
        "title",
    ]
    list_filter = [
        "type",
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields = [
        "user__token",
    ]


@admin.register(AnswerToQuestion)
class AnswerToQuestionAdmin(admin.ModelAdmin):
    search_fields = [
        "answer__user__token",
    ]
