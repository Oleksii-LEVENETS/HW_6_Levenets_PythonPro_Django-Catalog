import re

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Person


def validate_non_zero(value):
    if value <= 0:
        raise ValidationError(
            _('value is not > 0'),
            params={'value': value},
        )


class Triangle(forms.Form):

    leg_a = forms.IntegerField(
        label="Leg (cathetus) 'a'",
        label_suffix=' =',
        help_text='A positive INTEGER > 0, please.',
        validators=[validate_non_zero],
    )

    leg_b = forms.IntegerField(
        label="Leg (cathetus) 'b'",
        label_suffix=' =',
        help_text='A positive INTEGER > 0, please.',
        validators=[validate_non_zero]
    )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']

    def clean_first_name(self):
        value = self.cleaned_data["first_name"]
        rez = re.fullmatch(r"[a-zA-Z]+-*[a-zA-Z]*", value)
        if rez is None:
            raise ValidationError("Only letters or one '-' are required!")
        return value

    def clean_last_name(self):
        value = self.cleaned_data["last_name"]
        rez = re.fullmatch(r"[a-zA-Z]+-*[a-zA-Z]*", value)
        if rez is None:
            raise ValidationError("Only letters or one '-' are required!")
        return value
