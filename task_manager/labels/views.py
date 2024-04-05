from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages
from task_manager.mixins import BaseRequiredMixin
from . forms import LabelsCreationForm
from . models import Labels
# Create your views here.


class CreateLabel(BaseRequiredMixin, generic.CreateView):
    form_class = LabelsCreationForm
    success_url = reverse_lazy('labels:labels_list')
    template_name = 'form.html'
    success_message = "Метка успешно создана"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать метку'
        context['button_value'] = 'Создать'
        return context


class LabelsList(View):

    def get(self, request):
        labels = Labels.objects.all()
        return render(request, 'labels/labels_list.html', context={'labels': labels})


class UpdateLabel(BaseRequiredMixin, generic.UpdateView):
    form_class = LabelsCreationForm
    success_url = reverse_lazy('labels:labels_list')
    template_name = 'form.html'
    success_message = "Метка успешно изменена"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить метку'
        context['button_value'] = 'Изменить'
        return context

    def get_queryset(self):
        return Labels.objects.filter(id=self.kwargs['pk'])


class DeleteLabel(BaseRequiredMixin, generic.DeleteView):
    model = Labels
    success_url = reverse_lazy('labels:labels_list')
    template_name = 'delete.html'
    error_url = reverse_lazy('labels:labels_list')
    success_message = "Метка успешно удалена"
    error_messages = "Невозможно удалить метку, потому что она используется"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить метку'
        context['object'] = Labels.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Labels.objects.filter(id=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().tasks_set.exists():
            messages.error(self.request, 'Невозможно удалить метку, потому что она используется')
            return redirect(self.error_url)
        return super().dispatch(request, *args, **kwargs)
