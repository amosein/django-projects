from django import forms

class CreateNoteForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
