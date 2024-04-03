from django import forms
from django.contrib.auth.hashers import make_password
from . models import Tasks


class TasksCreationForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Имя'
        self.fields['description'].label = 'Описание'
        self.fields['status'].label = 'Статус'
        self.fields['executor'].label = 'Исполнитель'
        self.fields['labels'].label = 'Метки'
