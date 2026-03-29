from django.shortcuts import render
from .models import Flashcard

def home(request):
    # Fetch all cards from the database
    cards = Flashcard.objects.all()
    # Send them to the template
    return render(request, 'education/home.html', {'cards': cards})