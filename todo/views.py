from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
import json
from .models import Todo


def get_users(request):
    json_data = list(Todo.objects.all().values())
    # json_data = json.dumps({"data": json_data})

    return JsonResponse({"data": json_data})
