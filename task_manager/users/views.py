from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from . forms import UserCreationForm
from . models import CustomUser
# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'form.html'
    success_message = "Пользователь успешно зерегистрирован"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class EditUser(generic.UpdateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:users_list')
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пользователя'
        return context

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.kwargs['pk'])


class DeleteUser(generic.DeleteView):
    model = CustomUser
    success_url = reverse_lazy('users:users_list')
    template_name = 'delete.html'

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