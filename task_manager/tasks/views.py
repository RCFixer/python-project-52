from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages
from task_manager.mixins import BaseRequiredMixin
from . forms import TasksCreationForm
from . models import Tasks
from . filters import TaskFilter
# Create your views here.


class CreateTask(BaseRequiredMixin, generic.CreateView):
    form_class = TasksCreationForm
    success_url = reverse_lazy('tasks:tasks_list')
    template_name = 'form.html'
    success_message = 'Задача успешно создана'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать задачу'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(BaseRequiredMixin, generic.UpdateView):
    form_class = TasksCreationForm
    success_url = reverse_lazy('tasks:tasks_list')
    template_name = 'form.html'
    error_url = reverse_lazy('tasks:tasks_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение задачи'
        return context

    def get_queryset(self):
        return Tasks.objects.filter(id=self.kwargs['pk'])


class DeleteTask(BaseRequiredMixin, generic.DeleteView):
    model = Tasks
    success_url = reverse_lazy('tasks:tasks_list')
    template_name = 'delete.html'
    error_url = reverse_lazy('tasks:tasks_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление задачи'
        context['object'] = Tasks.objects.get(id=self.kwargs['pk'])
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.id == self.get_object().author.id:
            return super().dispatch(request, *args, **kwargs)
        messages.error(self.request, 'Задачу может удалить только ее автор')
        return redirect(self.error_url)


class TasksList(BaseRequiredMixin, View):

    def get(self, request):
        tasks = Tasks.objects.all()
        tasks_filter = TaskFilter(request.GET, queryset=tasks)
        return render(request, 'tasks/tasks_list.html', context={'filter': tasks_filter})


class TaskDetail(generic.DetailView):
    model = Tasks
    template_name = 'users/detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
