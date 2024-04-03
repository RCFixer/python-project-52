from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class BaseRequiredMixin(LoginRequiredMixin, SuccessMessageMixin):
    # success_url = ""
    # error_url = ""
    login_url = reverse_lazy('login')
    success_message = 'Успешно'
    permission_denied_message = 'Что-то пошло не так'
    error_messages = 'У вас недостаточно прав'
