from django.db import models
from django.urls import reverse

class Player(models.Model):
    LEVELS = [
        ('Advanced', 'Advanced'),
        ('Intermediate', 'Intermediate'),
        ('N/A', 'N/A'),
    ]
    TEAMNAME = [
        ('Wardique', 'Wardique'),
        ('Tochka', 'Tochka'),
        ('Palmer', 'Palmer'),
        ('Bristol', 'Bristol'),
        ('Waffels', 'Waffels'),
        ('Tonys', 'Tonys'),
        ('Platinum', 'Platinum'),
        ('N/A', 'N/A'),
    ]
    name = models.CharField("First & last name", max_length=200)
    email = models.CharField("Email", max_length=200)
    teamLevel = models.CharField("Team Level", max_length=200, choices=LEVELS, blank=False)
    teamName = models.CharField("Team Name", max_length=200, choices=TEAMNAME, blank=False)
    phoneNum = models.CharField("Phone Number", max_length=200)
    def __str__(self):
       return self.name
    def get_absolute_url(self):
       return reverse('player-detail', args=[str(self.id)])