from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard, AlgSet
from .forms import FlashcardForm

def home(request):
    # Fetch all algorithm sets to display on the homepage
    alg_sets = AlgSet.objects.all()
    # Fetch all cards from the database
    cards = Flashcard.objects.all()
    # Send them to the template
    return render(request, 'education/home.html', {'alg_sets': alg_sets, 'cards': cards})

def set_detail(request, pk):
    # Get the specific group (e.g., EG-1)
    alg_set = get_object_or_404(AlgSet, pk=pk)
    # Get ONLY the cards that belong to this group
    cards = Flashcard.objects.filter(alg_set=alg_set)
    return render(request, 'education/set_detail.html', {'alg_set': alg_set, 'cards': cards})

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
