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

class Resistance(models.Model):
    name: models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    boss_number = models.IntegerField()

    def __str__(self):
        return f"{self.title}, Boss Number: {self.boss_number}"

class Boss(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    weaknesses = models.ManyToManyField(Weakness)
    resistances = models.ManyToManyField(Resistance)
    ishard = models.CharField(
        max_length=1,
        choices=ISHARD,
        default=ISHARD[0][0],
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} : {self.game}"