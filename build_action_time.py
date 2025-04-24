from datetime import datetime

class ActionTime:
  def __init__(self):
    pass

  def build_timestamp(estimated_pyautogui_delay, estimated_teams_delay, test):
    # test delay
    test_delay = 7
    # get date today
    datetime_today = datetime.now()
    year = datetime_today.year
    month = datetime_today.month
    day = datetime_today.day
    # cutoff time
    cutoff_time = datetime_today.replace(hour=13, minute=37, second=0, microsecond=0)

    if test:
        hour = datetime_today.hour
        minute = datetime_today.minute
        second = datetime_today.second
        fraction_of_second = 000000
    else:
        # set target action time as 13:37:01.337
        if datetime_today > cutoff_time:
           day += day
        hour = 13
        minute = 37
        second = 1
        fraction_of_second = 337000
    # build taget action epoch
    target_action_epoch = datetime(year, month, day, hour, minute, second, fraction_of_second).timestamp()
    # adjust and retrun action timestamp
    if test:
        return target_action_epoch + test_delay
    else:
        return target_action_epoch - estimated_teams_delay - estimated_pyautogui_delay