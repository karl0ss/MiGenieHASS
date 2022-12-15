import requests
from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv("username")
password = os.getenv("password")

def poll_genie():  
    url = "https://public.wcs.schneider-electric.ws/rpc/public_genie/poll"
    payload = "{}"
    headers = {
    'User-Agent-Wiser': 'iPhoneTestTool;iOS6;WiserApp2.0.0',
    'Content-Type': 'application/javascript',
    }
    response = requests.request("POST", url, headers=headers, data=payload, auth=(username, password))
    return response.json()

def get_heating_data():
    data = poll_genie()
    return data['updateData']['zones'][0]

def get_water_data():
    data = poll_genie()
    return data['updateData']['zones'][1]