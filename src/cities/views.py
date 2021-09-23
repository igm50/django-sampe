from django.http import HttpResponse
from .models import City


def index(request):
    sample = City.objects.filter(id=5)[0]
    return HttpResponse('id: 5'
                        + ', name: ' + sample.name
                        + ', country: ' + sample.countrycode.name
                        + ', district: ' + sample.district
                        + ', population: ' + str(sample.population))
