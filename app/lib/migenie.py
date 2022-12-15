import requests
from requests_cache import CachedSession
from dotenv import load_dotenv
import os
from lib.utils import convert_to_real_temp, is_valid_time

load_dotenv()
username = os.getenv("username")
password = os.getenv("password")

root_url = "https://public.wcs.schneider-electric.ws/rpc/public_genie/"

def poll_genie():  
    url = root_url+"poll"
    payload = "{}"
    headers = {
    'User-Agent-Wiser': 'iPhoneTestTool;iOS6;WiserApp2.0.0',
    'Content-Type': 'application/javascript',
    }
    response = requests.request("POST", url, headers=headers, data=payload, auth=(username, password))
    return response.json()

def poll_genie_proxy():  
    session = CachedSession('poll_cache', backend='sqlite',expire_after=30)
    url = 'http://127.0.0.1:5000/poll_genie'
    response = session.get(url)
    print("MiGenie Session Token = " + str(response.json()['sessionToken']))
    return response.json()

def get_heating_data():
    data = poll_genie_proxy()
    return data['updateData']['zones'][0]

def get_water_data():
    data = poll_genie_proxy()
    return data['updateData']['zones'][1]

def boost_water(time:int):
    if is_valid_time(time):
        url = root_url+"apply_timer"

        payload = '{"zoneId": [1],"setPoint": 255,"durationMinutes": ' + str(time) + '}'
        headers = {
        'User-Agent-Wiser': 'iPhoneTestTool;iOS6;WiserApp2.0.0',
        'Content-Type': 'application/javascript'
        }
        response = requests.request("POST", url, headers=headers, data=payload, auth=(username, password))
        return response.json()
    else:
        return {"Error":"Time must be multiples of 30"}

def turn_off_water():
    url = root_url+"cancel_timer"

    payload = '{"zoneId": [1]}'
    headers = {
    'User-Agent-Wiser': 'iPhoneTestTool;iOS6;WiserApp2.0.0',
    'Content-Type': 'application/javascript'
    }
    response = requests.request("POST", url, headers=headers, data=payload, auth=(username, password))
    return response.json()

def turn_on_heating(temp:int, time):
    temp = str(convert_to_real_temp(temp, True))
    if is_valid_time(time):
        url = root_url+"adjust_setpoint"
        payload = '{"zoneId": [0],"setpoint": ' +temp+',"durationMinutes": '+ str(time) + '}'
        headers = {
        'User-Agent-Wiser': 'iPhoneTestTool;iOS6;WiserApp2.0.0',
        'Content-Type': 'application/javascript'
        }
        response = requests.request("POST", url, headers=headers, data=payload, auth=(username, password))
        return response.json()
    else:
        return {"Error":"Time must be multiples of 30"}    
    
    
def turn_off_heating():
    url = root_url+"adjust_setpoint"
    payload = '{"zoneId": [0],"setpoint": 0}'
    headers = {
    'User-Agent-Wiser': 'iPhoneTestTool;iOS6;WiserApp2.0.0',
    'Content-Type': 'application/javascript'
    }
    response = requests.request("POST", url, headers=headers, data=payload, auth=(username, password))
    return response.json()