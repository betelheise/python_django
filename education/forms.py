from django import forms
from .models import Flashcard, AlgSet

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['alg_set', 'name', 'question', 'answer', 'image']

        widgets = {
            'image': forms.FileInput(),
        }

        labels = {
            'alg_set': 'Algorithm Set',
            'name': 'Case Name',
            'question': 'Case or Scramble',
            'answer': 'The Algorithm',
            'image': 'Case Image',
        }

class AlgSetForm(forms.ModelForm):
    class Meta:
        model = AlgSet
        fields = ['name', 'description', 'image']

        widgets = {
            # to remove Django's annoying check-mark in group image add section
            'image': forms.FileInput(),
        }

        labels = {
            'name': 'Group Name (e.g., CLL, OLL)',
            'description': 'Short description',
            'image': 'Group Icon (Optional)'
        }
