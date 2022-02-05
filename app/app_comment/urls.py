from django.urls import path
from .views import (
    ListCommentView,
    CreateCommentView,
)

app_name = 'comments'
urlpatterns = [
    path('', ListCommentView.as_view(), name='list_comments'),
    path('create/', CreateCommentView.as_view(), name='create_comment'),
]
