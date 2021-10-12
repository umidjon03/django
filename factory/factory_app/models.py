from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    location=models.TextField()
    email=models.EmailField()
    message=models.TextField()
    emailcopy=models.NullBooleanField(null=True,blank=True)
    human=models.NullBooleanField(null=True,blank=True)

    def __str__(self):
        return self.name