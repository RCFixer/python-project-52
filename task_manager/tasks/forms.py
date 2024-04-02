from django import forms
from django.contrib.auth.hashers import make_password
from . models import Tasks


class TasksCreationForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']

    # def save(self, commit=True):
    #     instance = super(TasksCreationForm, self).save(commit=False)
    #     instance.author = self.request.user
    #     if commit:
    #         instance.save()
    #     return instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].label = 'Имя'
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].label = 'Описание'
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].label = 'Статус'
        self.fields['executor'].widget.attrs.update({'class': 'form-control'})
        self.fields['executor'].label = 'Исполнитель'
        self.fields['labels'].widget.attrs.update({'class': 'form-control'})
        self.fields['labels'].label = 'Метки'
