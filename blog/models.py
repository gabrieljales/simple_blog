from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.PROTECT) # Protege o user
    created_at = models.DateField(auto_now_add = True)