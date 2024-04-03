from django.urls import path
from .views import CreateStatus, StatusesList, UpdateStatus, DeleteStatus

app_name = 'statuses'

urlpatterns = [
    path('', StatusesList.as_view(), name='statuses_list'),
    path('create/', CreateStatus.as_view(), name='create_status'),
    path('<int:pk>/update/', UpdateStatus.as_view(), name='status_update'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='status_delete'),
]
