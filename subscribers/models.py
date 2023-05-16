from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email