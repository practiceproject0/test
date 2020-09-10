from django.db import models


# Create your models here.
class DBConnection(models.Model):
    name = models.CharField("name",max_length=255)
    email = models.EmailField("email",max_length=150)
    DoB = models.DateTimeField("DoB",auto_now_add=True)

