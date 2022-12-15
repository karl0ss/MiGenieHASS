from lib import migenie, utils


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
            "nextScheduleEventUtcTime": utils.format_datetime(data['nextScheduleEventUtcTime'])
    }
    
    return waterStatus, 200
    