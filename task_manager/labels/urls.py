from django.urls import path
from .views import CreateLabel, LabelsList, UpdateLabel, DeleteLabel

app_name = 'labels'

urlpatterns = [
    path('', LabelsList.as_view(), name='labels_list'),
    path('create/', CreateLabel.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabel.as_view(), name='label_update'),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name='label_delete'),
]
