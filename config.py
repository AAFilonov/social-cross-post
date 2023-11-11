import json
import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore 
 
 # Open and read the config.json file
with open('config.json', 'r') as file:
        
    config_data = json.load(file)
    print(config_data)
    # Convert config_data into global variables
    for key, value in config_data.items():
        globals()[key] = value


class Config(object):
    SECRET_KEY = os.urandom(24)
    SESSION_TYPE = 'filesystem'
    VERSION = "1.0."
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    SCHEDULER_JOBSTORES = {    
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.db')
    }
    SCHEDULER_API_ENABLED = True    