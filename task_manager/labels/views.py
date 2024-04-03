from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from . forms import LabelsCreationForm
from . models import Labels
# Create your views here.


class CreateLabel(generic.CreateView):
    form_class = LabelsCreationForm
    success_url = reverse_lazy('labels_list')
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать метку'
        return context


class LabelsList(View):

    def get(self, request):
        labels = Labels.objects.all()
        return render(request, 'labels/labels_list.html', context={'labels': labels})
        pass
