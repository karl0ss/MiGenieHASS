from lib import migenie, utils

def format_temp(temp:int):
    """_summary_

    Args:
        temp (int): _description_

    Returns:
        _type_: _description_
    """    
    temp = str(temp)
    whole = temp[:-1]
    decimal = temp[-1]
    return float(f"{whole}.{decimal}")


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
            "measuredRoomTemp": format_temp(data['measuredRoomTemp']),
            "currentSetpoint": utils.convert_to_real_temp(data['currentSetpoint']),
            "lastTimerSetPoint": utils.convert_to_real_temp(data['lastTimerSetPoint']),
            "lastTimerDurationMinutes": data['lastTimerDurationMinutes'],
            "nextScheduleEventUtcTime": utils.format_datetime(data['nextScheduleEventUtcTime']),
            "nextEventTime":utils.format_time(data['nextScheduleEventUtcTime'])
        }
    
    return heatingStatus, 200
    