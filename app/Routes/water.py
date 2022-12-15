from lib import migenie, utils
from flask_restful import reqparse
from time import sleep

def get_water_root()->dict:
    """_summary_

    Returns:
        dict: _description_
    """    
    data = migenie.get_water_data()
    return data, 200
    

def get_water_status()->dict:
    """_summary_

    Returns:
        dict: _description_
    """    
    data = migenie.get_water_data()['status']
    waterStatus = {
            "waterOn": utils.is_item_on(data['currentSetpoint']),
            "currentSetpoint": utils.convert_to_real_temp(data['currentSetpoint']),
            "lastTimerSetPoint": utils.convert_to_real_temp(data['lastTimerSetPoint']),
            "lastTimerDurationMinutes": data['lastTimerDurationMinutes'],
            "nextScheduleEventUtcTime": utils.format_datetime(data['nextScheduleEventUtcTime']),
            "nextEventTime":utils.format_time(data['nextScheduleEventUtcTime'])
            
    }
    
    return waterStatus, 200
    
def boost_water()->dict:
    parser = reqparse.RequestParser()  # initialize
    parser.add_argument('time',required=True)
    time = int(parser.parse_args()['time'])
    data = migenie.boost_water(time)
    sleep(2)
    if get_water_status()[0]['waterOn']:
        return data, 200  # return data with 200 OK
    else: 
        return data, 400

def turn_off_water()->dict:
    data = migenie.turn_off_water()
    sleep(2)
    if get_water_status()[0]['waterOn']:
        return data, 400  # return data with 200 OK
    else: 
        return data, 200