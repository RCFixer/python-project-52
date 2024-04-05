from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from task_manager.mixins import BaseRequiredMixin
from . forms import StatusesCreationForm
from . models import Statuses
# Create your views here.


class CreateStatus(BaseRequiredMixin, generic.CreateView):
    form_class = StatusesCreationForm
    success_url = reverse_lazy('statuses:statuses_list')
    template_name = 'form.html'
    success_message = "Статус успешно создан"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать статус'
        context['button_value'] = 'Создать'
        return context


class StatusesList(BaseRequiredMixin, View):

    def get(self, request):
        statuses = Statuses.objects.all()
        return render(request, 'statuses/statuses_list.html', context={'statuses': statuses})


class UpdateStatus(BaseRequiredMixin, generic.UpdateView):
    form_class = StatusesCreationForm
    success_url = reverse_lazy('statuses:statuses_list')
    template_name = 'form.html'
    success_message = "Статус успешно изменен"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить статус'
        context['button_value'] = 'Изменить'
        return context

    def get_queryset(self):
        return Statuses.objects.filter(id=self.kwargs['pk'])


class DeleteStatus(BaseRequiredMixin, generic.DeleteView):
    model = Statuses
    success_url = reverse_lazy('statuses:statuses_list')
    template_name = 'delete.html'
    success_message = "Статус успешно удален"
    error_messages = "Вы не можете удалить статус, он используется"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить статус'
        context['object'] = Statuses.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Statuses.objects.filter(id=self.kwargs['pk'])
