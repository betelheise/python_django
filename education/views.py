from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard, AlgSet
from .forms import FlashcardForm, AlgSetForm


def home(request):
    # Only fetch the groups now, I don't want all cards on the home page anymore
    alg_sets = AlgSet.objects.all()
    return render(request, 'education/home.html', {'alg_sets': alg_sets})


def set_detail(request, pk):
    # Get the specific group (e.g., EG-1)
    alg_set = get_object_or_404(AlgSet, pk=pk)

    # Read what the user clicked in the URL (default to 'list' and 'newest')
    layout = request.GET.get('layout', 'list')
    sort_by = request.GET.get('sort', 'newest')

    # Get the cards for this set
    cards = Flashcard.objects.filter(alg_set=alg_set)

    if sort_by == 'name':
        cards = cards.order_by('name') # Sorts alphabetically A-Z
    else:
        cards = cards.order_by('-created_at') # Sorts by newest first

    return render(request, 'education/set_detail.html', {
        'alg_set': alg_set,
        'cards': cards,
        'layout': layout,
        'current_sort': sort_by
    })


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


def add_set(request):
    if request.method == 'POST':
        form = AlgSetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlgSetForm()

    return render(request, 'education/add_set.html', {'form': form})


def edit_set(request, pk):
    alg_set = get_object_or_404(AlgSet, pk=pk)

    if request.method == 'POST':
        form = AlgSetForm(request.POST, request.FILES, instance=alg_set)
        if form.is_valid():
            form.save()
            return redirect('set_detail', pk=alg_set.pk)
    else:
        form = AlgSetForm(instance=alg_set)

    return render(request, 'education/edit_set.html', {'form': form, 'alg_set': alg_set})


def delete_set(request, pk):
    alg_set = get_object_or_404(AlgSet, pk=pk)
    if request.method == 'POST':
        alg_set.delete()
        return redirect('home')

    return redirect('set_detail', pk=alg_set.pk)
