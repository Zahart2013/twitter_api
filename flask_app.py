from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import json
import folium
from flask import Flask, render_template, request
from json_parse import json_downloader as downloader


app = Flask(__name__)

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


@app.route("/")
def username():
    return render_template("username.html")


@app.route("/register", methods=["POST"])
def register():
    mapa_build(request.form.get("user"))
    return render_template("Map_Friends.html")


def mapa_build(user):
    """
    Builds html file with map
    """
    downloader.downloader(user, TWITTER_URL)
    mapa = folium.Map(tiles="Mapbox Bright", zoom_start=8)
    mapa.add_child(friend_locations(generate_data()))
    mapa.save("templates\\Map_Friends.html")


def friend_locations(data):
    fg = folium.FeatureGroup(name="Friend location")
    for each in data:
        try:
            fg.add_child(
                (folium.Marker(location=generate_coordinates(each[1]),
                               popup=each[0],
                               icon=folium.Icon())))
        except:
            continue
    return fg


def generate_data():
    data = []
    with open("data.json", "r") as file:
        json_dic = json.load(file)
    for each in json_dic["users"]:
        try:
            data.append((each["name"], each["location"]))
        except:
            continue
    return data


def generate_coordinates(location):
    """
    (str) -> list
    Gets location name and returns list with coordinates
    """
    geolocator = Nominatim(user_agent="twitter")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1.0)
    coordinate = geolocator.geocode(location)
    return [coordinate.latitude, coordinate.longitude]
