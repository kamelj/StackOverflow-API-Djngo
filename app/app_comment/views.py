from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer
from permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ListCommentView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        srz_data = CommentSerializer(instance=comments, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class CreateCommentView(APIView):
    def post(self, request):
        srz_data = CommentSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)