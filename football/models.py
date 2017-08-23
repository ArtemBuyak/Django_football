from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=200)
    number_of_players = models.IntegerField(default=5)
    team_captain = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Referee(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.IntegerField(default=25)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.second_name


class Cup(models.Model):
    cup_name = models.CharField(max_length=200)
    cup_information = models.TextField(default="Это будет очень хороший турнир!")
    count_commands = models.IntegerField(default=8)
    prize = models.IntegerField(default=1000)
    date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days = 30))
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)


    def __str__(self):
        return self.cup_name


class Lists(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE)



class ArchiveGame(models.Model):
    tourney = models.ForeignKey(Cup, on_delete=models.CASCADE)
    team_first = models.ForeignKey(Team, related_name='first_team', on_delete=models.CASCADE)
    team_second = models.ForeignKey(Team, related_name='second_team', on_delete=models.CASCADE, default=0)
    goal_first = models.IntegerField(default=0)
    goal_second = models.IntegerField(default=0)
    tour = models.IntegerField(default=0)


class Winner(models.Model):
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE)

    def __str__(self):
        return "Winner: %s" % (Team.objects.get(id = self.winner))