import os
import time
import keyboard

os.system("start activate.bat")
time.sleep(0.1)
keyboard.write('set SLACK_API_TOKEN=ENTER BOT OAUTH TOKEN')
keyboard.press_and_release('enter')
keyboard.write('slackbot.py')
keyboard.press_and_release('enter')

