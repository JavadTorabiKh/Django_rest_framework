from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_dateTime = models.DateTimeField()
    image = models.ImageField(blank=True, null=True)
    is_show = models.BooleanField(default=False)
    auther = models.ForeignKey("Person", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return (self.first_name +" "+ self.last_name)

