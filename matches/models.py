# models.py

from django.db import models
from django.utils import timezone

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    division = models.ForeignKey('Division', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='team_images/')
    stadium_name = models.CharField(max_length=255, null=True, blank=True)
    stadium_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    home = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
    away = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    place = models.ForeignKey(Team, related_name='match_place', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.home} vs {self.away} at {self.place.stadium_name if self.place else 'Unknown Location'} on {self.time}"
