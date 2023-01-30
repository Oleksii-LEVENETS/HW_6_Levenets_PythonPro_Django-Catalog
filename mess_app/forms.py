from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
