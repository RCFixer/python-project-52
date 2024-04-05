# from django import forms
# from django.contrib.auth.hashers import make_password
# from . models import CustomUser
#
#
# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label='Подтверждение пароля',
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'username']
#
#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     password = cleaned_data.get('password1')
#     #     password2 = cleaned_data.get('password2')
#     #     if password != password2:
#     #         raise forms.ValidationError('Введенные пароли не совпадают.')
#     #     cleaned_data['password'] = make_password(password)
#     #     temp1 = cleaned_data.pop('password1', 'Key not found')
#     #     temp2 = cleaned_data.pop('password2', 'Key not found')
#     #     return cleaned_data
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password1')
#         password2 = cleaned_data.get('password2')
#         if password != password2:
#             raise forms.ValidationError('Введенные пароли не совпадают.')
#         cleaned_data['password'] = make_password(password)
#         return cleaned_data
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].label = 'Имя пользователя'
#         self.fields['first_name'].label = 'Имя'
#         # self.fields['second_name'].widget.attrs.update({'class': 'form-control'})
#         self.fields['last_name'].label = 'Фамилия'
#         self.fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 3 символа.'
#         self.fields['password2'].help_text = 'Для подтверждения введите, пожалуйста, пароль ещё раз.'

from task_manager.users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password1'].help_text = "Ваш пароль должен содержать как минимум 3 символа."

    def clean_username(self):
        """Reject usernames that differ only in case
        and allow to use same username"""

        if 'username' in self.changed_data:
            return super().clean_username()
        return self.cleaned_data.get("username")
