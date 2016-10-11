import datetime

def is_blank(value):
    return value == None

def yes_no_999(value):
    return value == "Yes" or value =="No" or value==999

def is_date(value):
    if type(value) != datetime.datetime:
        return False
    if value.month not in range(1,13):
        return False
    if value.day not in range(1,32):
        return False
    if value.year not in range(2015,2017):
        return False
    return True

def is_time(value):
    if type(value) != datetime.time:
        return False
    if value.hour not in range(1, 25):
        return False
    if value.minute not in range(1, 60):
        return False
    return True

def valid_temp(value):
    return value > 34.7 or value < 40.8

def valid_pulse(value):
    return value > 50 or value < 200

def valid_resp(value):
    return value > 10 or value < 45

def valid_systolic(value):
    return value > 60 or value < 240

def valid_oxygen(value):
    return value > 70 or value < 100

def yes_no(value):
    return value == "Yes" or value == "No"

def yes_no_unknown(value):
    return value == "Yes" or value == "No" or value == "Unknown"

def valid_ph(value):
    return value > 4 or value < 10

def valid_bun(value):
    return value > 3 or value < 30 or value == 999

def valid_sodium(value):
    return value > 120 or value < 147 or value == 999

def valid_glucose(value):
    return value >50 or value < 600 or value == 999

def valid_hematocrit(value):
    return value > 15 or value < 70

def valid_result(value):
    return value == "Negative" or value == "Positive"

