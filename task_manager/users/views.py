from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from . forms import UserCreationForm
from . models import CustomUser
# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class UsersList(View):

    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, 'users/users_list.html', context={'users': users})
