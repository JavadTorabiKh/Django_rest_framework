from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
import json
from .models import Todo
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TodoSerializer


@api_view(["GET", "POST"])
def get_users(request: Request):
    if request.method == "GET":
        json_data = list(Todo.objects.all().values())
        todo_serializer = TodoSerializer(json_data, many=True)

        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == "POST":
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response({"status": "success", "data": todo_serializer.data}, status.HTTP_201_CREATED)
        return Response({"status": "erorr"}, status.HTTP_400_BAD_REQUEST)
