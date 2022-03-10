from PyLyrics import *
import speech_recognition as sr
from tkinter import *
import json
import datetime


r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

a=r.recognize_google(audio, language="en-us")+"."
a=a.lower()
a=a.replace("play ","")
a=a.replace(" by ","$")
start_artist = a.find('$') + 1
artist_end= a.find('.')
artist=a[start_artist:artist_end]
song=a[:start_artist-1]
datenow = datetime.datetime.now().strftime("%X").replace(":","_")
datenow =datenow +(chr(int("10"+datenow[3])))+".json"
f = open(datenow, "x")
datasong={
  song: artist
}
HEADERS={ "X-AYYPI-KEY": "7NWtD5WrYyb1sRqGVDKmFpMxhALEFk9oyy4e"}

apidata = json.dumps(datasong, indent = 1)
headersdata = json.dumps(HEADERS, indent = 1)

with open(datenow, "w") as outfile:
    outfile.write(apidata)
with open("Api.json", "w") as outfile:   
    outfile.write(headersdata)
with open("lyrics of "+song+" by "+artist+".txt", "w") as outfile:    
    outfile.write(PyLyrics.getLyrics(artist,song))




