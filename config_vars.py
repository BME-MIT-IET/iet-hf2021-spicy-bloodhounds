import os
from dotenv import load_dotenv


class Config:
    load_dotenv()
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
    BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
    prefix = os.environ.get('BOT_PREFIX')
