from django.urls import path
from app_tag.views import (
    ListTagView,
    CreateTagView
)

app_name = 'tags'

urlpatterns = [
    path('', ListTagView.as_view(), name='list_tags'),
    path('create/', CreateTagView.as_view(), name='create_tag'),
]
