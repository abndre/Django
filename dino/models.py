from django.db import models

# Create your models here.
class Player(models.Model):
    #gameId = models.AutoField(primary_key=True)
    name = models.CharField(primary_key=True,max_length=100)
    Score = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
