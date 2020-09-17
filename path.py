import urllib
import requests
resp=urllib.request.urlopen("https://drive.google.com/drive/u/1/folders/1EVSNHUbUhhTA2Vxa8pQO69sONZPt_RO2")
print (resp.read())