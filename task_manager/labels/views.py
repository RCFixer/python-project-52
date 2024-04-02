from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from . forms import LabelsCreationForm
from . models import Labels
# Create your views here.


class CreateLabel(generic.CreateView):
    form_class = LabelsCreationForm
    success_url = reverse_lazy('labels_list')
    template_name = 'labels/create.html'


class LabelsList(View):

    def get(self, request):
        labels = Labels.objects.all()
        return render(request, 'labels/labels_list.html', context={'labels': labels})
        pass
