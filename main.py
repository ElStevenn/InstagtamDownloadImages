from instagrapi import Client
import json
from ImageDownloader import ImageDownloader
from tqdm import tqdm
import os
import pprint
import re
import random

cl = Client()
printer = pprint.PrettyPrinter()
cl.login("cachonda67_", "TusMuertos777")
cls = lambda: os.system('cls')
cls()


# Secord, transform this data to json document

def ask_for_user():
    typed_username = input("Type username: ")
    cls()
    print("Loading....")
    user_id = cl.user_id_from_username(typed_username)
    medias = cl.user_medias(user_id, 10000)

    return medias,typed_username

def create_folder(name):
    try:
        os.mkdir(f"{name}_images")
    except:
        os.rmdir(f"{name}_images")
        os.mkdir(f"{name}_images")
    finally:
        return f"{name}_images"

def extract_url(expression):
    url_pattern = r'(https?://\S+)'
    match = re.search(url_pattern, expression)
    
    if match:
        return match.group(0)
    else:
        return None

def convert_to_dic(OBJ_):
    Final = []
    for obj in OBJ_:
        insd = {
            "id": obj.id,
            "captation_text":obj.caption_text
        }
        # Check if there is a unique photo
        if obj.thumbnail_url is not None:
            unique_photo = extract_url(obj.thumbnail_url)
            insd["Photo"] = [unique_photo]  # Store the URL in a list
        # When there are multiple photos
        else:
            img_stored = []
            for img in obj.resources:
                HttpUrl = img.thumbnail_url  # Extract the image URL inside HttpUrl('')
                img_stored.append(extract_url(HttpUrl))  # Extract the URL using the extract_url function
            insd["Photo"] = img_stored  # Store the URLs of multiple photos
            
        Final.append(insd)
    return Final


def main():
    # Ask for user and create folder
    medias, username = ask_for_user()
    folder_name = create_folder(username)

    # I get the data and I convert to username
    posts = convert_to_dic(medias)

    for post in tqdm(posts):
        if len(post['Photo']) == 1:
            # Only one photo
            ImageDownloader(post['Photo'][0],post['id'],folder_name)
        else:
            # When we have more than one single photo
            for photo in post['Photo']:
                ImageDownloader(photo,random.randint(1000,10000000000),folder_name)
        
    print(f"Completed!\nA folder called {folder_name} has been created with their photos!")

if __name__ == '__main__':
    main()