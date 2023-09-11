from django.db import models

# Create your models here.
class Room(models.Model):
    #host = models.CharField(max_length=50)
    #topic =
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    #participants = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name