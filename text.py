import pyautogui as pg
import time
import random
message = ['hi','hello','hi']
time.sleep(10)

for i in range(20):
    a = random.choice(message)
    pg.typewrite(a)
    pg.press('enter')