from django.urls import path
from .views import CreateStatus, StatusesList

urlpatterns = [
    path('', StatusesList.as_view(), name='statuses_list'),
    path('create/', CreateStatus.as_view(), name='create_status'),
]
