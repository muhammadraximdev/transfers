from django.contrib import admin
from django.urls import path
from main import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),
    path('clubs/', views.clubs, name='clubs'),
    path('latest-transfers/', views.latest_transfers, name='latest-transfers'),
    path('players/', views.players_view, name='players'),
    path('tryouts/', views.tryouts_view, name='tryouts'),
    path('about/', views.about, name='about'),
    path('u20/',views.u20_players_view, name='u20'),
    path('stats/',views.StatsView.as_view(), name='stats'),
    path('stats/150-accurate-predictions/',views.Top150AccuratePredictionsView.as_view(), name='150-accurate-predictions'),
    path('stats/transfers-records/',views.transfers_records.as_view(), name='transfers-records'),
    path('stats/top50-clubs-by-expenditure/',views.Top50ClubsByExpenditureView.as_view(), name='top50-clubs-by-expenditure'),
    path('stats/top50-clubs-by-income/',views.Top50ClubsByIncomeView.as_view(), name='top50-clubs-by-income'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


