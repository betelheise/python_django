from django.shortcuts import render, get_object_or_404
from .models import Flashcard

def home(request):
    # Fetch all cards from the database
    cards = Flashcard.objects.all()
    # Send them to the template
    return render(request, 'education/home.html', {'cards': cards})

def card_detail(request, pk):
    # gets one card by it's id or gives error 404
    card = get_object_or_404(Flashcard, pk=pk)
    return render(request, 'education/card_detail.html', {'card': card})
