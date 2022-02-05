from django.urls import path
from .views import (
    ListAnswerView,
    CreateAnswerView
)

app_name = 'tags'

urlpatterns = [
    path('', ListAnswerView.as_view(), name='list_answers'),
    path('create/', CreateAnswerView.as_view(), name='create_answer'),
]
