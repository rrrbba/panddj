from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User #allows access to user functionality

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #on_delete=models.CASCADE helps with the integrity of the data. In relational databases, one of the principles is to protect consistency. There shouldn’t be an item in one table that references the foreign key of something that has been removed from another. 