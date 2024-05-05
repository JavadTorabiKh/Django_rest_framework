from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
import json
from .models import Todo
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TodoSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# region function view
User = get_user_model()


@api_view(["GET", "POST"])
def get_users(request: Request):
    if request.method == "GET":
        json_data = list(Todo.objects.all())
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

class TodosMixinListApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class TodosMixinDetailApi(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

# endregion


# region generics
class TodosGenericsPaginationSize(PageNumberPagination):
    page_size = 3


class TodosGenericsListApiView(generics.ListCreateAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodosGenericsPaginationSize

    # authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TodosGenericsDetailApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# endregion


# region viewset

class TodosviewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = PageNumberPagination


class UsersViewSetApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# endregion
