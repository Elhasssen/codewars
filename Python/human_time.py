# Write a function, which takes a non-negative integer
# (seconds) as input and returns the time in a 
# human-readable format (HH:MM:SS)


def make_readable(seconds):
    if seconds == 0 :
        return '00:00:00'
    else :
        sec = seconds % 60
        minutes = seconds // 60 
        if minutes >= 60 :
            minutes = minutes % 60
        hours = seconds // 3600
        if sec <= 9  : sec = '0' + str(sec)
        if minutes <= 9  : minutes = '0' + str(minutes)
        if hours <= 9 : hours = '0' + str(hours)
        human_time = str(hours) + ':' + str(minutes) + ':' + str(sec)
        return human_time