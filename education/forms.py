from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['topic', 'question', 'answer']

        labels = {
            'topic': 'Algorithm Set (CLL, EG-1, CSP, TBD!!!)',
            'question': 'Case or Scramble',
            'answer': 'The Algoritm'
        }
