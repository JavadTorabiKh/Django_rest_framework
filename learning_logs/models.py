from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    # چیزی است که درباره Topic است
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # در پنل مدیریت با این اسم نوشته شود
    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.text[:50]} ..."
