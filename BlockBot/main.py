from datetime import datetime


def blockbot():
    YEAR = datetime.today().year
    MONTH = datetime.today().month
    DAY = datetime.today().day
    HOUR = 17
    MINUTE = 30
    SEC = 0
    MICRO = 0
    now = datetime.today()

    limit = datetime(YEAR,MONTH,DAY,HOUR,MINUTE,SEC,MICRO)
    return now > limit

