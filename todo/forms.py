# Django provides the functionality to automatically generate a form from a
# model and it will automatically check for blank fields and if there's a
# blank field it'll make it required input.
from django import forms
from .models import Item

# Will inherit from forms.ModelForm


class ItemForm(forms.ModelForm):

    # Inner class just allows us to provide some additional information to
    # Django to tell it we want this form to be based off the Item model and
    # the fields that we want to fill in our the name and the done
    class Meta:
        model = Item
        fields = ('name', 'done')
