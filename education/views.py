from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard
from .forms import FlashcardForm

def home(request):
    # Fetch all cards from the database
    cards = Flashcard.objects.all()
    # Send them to the template
    return render(request, 'education/home.html', {'cards': cards})

def card_detail(request, pk):
    # gets one card by its id or gives error 404
    card = get_object_or_404(Flashcard, pk=pk)
    return render(request, 'education/card_detail.html', {'card': card})

def add_card(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()     # saves to database
            return redirect('home')
    else:
        form = FlashcardForm() # just shows empty form

    return render(request, 'education/add_card.html', {'form': form})

def edit_card(request, pk):
    card = get_object_or_404(Flashcard, pk=pk)

    # if user clicks Save (POST)
    if request.method == 'POST':
        form = FlashcardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            # sends back to details page to see changes
            return redirect('card_detail', pk=card.pk)

    # if user just opens the page (GET)
    else:
        # prefill the form curent data of card
        form = FlashcardForm(instance=card)

    return render(request, 'education/edit_card.html', {'form': form, 'card': card})
