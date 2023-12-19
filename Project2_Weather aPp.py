import requests
import json
import pyttsx3
engine = pyttsx3.init()
city = input("Enter the name of city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=0f0be44e9a774e0b81f93203232210&q={city}"

r=requests.get(url)
print(r.text)
print(type(r.text))      # string type
wdic = json.loads(r.text)  # for string to dictonary
print(type(wdic))
w = wdic["current"]["temp_c"]
engine.say(f"temperature in {city} is {w} degrees")
engine.runAndWait()
print(f"temperature in {city} is = ",w)

s = wdic["location"]["region"]
engine.say(f"region of {city} is {s}")
engine.runAndWait()
print(f"region of {city} is {s}")