from django import forms
from . models import Labels


class LabelsCreationForm(forms.ModelForm):

    class Meta:
        model = Labels
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].label = 'Имя'
