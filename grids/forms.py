from django import forms

class CreateGameForm(forms.Form):
    rows = forms.IntegerField(label="rows", max_value=32, required=True, initial=3)
    cols = forms.IntegerField(label="cols", max_value=32, required=True, initial=4)

