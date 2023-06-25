import requests
import os
import json
# from instagrapi import CLient

path = os.getcwd()
cls = lambda: os.system('cls')

access_token = "YOUR_ACCESS_TOKEN"

url_base = "https://api.instagram.com" # To get instagram user access tokens
url_base2 = "graph.instagram.com" # To get multimedia content and user porfile

url = f"https://graph.instagram.com/me/media?fields=id,caption&access_token={access_token}"


#####################################################

data = requests.get(url)
print(data)

