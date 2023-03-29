from django.db import models

# Create your models here.
class Boss(models.Model):
    name = models.CharField(max_length=100)
    game = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    difficulty = models.IntegerField()

def __str__(self):
    return f"{self.name} : {self.game}"