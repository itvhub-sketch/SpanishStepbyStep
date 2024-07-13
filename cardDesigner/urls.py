from django.urls import path
from . import views
from .views import DeckCreate
from django.conf import settings  # Import the settings module
from django.conf.urls.static import static  # Import the static function

urlpatterns = [ 
    path('', views.show_all_decks, name='all_decks'),
    path('card/all/', views.show_all_cards, name='all_cards'),
    path('deck/practice/<int:deck_id>/text-to-speech/<int:card_id>/', views.text_to_speech, name='text_to_speech'),  # Trailing slash added
    path('cards/', views.show_all_cards, name='all_cards'),
    path('cards/delete/<int:card_id>/', views.delete_card, name='delete_card'),
    path('decks/', views.show_all_decks, name='all_decks'),
    path('deck/<int:deck_id>/', views.create_cards, name='create_cards'),
    path('deck/delete/<int:deck_id>/', views.delete_deck, name='delete_deck'),
    path('decks/create/', DeckCreate.as_view(), name='create_deck'),
    path('deck/show/<int:deck_id>/', views.show_deck, name='show_deck'),
    path('deck/practice/<int:deck_id>/', views.practice_deck, name='practice_deck'),
    path('deck/save/<int:deck_id>/', views.save_for_study, name='save_for_study'),
    path('studyset/', views.show_my_studyset, name='show_my_studyset'),
    path('studyset/remove/<int:studentdeck_id>/', views.remove_from_studyset, name='remove_from_studyset'),
    path('deck/leitner/<int:deck_id>/', views.leitner, name='leitner'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
