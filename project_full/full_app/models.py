from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    number=models.IntegerField()
    message=models.TextField(max_length=1200)

    def __str__(self):
        return self.name
