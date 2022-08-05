

def make_readable(seconds: int):
    hours = (seconds - (seconds % 3600))/3600
    seconds_left = seconds - hours * 3600
    minutes = (seconds_left - (seconds_left % 60))/60
    seconds_left = seconds_left - minutes * 60
    s_hours: str = str(int(hours)).zfill(2)
    s_minutes: str = str(int(minutes)).zfill(2)
    s_seconds: str = str(int(seconds_left)).zfill(2)
    return s_hours + ':' + s_minutes + ':' + s_seconds
