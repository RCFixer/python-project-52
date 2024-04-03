from django import forms
from . models import Statuses


class StatusesCreationForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Имя'
