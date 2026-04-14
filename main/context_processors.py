from django.db.models import Count
from  .models import Country


def get_country(request):
    countries = Country.objects.annotate(
        clubs_count=Count('club')
    ).filter(clubs_count__gt=0).order_by('-clubs_count')[:16]
    countries_left=[]
    countries_right=[]
    for i, country in enumerate(countries, start=1):
        if i % 2 == 1:
            countries_left.append(country)
        else:
            countries_right.append(country)

    context={
         'cl': countries_left,
         'cr': countries_right,
     }

    return context



