from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField() # ckeditor Text Field
    content = RichTextUploadingField() # ckeditor Text Field + upload images
    author = models.ForeignKey(User, on_delete = models.PROTECT) # Protege o user
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title