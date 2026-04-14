from django.contrib import admin

from main.models import *

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PlayerInline(admin.StackedInline):
    model = Player
    extra = 1

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'president', 'coach','found_date', 'country')
    list_filter = ('country',)
    search_fields = ('name',)
    inlines = (PlayerInline,)
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'number', 'age', 'club', 'price', 'country',)
    list_filter = ('country','club', 'age', 'number','position')
    search_fields = ('name',)
    ordering = ('-price',)
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('player', 'old_club', 'new_club','price','price_tft','date','season')
    list_filter = ('player', 'old_club', 'new_club','season')
    ordering = ('-price','player__name')


