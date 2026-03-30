from django import forms
from .models import Flashcard, AlgSet

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['alg_set', 'question', 'answer']

        labels = {
            'alg_set': 'Algorithm Set (e.g. CLL, EG-1, CSP)',
            'question': 'Case or Scramble',
            'answer': 'The Algoritm'
        }

class AlgSetForm(forms.ModelForm):
    class Meta:
        model = AlgSet
        fields = ['name', 'description', 'image']
        labels = {
            'name': 'Group Name (e.g., CLL, OLL)',
            'description': 'Short description',
            'image': 'Group Icon (Optional)'
        }
