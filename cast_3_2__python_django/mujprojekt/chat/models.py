from django.db import models

# Create your models here.
class Message(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False, max_length=10000)
