

# SPANISH Step-by-Step
Cloud Based Flashcard Module Integration with Moodle, Emphasizing Accessibility

 User Documentation for CardBased Learning Application

 Table of Contents

1. Introduction(introduction)
2. Getting Started(gettingstarted)
     System Requirements(systemrequirements)
     Installation(installation)
     Running the Application(runningtheapplication)
3. User Registration and Authentication(userregistrationandauthentication)
4. Managing Decks(managingdecks)
     Creating a Deck(creatingadeck)
     Viewing Decks(viewingdecks)
     Editing a Deck(editingadeck)
     Deleting a Deck(deletingadeck)
5. Managing Cards(managingcards)
     Creating a Card(creatingacard)
     Viewing Cards(viewingcards)
     Editing a Card(editingacard)
     Deleting a Card(deletingacard)
6. Studying with Decks(studyingwithdecks)
     Starting a Study Session(startingastudysession)
     Tracking Progress(trackingprogress)
7. TexttoSpeech Feature(texttospeechfeature)
8. Troubleshooting(troubleshooting)
9. Contact and Support(contactandsupport)

 Introduction

Welcome to the CardBased Learning Application! This platform allows users to create, manage, and study using decks of flashcards. The application supports features such as spaced repetition and realtime updates to help optimize your learning experience.

 Getting Started

 System Requirements

 Python 3.8 or higher
 Django 3.2 or higher
 SQLite (for local development)
 Web browser (latest version of Chrome, Firefox, Safari, or Edge)

 Installation

1. Clone the repository:
   bash
   git clone https://github.com/yourrepo/cardlearningapp.git
   cd cardlearningapp
   

2. Create a virtual environment:
   bash
   python m venv venv
   source venv/bin/activate   On Windows: venv\Scripts\activate
   

3. Install dependencies:
   bash
   pip install r requirements.txt
   

4. Apply migrations:
   bash
   python manage.py migrate
   

5. Create a superuser:
   bash
   python manage.py createsuperuser
   

 Running the Application

1. Start the development server:
   bash
   python manage.py runserver
   

2. Open your web browser and navigate to:
   
   http://127.0.0.1:8000/
   

 User Registration and Authentication

 Registering a New User

1. Navigate to the registration page: /register/.
2. Fill in the required fields: username, email, password.
3. Submit the form to create your account.

 Logging In

1. Navigate to the login page: /login/.
2. Enter your username and password.
3. Click the "Login" button to access your account.

 Logging Out

1. Click on your username in the navigation bar.
2. Select "Logout" from the dropdown menu.

 Managing Decks

 Creating a Deck

1. Navigate to /decks/create/.
2. Fill in the deck details: title, subject, description.
3. Click "Save" to create the deck.

 Viewing Decks

1. Navigate to /decks/ to view a list of all decks.
2. Click on a deck title to view its details.

 Editing a Deck

1. Navigate to the deck detail page: /decks/<deck_id>/.
2. Click the "Edit" button.
3. Update the deck details and click "Save".

 Deleting a Deck

1. Navigate to the deck detail page: /decks/<deck_id>/.
2. Click the "Delete" button.
3. Confirm the deletion.

 Managing Cards

 Creating a Card

1. Navigate to /cards/create/.
2. Select the deck for the new card.
3. Fill in the card details: question, answer, (optional) question audio, answer audio.
4. Click "Save" to create the card.

 Viewing Cards

1. Navigate to the deck detail page: /decks/<deck_id>/.
2. View the list of cards within the deck.

 Editing a Card

1. Navigate to the card detail page: /cards/<card_id>/.
2. Click the "Edit" button.
3. Update the card details and click "Save".

 Deleting a Card

1. Navigate to the card detail page: /cards/<card_id>/.
2. Click the "Delete" button.
3. Confirm the deletion.

 Studying with Decks

 Starting a Study Session

1. Navigate to the deck detail page: /decks/<deck_id>/.
2. Click the "Start Study Session" button.
3. Follow the onscreen prompts to review and answer the cards.

 Tracking Progress

1. Navigate to your dashboard: /dashboard/.
2. View your study progress and statistics for each deck.

 TexttoSpeech Feature

 Using TexttoSpeech

1. Navigate to the card detail page: /cards/<card_id>/.
2. Click the "Play Question Audio" or "Play Answer Audio" button to hear the audio.
3. Ensure your browser supports audio playback.

 Troubleshooting TexttoSpeech

 Ensure you have internet access if using cloudbased TTS services.
 Verify that audio files are correctly uploaded and accessible.
 Check the browser console for any errors and consult the Troubleshooting(troubleshooting) section.

 Troubleshooting

 Common Issues

1. Unable to create or edit decks/cards:
    Ensure all required fields are filled.
    Check for any validation error messages.

2. TexttoSpeech not working:
    Verify internet connection.
    Ensure audio files are properly uploaded.
    Check browser console for errors.

3. Login issues:
    Verify username and password.
    Check if the account is activated.

