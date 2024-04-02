from django.urls import path
from .views import SignUp, UsersList

urlpatterns = [
    path('', UsersList.as_view(), name='users_list'),
    path('create/', SignUp.as_view(), name='signup'),
]
