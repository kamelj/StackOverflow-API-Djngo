from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tags/', include('app_tag.urls', namespace='tags')),
    path('comments/', include('app_comment.urls', namespace='comments')),
    path('answers/', include('app_answer.urls', namespace='answers')),
    path('questions/', include('app_question.urls', namespace='questions')),
    path('users/', include('app_user.urls', namespace='users')),
]
