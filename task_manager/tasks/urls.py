from django.urls import path
from .views import CreateTask, TasksList, UpdateTask, DeleteTask, TaskDetail

app_name = 'tasks'

urlpatterns = [
    path('', TasksList.as_view(), name='tasks_list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='task_update'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='task_delete'),
]
