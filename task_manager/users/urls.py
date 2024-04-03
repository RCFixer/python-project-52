from django.urls import path
from .views import SignUp, UsersList, EditUser, DeleteUser

app_name = 'users'

urlpatterns = [
    path('', UsersList.as_view(), name='users_list'),
    path('create/', SignUp.as_view(), name='signup'),
    path('<int:pk>/update/', EditUser.as_view(), name='user_update'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='user_delete'),
]
