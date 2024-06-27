"""
This module defines the Django admin configuration for the card designer application.

The following models are registered with the Django admin interface:
- Deck: Represents a deck of cards, with fields for the title, subject, creator, and description.
- Card: Represents a single card in a deck, with fields for the question and answer, and a foreign key to the deck.
- StudySet: Represents a set of cards that a student is studying, with a foreign key to the student.
- StudentDeck: Represents a deck of cards that a student is studying, with foreign keys to the study set and the deck.
- LeitnerBox: Represents a Leitner box for a student's card review, with a field for the frequency.
- ScoreBoard: Represents a student's score for a card, with fields for the student, card, box, update timestamp, and Leitner date.

The admin configuration for each model includes the fields that should be displayed in the admin interface.
"""
from django.contrib import admin

# Register your models here with django admin.

from django.contrib import admin
from .models import Deck, Card, StudySet, LeitnerBox, ScoreBoard, StudentDeck

@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    fields = ['title', 'subject', 'creator', 'description']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    fields = ['question', 'answer', 'deck']

@admin.register(StudySet)
class StudySetAdmin(admin.ModelAdmin):
    fields = ['student']

@admin.register(StudentDeck)
class StudentDeckAdmin(admin.ModelAdmin):
    fields = ['studyset', 'student', 'deck']

@admin.register(LeitnerBox)
class LeitnerBoxAdmin(admin.ModelAdmin):
    fields = ['frequency']

@admin.register(ScoreBoard)
class ScoreBoardAdmin(admin.ModelAdmin):
    fields = ['student', 'card', 'box', 'updated', 'leitner_date']

