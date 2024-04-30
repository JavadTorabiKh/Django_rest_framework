from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
import json
from .models import Todo
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from rest_framework.views import APIView

# region function view


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


@api_view(["GET", "PUT", "DELETE"])
def get_user(request: Request, todoId: int):

    try:
        todo = Todo.objects.get(pk=todoId)
    except Todo.DoesNotExist:
        return Response({"status": "erorr"}, status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        todo_serializer = TodoSerializer(todo, many=False)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    elif request.method == "PUT":
        todo_serializer = TodoSerializer(todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status.HTTP_202_ACCEPTED)
        return Response({"status": "erorr"}, status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

# endregion

# region class base view


class TodosListApiView(APIView):
    def get(self, request: Request):
        json_data = list(Todo.objects.all().values())
        todo_serializer = TodoSerializer(json_data, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response({"status": "success", "data": todo_serializer.data}, status.HTTP_201_CREATED)
        return Response({"status": "erorr"}, status.HTTP_400_BAD_REQUEST)


class TodosDetailApiView(APIView):
    def get_obj(self, todoId: int):
        try:
            return Todo.objects.get(pk=todoId)
        except Todo.DoesNotExist:
            return None

    def get(self, request: Request, todoId: int):
        todo = self.get_obj(todoId)
        if todo:
            todo_serializer = TodoSerializer(todo, many=False)
            return Response(todo_serializer.data, status.HTTP_200_OK)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, todoId: int):
        todo = self.get_obj(todoId)
        todo_serializer = TodoSerializer(todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status.HTTP_202_ACCEPTED)
        return Response({"status": "erorr"}, status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, todoId: int):
        todo = self.get_obj(todoId)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

# endregion


# region mixin


# endregion
