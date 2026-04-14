from django.shortcuts import render

from main.models import Club, Transfer, Season, Player


def home_view(request):
    return render(request, 'index.html')


def clubs(request):
    clubs = Club.objects.all()
    country_query=request.GET.get('country')
    if country_query:
        clubs = clubs.filter(country__name=country_query)

    context = {
        'clubs': clubs,
    }
    return render(request, 'clubs.html', {'clubs': clubs})

def latest_transfers(request):
    transfers = Transfer.objects.filter(
        season=Season.objects.last()
    ).order_by('-price')
    context = {
        'transfers': transfers
    }
    return render(request, 'latest-transfers.html', context)

def players_view(request):
    players = Player.objects.order_by('-price')
    context = {
        'players': players
    }
    return render(request, 'players.html', context)


def tryouts_view(request):
     return render(request, 'tryouts.html')

def u20_players_view(request):
    players=Player.objects.filter(age__lte=20).order_by('-price')
    context = {
        'players': players
    }
    return render(request, 'u20.html', context)