from django import forms
from django.contrib.auth.hashers import make_password
from . models import CustomUser


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'second_name', 'username', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Введенные пароли не совпадают.')
        cleaned_data['password'] = make_password(password)
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['first_name'].label = 'Имя'
        # self.fields['second_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['second_name'].label = 'Фамилия'
        self.fields['password'].help_text = 'Ваш пароль должен содержать как минимум 3 символа.'
        self.fields['password2'].help_text = 'Для подтверждения введите, пожалуйста, пароль ещё раз.'
