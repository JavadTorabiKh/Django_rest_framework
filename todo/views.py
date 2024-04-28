from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
import json
from .models import Todo
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_users(request: Request):
    json_data = list(Todo.objects.all().values())

    # json_data = json.dumps({"data": json_data})
    # return JsonResponse({"data": json_data})

    return Response({"data": json_data}, status.HTTP_200_OK)
