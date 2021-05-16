import os


class Config:
    '''
    In the Config the config variables are defined
    DATABASE_URL will the the databse url in the format postgres://user:password@hostname/dbname
    DISCORD_BOT_TOKEN is the bot token
    BOT_PREFIX is the bot prefix
    '''
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
    BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
    prefix = os.environ.get('BOT_PREFIX')
