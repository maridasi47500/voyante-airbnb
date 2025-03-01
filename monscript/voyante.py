import random
import webbrowser
from geopy.geocoders import Nominatim
import geopandas as gpd
from shapely.geometry import Point


def is_land(lat, lon, land_polygons):
    """
    Check if the coordinate is on land.
    
    :param lat: Latitude of the coordinate
    :param lon: Longitude of the coordinate
    :param land_polygons: GeoSeries of land polygons
    :return: True if the coordinate is on land, False otherwise
    """
    point = Point(lon, lat)
    return land_polygons.contains(point).any()


def generate_random_coordinate():
    # Load world land polygons from GeoPandas datasets
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    land_polygons = world[world['geometry'].type == 'Polygon'].geometry
    while True:
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        if is_land(lat, lon, land_polygons):
            return lat, lon

def search_news(lat, lon):
    query = f"{lat},{lon} news"
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
def search_news_location(lokation):
    query = f"{lokation} news"
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Génère une coordonnée aléatoire sur terre
lat, lon = generate_random_coordinate()
print(f"Coordonnée trouvée : {lat}, {lon}")
geolocator = Nominatim(user_agent="abcdefgh")
location = geolocator.reverse((lat, lon), language='fr')

# Ouvre une recherche Google pour cette coordonnée
search_news_location(location)
