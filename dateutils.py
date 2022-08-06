from datetime import datetime, timedelta

def get_latest_date_strings_list():
    datestringlist = []
    currentdate = datetime.now()

    for _ in range(0, 10):
        currentdate = currentdate - timedelta(days=1)
        currentdatestring = get_custom_date_string(currentdate)
        datestringlist.append(currentdatestring)
    return datestringlist

def get_custom_date_string(datestring: datetime):
    newdatestring = str(datestring).split(" ")[0].replace("-", "")[2::]
    return newdatestring