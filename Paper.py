import os
from datetime import date
import re
import ssl
import requests
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
import json
resp = request.urlopen("https://newspaperpdf.online/download_the_hindu.php")
text = resp.read()

plaintext = text.decode('utf8')

links = re.findall(
    "href=[\"]https://drive.google.com/file/d/(.*?)/view", plaintext)

todays_paper = links[0]
todays_paper_link = "https://drive.google.com/uc?export=download&id="+todays_paper
todays_date = date.today().strftime("%d-%m-%y")
print(todays_paper_link)
todays_paper_binary = requests.get(
    todays_paper_link, allow_redirects=True, timeout=90)

paper = open(todays_date + ".pdf", 'wb')
paper.write(todays_paper_binary.content)
paper.close()
