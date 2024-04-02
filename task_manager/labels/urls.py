from django.urls import path
from .views import CreateLabel, LabelsList

urlpatterns = [
    path('', LabelsList.as_view(), name='labels_list'),
    path('create/', CreateLabel.as_view(), name='create_label'),
]
