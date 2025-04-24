from datetime import datetime
import time
import pyautogui
from build_action_time import ActionTime

# are we testing?
test_run = False
# pyautogui
x_type = 1025
y_type = 1025
text_to_write = "1337"
x_send = 1600
y_send = 1025
# delays
estimated_teams_delay = .468641
estimated_pyautogui_delay = .102343
# wake up allowance
wake_up_early_by = 2
min_sleep_duration = 3

action_time = ActionTime.build_timestamp(estimated_pyautogui_delay, estimated_teams_delay, test_run)

sleep_duration = action_time - time.time() - wake_up_early_by
if sleep_duration > min_sleep_duration:
    print("too early, going to sleep for: " + str(sleep_duration) + " secs")
    time.sleep(sleep_duration)
print("ready for action")

pyautogui.moveTo(x_type,y_type)
pyautogui.click()
pyautogui.write(text_to_write)
pyautogui.moveTo(x_send,y_send)

while(1):
    if action_time <= time.time():
        print(datetime.fromtimestamp(time.time()))
        pyautogui.click()
        print(datetime.fromtimestamp(time.time()))
        quit()
