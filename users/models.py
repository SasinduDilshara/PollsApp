from django.db import models
from django.contrib.auth.models import User
import uuid

class AppUser(models.Model):
    """
    Has a one-to-one mapping with [django.contrib.auth.models.User] object.
    """
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # If the auth user object is deleted, this object will also be deleted.
    auth = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    
    snippet = models.CharField(max_length=90)
    number = models.IntegerField()
    
    # Image foreign key. Would not let the image be deleted
    # if the image is linked with a user.
    def username(self):
        return self.auth.username
    def __str__(self):
        return self.username()
    class Meta:
        unique_together = (('number','snippet'),)
        ordering = ['number']
