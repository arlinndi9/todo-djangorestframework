from django.db import models

# Create your models here.



class Todos(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    location=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.title
