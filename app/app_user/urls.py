from django.urls import path
from .views import (
    ListUserView,
    CreateUserView,
)

app_name = 'users'

urlpatterns = [
    path('', ListUserView.as_view(), name='list_users'),
    path('create/', CreateUserView.as_view(), name='create_user'),
]
