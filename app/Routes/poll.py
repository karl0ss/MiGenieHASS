from lib import migenie

def poll_genie()->dict:
    """_summary_

    Returns:
        dict: _description_
    """    
    data = migenie.poll_genie()
    return data, 200