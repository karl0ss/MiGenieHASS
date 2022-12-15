import datetime

def convert_to_real_temp(migenie_value:int)->float:
    """_summary_

    Args:
        migenie_value (int): _description_

    Returns:
        float: _description_
    """    
    start = [50,5]
    if migenie_value == 0:
        return 0.0
    else:
        steps = migenie_value - start[0]
        return start[1] + .5*steps
    
def is_item_on(item_name:int)->bool:
    """_summary_

    Args:
        item_name (int): _description_

    Returns:
        bool: _description_
    """
    if item_name > 0:
        return True
    else:
        return False

def format_datetime(date_time:int)->str:
    """_summary_

    Args:
        date_time (int): _description_

    Returns:
        str: _description_
    """
    return datetime.datetime.fromtimestamp(date_time).strftime('%d-%m-%Y %H:%M:%S')