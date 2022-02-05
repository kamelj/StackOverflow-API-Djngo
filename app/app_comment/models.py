from django.db import models
from app_answer.models import Answer
from app_question.models import Question
from app_user.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    belong_to = models.CharField(max_length=1, choices = (('1', 'answer'), ('2', 'question')), default='1')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments', blank=True, default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments', blank=True, default='')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
