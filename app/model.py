from django.db import models

#Creating the base in the database 
class Score(models.model):
    player_name = models.CharField(max_length=100) #max 100 caracter
    points = models.IntegerFielf(default=0) #the points at the beginning 

    def __str__(self):
        return f"{self.player_name} : {self.points} pts"
