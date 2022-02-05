from rest_framework import serializers
from app_answer.serializers import AnswerSerializer
from app_comment.serializers import CommentSerializer
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_answers(self, obj):
        answers = obj.answers.all()
        return AnswerSerializer(instance=answers, many=True).data

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializer(instance=comments, many=True).data

    class Meta:
        model = Question
        fields = '__all__'
