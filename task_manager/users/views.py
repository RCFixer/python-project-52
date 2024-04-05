from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.messages.views import SuccessMessageMixin
from . forms import CustomUserCreationForm
from . models import CustomUser
# Create your views here.


class SignUp(SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'form.html'
    success_message = "Пользователь успешно зерегистрирован"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['button_value'] = 'Зарегистрировать'
        return context


class EditUser(SuccessMessageMixin, generic.UpdateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:users_list')
    template_name = 'form.html'
    success_message = "Пользователь успешно изменен"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пользователя'
        context['button_value'] = 'Изменить'
        return context

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.kwargs['pk'])


class DeleteUser(SuccessMessageMixin, generic.DeleteView):
    model = CustomUser
    success_url = reverse_lazy('users:users_list')
    template_name = 'delete.html'
    success_message = "Пользователь успешно удалён"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление пользователя'
        context['object'] = CustomUser.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.kwargs['pk'])


class UsersList(View):

    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, 'users/users_list.html', context={'users': users})
