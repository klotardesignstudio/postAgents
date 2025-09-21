from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ACCOUNT_USERNAME = os.getenv('ACCOUNT_USERNAME')
ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')

def post_carrousel():
    logger = logging.getLogger()

    cl = Client()
    logger.info(f"Posting in to Instagram with username: {ACCOUNT_USERNAME} and password: {ACCOUNT_PASSWORD}")
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

    cl.delay_range = [1, 3]

    # check if session is valid
    try:
        cl.get_timeline_feed()

        media = cl.album_upload(
            [
                "/Users/zaialorenz/Documents/Klotar/projetos/ContentCraft/postAgents/images/post1-1.jpg",
                "/Users/zaialorenz/Documents/Klotar/projetos/ContentCraft/postAgents/images/post1-2.jpg",
                "/Users/zaialorenz/Documents/Klotar/projetos/ContentCraft/postAgents/images/post1-3.jpg"
            ],
            "Em breve um novo jeito de aprender sobre criptomoedas!"
        )

        logger.info(f"Media uploaded: {media}")
    except LoginRequired:
        logger.info("Session is invalid, need to login via username and password")

post_carrousel()