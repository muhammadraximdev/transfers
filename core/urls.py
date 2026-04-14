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
    path('u20/',views.u20_players_view, name='u20'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


