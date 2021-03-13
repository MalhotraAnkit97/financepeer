from django.db import models

# Create your models here.
from django.db import models


class user(models.Model):
    userid = models.IntegerField(primary_key=True)
    id= models.IntegerField()
    title = models.CharField(max_length=500)
    body = models.CharField(max_length = 500)
    file = models.FileField(upload_to='pics', blank=True)

    def __str__(self):
        return self.id