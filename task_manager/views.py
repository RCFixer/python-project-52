from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


class SignIn(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Вход', 'button_value': 'Войти'}
    success_message = 'Вы залогинены'


class LogOut(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
