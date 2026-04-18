from functools import total_ordering

from django.core.paginator import Paginator
from django.db.models import F, Sum
from django.db.models.functions import Abs, Round, Coalesce
from django.shortcuts import render
from django.views import generic, View

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

def about(request):
    return render(request, 'about.html')


def u20_players_view(request):
    players=Player.objects.filter(age__lte=20).order_by('-price')
    context = {
        'players': players
    }
    return render(request, 'u20.html', context)


class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')
class Top150AccuratePredictionsView(View):
    def get(self, request):
        transfers = Transfer.objects.exclude(price_tft=0).filter(
            price__isnull=False,
            price_tft__isnull=False
        ).annotate(
            percent_of_accurate=Round(
                Abs(
                    (F('price') - F('price_tft')) / F('price') * 100,
                ),
                precision=2
            )
        ).order_by('percent_of_accurate')[:150]

        context = {
            'transfers': transfers
        }

        return render(request, 'stats/150-accurate-predictions.html', context)


class transfers_records(View):
    def get(self, request):
        transfers = Transfer.objects.exclude(
            price=0
        ).order_by('-price')

        paginator = Paginator(transfers, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj
        }

        return render(request, 'stats/transfers-records.html', context)
class Top50ClubsByExpenditureView(View):
    def get(self, request):
        clubs = Club.objects.annotate(
            total_expenditure=Sum(
                'import_transfers__price',
            )
        ).filter(total_expenditure__isnull=False).order_by('-total_expenditure')[:50]
        context = {
            'clubs': clubs
        }
        return render(request, 'stats/top-50-clubs-by-expenditure.html', context)


class Top50ClubsByIncomeView(View):
    def get(self, request):
        clubs = Club.objects.annotate(
            total_income=Sum(
                'export_transfers__price',
            )
        ).filter(total_income__isnull=False).order_by('-total_income')[:50]
        return render(request, 'stats/top-50-clubs-by-income.html', {
            'clubs': clubs
        })
