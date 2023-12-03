from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SearchForm(forms.Form):
    classification = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search by genre, artist, or event'}), required=True, label=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a city e.g., Hartford'}), required=True, label=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Search'))
