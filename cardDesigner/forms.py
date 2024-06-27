"""
The `forms.py` module in the `cardDesigner` app defines the Django forms used for creating and updating cards and decks.

The `CardForm` class is a Django `ModelForm` that represents the `Card` model, with fields for the question, answer, and associated deck.

The `DeckForm` class is a Django `ModelForm` that represents the `Deck` model, with fields for the title, subject, and description. The `widgets` attribute is used to customize the HTML attributes of the form fields.

The `CardFormSet` is an inline formset factory that allows creating and updating multiple `Card` instances associated with a `Deck` instance. The `fields` attribute specifies the fields to include, `can_delete` is set to `False` to disable deleting cards, `extra` is set to 1 to add one extra empty card form, and the `widgets` attribute is used to customize the HTML attributes of the question and answer form fields.
"""
from .models import Card, Deck
from django.forms import ModelForm, Textarea, inlineformset_factory, TextInput
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView


# Create the form class.
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'deck')
        

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ('title', 'subject', 'description')
        widgets = {'title':
                                TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': "",
                                }),
                    'subject':
                                TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': " Language level one or two",
                                }),
                    'description':
                                Textarea(attrs={
                                'class': 'form-control',
                                'placeholder': "Description or phrase",
                                }),
                    }


CardFormSet = inlineformset_factory(
                Deck, Card,
                fields=('question','answer'),
                can_delete=False,
                extra=1,
                widgets={
                    'question': TextInput(attrs={"class":"form-control form-control-lg",
                                                    "placeholder":"Question",}),
                    'answer': TextInput(attrs={"class":"form-control",
                                                    "placeholder":"Answer"}),


                        }

                )