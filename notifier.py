import json
from geopy.geocoders import Nominatim
from datetime import datetime
import requests

pushbullet_client = None
wanted_pokemon = None
origin_lat = 0.0
origin_lng = 0.0
# Initialize object
def init():
    global  wanted_pokemon, origin_lat, origin_lng, webhookUrl
    # load pushbullet key
    with open('config.json') as data_file:
        data = json.load(data_file)
        # get list of pokemon to send notifications for
        wanted_pokemon = _str( data["notify"] ) . split(",")
        # transform to lowercase
        wanted_pokemon = [a.lower() for a in wanted_pokemon]
        # get api key
        webhookUrl = data['slackWebhook']
        origin_lat = data["latitude"]
        origin_lng = data["longitude"]


# Safely parse incoming strings to unicode
def _str(s):
  return s.encode('utf-8').strip()

# Notify user for discovered Pokemon
def pokemon_found(pokemon):
    # get name
    pokename = _str( pokemon["name"] ).lower()
    # check array
    if not pokename in wanted_pokemon: return
    # notify
    print "[+] Notifier found pokemon:", pokename
    address = Nominatim().reverse(str(pokemon["lat"])+", "+str(pokemon["lng"])).address
    notification_text = "Pokemon Finder found a " + _str(pokemon["name"]) + "!"
    disappear_time = str(datetime.fromtimestamp(pokemon["disappear_time"]).strftime("%I:%M%p").lstrip('0'))
    location_text = "A "+ _str(pokemon["name"]) +" appeared at <https://maps.google.com/?saddr="+str(origin_lat)+","+str(origin_lng)+"&daddr="+str(pokemon["lat"])+","+str(pokemon["lng"])+"|this location>. ("+str(pokemon["distance"]) +" meters away)"+ _str(pokemon["name"]) + " will be available until " + disappear_time + "."
    thumb_url = "https://img.pokemondb.net/artwork/"+_str(pokemon["name"]).lower()+".jpg"
    slack_payload = {"attachments" : [{"thumb_url" : thumb_url, "text" : "A wild "+_str(pokemon["name"])+" appeared!", "fields" : [{"title" : "Distance", "value" : str(pokemon["distance"]) +" meters", "short":1}, {"title" : "Available until", "value" : disappear_time, "short":1},{"title" : "Location", "value" : " Click <https://maps.google.com/?saddr="+str(origin_lat)+","+str(origin_lng)+"&daddr="+str(pokemon["lat"])+","+str(pokemon["lng"])+"|here> for directions", "short":0}]}]}
    print(slack_payload);
    r = requests.post(webhookUrl, json=slack_payload);
    print(r.status_code)

init()
