from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from . forms import TasksCreationForm
from . models import Tasks
# Create your views here.


class CreateTask(generic.CreateView):
    form_class = TasksCreationForm
    success_url = reverse_lazy('tasks_list')
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksList(View):

    def get(self, request):
        tasks = Tasks.objects.all()
        return render(request, 'tasks/tasks_list.html', context={'tasks': tasks})
