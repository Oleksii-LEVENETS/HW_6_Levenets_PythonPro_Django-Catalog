from django import forms


class Triangle(forms.Form):
    leg_a = forms.IntegerField(label="Leg (cathetus) 'a'", min_value=0)
    leg_b = forms.IntegerField(label="Leg (cathetus) 'b'", min_value=0)
