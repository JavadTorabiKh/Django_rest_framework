from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Todo(models.Model):
    name = models.CharField(max_length=500)
    user = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name="todos")
