import requests

from myapp.models import BikeStation


def get_bikerio_data(request):
    url = 'https://api.citybik.es/v2/networks/bikerio'
    response = requests.get(url)
    data = response.json()

    for station_data in data['network']['stations']:
        station = BikeStation(
            name=station_data['name'],
            latitude=station_data['latitude'],
            longitude=station_data['longitude'],
            capacity=station_data['empty_slots'] + station_data['free_bikes']
        )
        station.save()
