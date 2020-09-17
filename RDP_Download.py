import os
from datetime import date
import re
import ssl
import requests
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
import json

rdp_link = "https://drive.google.com/uc?export=download&id=1QUDh2VoLFzg7O9U1XmjhAlMjILtX9rNM"

rdp_binary = requests.get(
    rdp_link, allow_redirects=True, timeout=90)

paper = open( "ayush.rdp", 'wb')
paper.write(rdp_binary.content)
paper.close()
