from django import forms
from .models import Todo

class CreateNoteForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()

class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "body"]

class MiddleUpdateForm(forms.Form):
    id_ = forms.CharField()

class MiddleDeleteForm(forms.Form):
    id_ = forms.CharField()