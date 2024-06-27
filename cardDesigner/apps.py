"""
The CardmakerConfig class is an AppConfig subclass that provides configuration for the 'cardDesigner' Django app. It sets the name attribute to 'cardDesigner', which is the name of the app.
"""
from django.apps import AppConfig


class CardmakerConfig(AppConfig):
    name = 'cardDesigner'