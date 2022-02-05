from django.urls import path
from .views import (
    ListQuestionView,
    CreateQuestionView,
)

app_name = 'tags'
urlpatterns = [
    path('', ListQuestionView.as_view(), name='list_questions'),
    path('create/', CreateQuestionView.as_view(), name='create_question'),
]
