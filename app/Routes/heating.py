from lib import migenie, utils
from flask_restful import reqparse
from time import sleep

def get_heating_root()->dict:
    """_summary_

    Returns:
        dict: _description_
    """    
    data = migenie.get_heating_data()
    return data, 200

def get_heating_status()->dict:
    """_summary_

    Returns:
        dict: _description_
    """    
    data = migenie.get_heating_data()['status']
    heatingStatus = {
            "heatingOn": utils.is_item_on(data['currentSetpoint']),
            "measuredRoomTemp": utils.format_temp(data['measuredRoomTemp']),
            "currentSetpoint": utils.convert_to_real_temp(data['currentSetpoint']),
            "lastTimerSetPoint": utils.convert_to_real_temp(data['lastTimerSetPoint']),
            "lastTimerDurationMinutes": data['lastTimerDurationMinutes'],
            "nextScheduleEventUtcTime": utils.format_datetime(data['nextScheduleEventUtcTime']),
            "nextEventTime":utils.format_time(data['nextScheduleEventUtcTime'])
        }
    
    return heatingStatus, 200
    
def turn_on_heating()->dict:
    parser = reqparse.RequestParser()  # initialize
    parser.add_argument('time', required=True)
    parser.add_argument('temp', required=True)
    time = int(parser.parse_args()['time'])
    temp = float(parser.parse_args()['temp'])
    data = migenie.turn_on_heating(temp, time)
    sleep(2)
    if get_heating_status()[0]['heatingOn']:
        return data, 200  # return data with 200 OK
    else: 
        return data, 400

def turn_off_heating()->dict:
    data = migenie.turn_off_heating()
    return data, 200