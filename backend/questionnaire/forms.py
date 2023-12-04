from django.forms import ModelForm
from django_select2 import forms as s2forms

from .models import *
from django_json_widget.widgets import JSONEditorWidget


__all__ = [
    "QuestionForm",
]


_ms2w_attrs = {
    "style": "width:40rem;",
    "data-minimum-input-length": 3,
    "data-ajax--delay": 1000,
}


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        widgets = {
            "questionnaire": s2forms.ModelSelect2Widget(
                search_fields=["name__icontains"],
                attrs=_ms2w_attrs,
            ),
            "structure": JSONEditorWidget(
                mode="tree",
                width="640px",
                options={"search": False},
            ),
        }
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and not self.instance.structure:
            self.initial["structure"] = self.instance.get_default_structure()
