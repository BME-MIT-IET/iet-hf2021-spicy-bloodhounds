import os
import config_vars
from yaml import load, Loader

config_path = os.path.join('config_vars.py')

class envloader:
    config = config_vars.Config()