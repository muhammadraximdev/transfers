from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Season(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clubs/', blank=True, null=True) # null=True qilindi
    president = models.CharField(max_length=50, blank=True, null=True)
    coach = models.CharField(max_length=50, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    number = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    age = models.SmallIntegerField(blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, blank=True, null=True) # null=True qo'shildi
    old_club = models.ForeignKey(Club, on_delete=models.SET_NULL, blank=True, null=True, related_name='export_transfers')
    new_club = models.ForeignKey(Club, on_delete=models.SET_NULL, blank=True, null=True, related_name='import_transfers')
    price = models.FloatField(blank=True, null=True)
    price_tft = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.player} | {self.old_club} -> {self.new_club}"