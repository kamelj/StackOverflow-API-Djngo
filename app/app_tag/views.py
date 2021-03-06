from .models import Tag
from .serializers import TagSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ListTagView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        srz_data = TagSerializer(instance=tags, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class CreateTagView(APIView):
    def post(self, request):
        srz_data = TagSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)