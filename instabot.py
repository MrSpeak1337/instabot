import requests
from bs4 import BeautifulSoup
import time
import os
import urllib3
from instabot import Bot
import logging

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# Create a bot instance
try:
    bot = Bot()
    bot.login(username='memes.god1322', password='Wtfkkt1322')
    logger.info("Instagram Login Successful")
except Exception as e:
    logger.error("Error during Instagram login: ", e)
    exit()

url = "https://imgflip.com/i/"
count = 0

# Create a directory to save the images if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Create a urllib3 poolmanager instance
http = urllib3.PoolManager(retries=5)

with open("output.txt", "w") as f:
    while count < 100:
        try:
            # Make a GET request to the website
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            # Find the image link with the "im" ID
            image_link = soup.find("img", {"id": "im"})
            if image_link:
                image_link = image_link["src"]
            else:
                image_link = "N/A"

            img_title = soup.find("h1", {"id": "img-title"})
            if img_title:
                img_title = img_title.text
            else:
                img_title = "N/A"

            # Write the image link and title to the file
            f.write("Image Link: " + image_link + "\n")
            f.write("Image Title: " + img_title + "\n")

            # Download the image and save it to the images directory with a numerical name
            response = http.request('GET', image_link, preload_content=False)
            with open("images/{}.jpg".format(count+1), 'wb') as out:
                while True:
                    data = response.read()
                    if not data:
                        break
                    out.write(data)
            response.release_conn()

            # Try to upload the image and its title to Instagram
            try:
                bot.upload_photo("images/{}.jpg".format(count+1), caption=img_title)
                logger.info("Image and title successfully uploaded to Instagram!")
            except Exception as e:
                logger.error("Error uploading image to Instagram: ", e)
            # Wait for 20 seconds before repeating the loop
            time.sleep(20)
            count += 1

        except Exception as e:
            logger.error("Error during the process: ", e)
            exit()

