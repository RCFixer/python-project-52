from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from . forms import StatusesCreationForm
from . models import Statuses
# Create your views here.


class CreateStatus(generic.CreateView):
    form_class = StatusesCreationForm
    success_url = reverse_lazy('statuses_list')
    template_name = 'statuses/create.html'


class StatusesList(View):

    def get(self, request):
        statuses = Statuses.objects.all()
        return render(request, 'statuses/statuses_list.html', context={'statuses': statuses})
        pass
