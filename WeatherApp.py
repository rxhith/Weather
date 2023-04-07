import requests
import json
import pyttsx3
#throgh network can ask for stuff
engine = pyttsx3.init()
city=input("enter the name of the city")
url="http://api.weatherapi.com/v1/current.json?key=5d39fdb2b2ee4957950223052230704&q="+city
r=requests.get(url)
print(r.text)
print(type(r.text))
weather_dictionary=json.loads(r.text)
print(weather_dictionary["current"]["temp_c"])
w = weather_dictionary["current"]["temp_c"]
engine.say(f"The current weather in the {city} is {w} degrees")
engine.runAndWait()
