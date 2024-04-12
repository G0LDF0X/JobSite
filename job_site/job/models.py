from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name