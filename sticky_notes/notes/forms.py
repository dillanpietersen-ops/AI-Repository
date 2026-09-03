from django import forms
from .models import Note


class NoteForm(forms.ModelForm):  # For creating and updating Sticky Notes
    class Meta:  # Defines the model to use (Note) and fields to include
        model = Note
        fields = ["title", "content", "author"]
