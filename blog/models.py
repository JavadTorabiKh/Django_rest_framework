from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    first_name = models.CharField(max_length=110, verbose_name='نام')
    last_name = models.CharField(max_length=220, verbose_name='تام خانوادگی')
    email = models.EmailField()
    age = models.IntegerField(default=0)
    website_adders = models.URLField()
    score = models.FloatField()
    score_2 = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-age']
        # db_table = 't'
        verbose_name = 'شخص'
        verbose_name_plural = 'اشخاص'

    def __str__(self):
        return f"Name:{self.first_name}-{self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=110)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/articles/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_show = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    articles = models.Manager()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title


