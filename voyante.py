import random
import webbrowser
from geopy.geocoders import Nominatim

def is_land(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((lat, lon), language='en')
    return location and 'land' in location.raw['category']

def generate_random_coordinate():
    while True:
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        if is_land(lat, lon):
            return lat, lon

def search_news(lat, lon):
    query = f"{lat},{lon} news"
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Génère une coordonnée aléatoire sur terre
lat, lon = generate_random_coordinate()
print(f"Coordonnée trouvée : {lat}, {lon}")

# Ouvre une recherche Google pour cette coordonnée
search_news(lat, lon)
