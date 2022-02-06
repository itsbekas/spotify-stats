from time import time, strftime, process_time

time_ranges = ['short_term', 'medium_term', 'long_term']

def currentDate():
    return strftime("%a, %d %b %Y %H:%M")

def log(*args):
    timestr = strftime("%H:%M:%S")
    print('[{}]'.format(timestr), "".join(map(str, args)))
