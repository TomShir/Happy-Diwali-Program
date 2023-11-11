from colorama import Fore as Fire
import sys 
import time
import random
from playsound import playsound
italic = '\033[3m'
ascii_happy_diwali='''
 _    _                           _____  _               _ _   _ 
 | |  | |                         |  __ \(_)             | (_) | |
 | |__| | __ _ _ __  _ __  _   _  | |  | |___      ____ _| |_  | |
 |  __  |/ _` | '_ \| '_ \| | | | | |  | | \ \ /\ / / _` | | | | |
 | |  | | (_| | |_) | |_) | |_| | | |__| | |\ V  V / (_| | | | |_|
 |_|  |_|\__,_| .__/| .__/ \__, | |_____/|_| \_/\_/ \__,_|_|_| (_)
              | |   | |     __/ |                                 
              |_|   |_|    |___/                                  '''
colors=[Fire.CYAN,Fire.MAGENTA,Fire.BLUE,Fire.YELLOW,Fire.WHITE,Fire.LIGHTBLUE_EX]
while True:
 for n in ascii_happy_diwali:
    sys.stdout.flush()
    time.sleep(0.0001)
    print(f'{random.choice(colors)}{n.upper()}{italic}',flush=True,end='')
 else:
     time.sleep(1)
     playsound('firework.mp3')
     sys.exit(f'{colors[0]+italic+"Happy Diwali"}\n{colors[4]}')