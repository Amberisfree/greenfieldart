
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

# strip means to remove whitespace from the beginning and the end before storing the column
class ReviewForm(forms.Form):
    review = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
