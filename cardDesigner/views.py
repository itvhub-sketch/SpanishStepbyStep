"""
Generates text-to-speech audio for a card in a deck.

This view function is responsible for generating audio data for the question and answer of a card in a given deck. It uses the pyttsx3 library to convert the text to audio, and then encodes the audio data in base64 format to be returned as a JSON response.

The function first retrieves the deck and its associated cards. If a specific card ID is provided, it retrieves that card, otherwise it randomly selects a card from the deck. It then generates the audio data for the question and answer of the selected card, and returns the audio data in a JSON response.

Args:
    request (django.http.request.HttpRequest): The HTTP request object.
    deck_id (int): The ID of the deck.
    card_id (int, optional): The ID of the card. If not provided, a random card from the deck will be selected.

Returns:
    django.http.JsonResponse: A JSON response containing the base64-encoded audio data for the question and answer of the selected card.
"""
import os
import base64
import pyttsx3
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Card, Deck, StudySet, StudentDeck
from .forms import CardFormSet, DeckForm
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import random
from io import BytesIO

import logging

logger = logging.getLogger(__name__)

def text_to_speech(request, deck_id, card_id=None):
    logger.info(f"Received request for deck_id={deck_id} and card_id={card_id}")

    deck = get_object_or_404(Deck, id=deck_id)
    logger.info(f"Retrieved deck: {deck}")

    cards = deck.card_set.all()
    logger.info(f"Retrieved {len(cards)} cards for the deck")

    if not cards:
        logger.warning("No cards found for this deck.")
        return JsonResponse({'error': 'No cards found for this deck.'}, status=404)

    if card_id:
        card = get_object_or_404(Card, id=card_id)
        logger.info(f"Retrieved card with id={card_id}: {card}")
    else:
        card = random.choice(cards)
        logger.info(f"Randomly selected card: {card}")

    engine = pyttsx3.init()
    logger.info("Initialized pyttsx3 engine")

    # Generate audio data for the question
    question_audio_data = BytesIO()
    engine.save_to_wav(card.question, question_audio_data)
    question_audio_base64 = base64.b64encode(question_audio_data.getvalue()).decode('utf-8')
    logger.info("Generated audio data for the question")

    # Generate audio data for the answer
    answer_audio_data = BytesIO()
    engine.save_to_wav(card.answer, answer_audio_data)
    answer_audio_base64 = base64.b64encode(answer_audio_data.getvalue()).decode('utf-8')
    logger.info("Generated audio data for the answer")

    engine.stop()
    logger.info("Stopped pyttsx3 engine")

    audio_data = {
        'question_audio': question_audio_base64,
        'answer_audio': answer_audio_base64,
    }

    logger.info("Returning audio data as JSON response")
    return JsonResponse(audio_data)


def home(request):
    if request.user.is_authenticated:
        return redirect('all_decks')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def show_all_cards(request):
    c_list = Card.objects.all()
    context = {'list_of_cards': c_list}
    return render(request, 'show_all_cards.html', context)


def delete_card(request, card_id):
    card_to_delete = Card.objects.get(id=card_id)
    card_to_delete.delete()
    return redirect('show_all_cards')


def show_all_decks(request):
    d_list = Deck.objects.all()
    context = {'list_of_decks': d_list}
    return render(request, 'all_decks.html', context)


def delete_deck(request, deck_id):
    deck_to_delete = Deck.objects.get(id=deck_id)
    deck_to_delete.delete()
    return redirect('all_decks')


class DeckCreate(CreateView):
    form_class = DeckForm
    model = Deck

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creator = self.request.user
        f.save()
        return super().form_valid(form)


def generate_audio(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()


def create_cards(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)

    if request.method == 'POST':
        formset = CardFormSet(request.POST, instance=deck)
        if formset.is_valid():
            cards = formset.save(commit=False)
            for card in cards:
                card.deck = deck

                # Generate audio files for the question and answer
                question_audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', f'question_{card.id}.mp3')
                answer_audio_path = os.path.join(settings.MEDIA_ROOT, 'audio', f'answer_{card.id}.mp3')

                generate_audio(card.question, question_audio_path)
                generate_audio(card.answer, answer_audio_path)

                card.question_audio = os.path.join('audio', f'question_{card.id}.mp3')
                card.answer_audio = os.path.join('audio', f'answer_{card.id}.mp3')

                card.save()

            return redirect('create_cards', deck_id=deck_id)

    else:
        formset = CardFormSet(instance=deck)

    return render(request, 'create_cards.html', {'formset': formset, 'deck': deck})


def show_deck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    c_list = Card.objects.filter(deck=deck)
    context = {'list_of_cards': c_list, 'deck': deck}
    return render(request, 'show_deck.html', context)


def practice_deck(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    c_list = Card.objects.filter(deck=deck)
    context = {
        'list_of_cards': c_list,
        'deck': deck,
        'audio_enabled': request.GET.get('audio_enabled', False)
    }
    return render(request, 'practice_deck.html', context)


def save_for_study(request, deck_id):
    user = request.user
    deck = get_object_or_404(Deck, pk=deck_id)
    studyset, created = StudySet.objects.get_or_create(student=user)
    if not StudentDeck.objects.filter(deck=deck, student=user).exists():
        s = StudentDeck()
        s.studyset = studyset
        s.student = user
        s.deck = deck
        s.save()
    return redirect('show_my_studyset')


def show_my_studyset(request):
    studyset = StudySet.objects.get(student_id=request.user.id)
    deck_list = StudentDeck.objects.filter(studyset_id=studyset.id)
    context = {'studyset': studyset, 'deck_list': deck_list}
    return render(request, 'my_studyset.html', context)


def remove_from_studyset(request, studentdeck_id):
    deck_to_remove = get_object_or_404(StudentDeck, id=studentdeck_id)
    deck_to_remove.delete()
    return redirect('show_my_studyset')


def leitner(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    c_list = Card.objects.filter(deck=deck)
    context = {'list_of_cards': c_list}
    return render(request, 'leitner_deck.html', context)
