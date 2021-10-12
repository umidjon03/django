from django.db import models

# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.IntegerField()

    def __str__(self):
        return self.name


class Opinion(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name