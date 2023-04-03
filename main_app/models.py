from django.db import models
from django.urls import reverse

# Create your models here.

ISHARD = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

class Weakness(models.Model):
    name: models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('weaknesses_detail', kwargs={'pk': self.id})

class Resistance(models.Model):
    name: models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    boss_number = models.IntegerField()
    weaknesses = models.ManyToManyField(Weakness)


    def __str__(self):
        return f"{self.title}, Boss Number: {self.boss_number}"
    
    def get_absolute_url(self):
        return reverse('show', kwargs={'game_id': self.id})

class Boss(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} : {self.game}"