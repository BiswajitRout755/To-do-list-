from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  #this User will keep track of the logged in user into the application.
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    complete=models.BooleanField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering= ['complete']  #ordering ('complete') means every completed works should be sent to the bottom of the list..
