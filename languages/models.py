"""
This module defines the Django models for the languages application.

The `Deck` model represents a collection of flashcards on a specific subject. Each deck has a title, subject, description, and a creator (a Django `User` object).

The `Card` model represents an individual flashcard, with a question and an answer. Each card is associated with a specific `Deck`.

The `StudySet` model represents a set of flashcards that a user is studying. The `StudentDeck` model links a `StudySet` to a specific `Deck`.

The `LeitnerBox` model represents a Leitner box, which is a system for spaced repetition learning. The `ScoreBoard` model tracks a user's progress through the Leitner boxes for each card.
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Deck(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_decks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('create_cards', kwargs={'deck_id': self.id})

class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class StudySet(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="study_sets")

class StudentDeck(models.Model):
    study_set = models.ForeignKey(StudySet, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

class LeitnerBox(models.Model):
    frequency = models.SmallIntegerField()

    def __str__(self):
        return str(self.frequency)

class ScoreBoard(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scoreboards")
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    box = models.ForeignKey(LeitnerBox, on_delete=models.CASCADE)
    updated = models.DateField()
    leitner_date = models.DateField()

    def __str__(self):
        return str(self.card)
