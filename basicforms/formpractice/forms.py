from django import forms

class TestForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    description = forms.CharField(widget = forms.Textarea)