from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Creating posts model/class
class  Post(models.Model): #each class is going to be its own table in DB
    title = models.CharField(max_length=100) #field/attribute
    content = models.TextField() #unrestricted coz it could be big
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
