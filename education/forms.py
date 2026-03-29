from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['alg_set', 'question', 'answer']

        labels = {
            'alg_set': 'Algorithm Set (e.g. CLL, EG-1, CSP)',
            'question': 'Case or Scramble',
            'answer': 'The Algoritm'
        }
