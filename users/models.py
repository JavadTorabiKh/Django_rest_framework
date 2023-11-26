from django.db import models

class Topics(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
    
class Entry(models.Model):
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE)
    title = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "entries"
        
    def __str__(self):
        return f'{self.title[:50]} ....'
