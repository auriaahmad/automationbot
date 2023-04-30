import os
import time
import pyautogui
import pygetwindow as gw
import pydirectinput
import random
import pandas as pd
import string
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook
# ================================================

# print("start connection with Androind")
# os.system('runas /user:Auria "cmd /k scrcpy"')
# time.sleep(5)

# print("connection established")

# active_window = gw.getActiveWindow()

# # Get the title of the active window
# window_title = active_window.title

# # Print the window title
# print(window_title)

# #moving emulator window to upper left corner
# active_window.moveTo(0, 0)

# =============================
# reading names from xls file
try:
    df = pd.read_excel('names.xlsx')
    num_rows = len(df)
    print(num_rows)
    for i in range(num_rows):
        name = df.loc[i, 'names']
        # print(name)
        # print(email)
        try:
            # =============================
            # random string for password
            def random_password():
                letters = ''.join(random.choices(string.ascii_letters, k=3))
                numbers = ''.join(random.choices(string.digits, k=3))
                return f"{letters}.{numbers}.{letters}"
            password = random_password()
            email = name + "@gmail.com"
            print(email)
            print(password)
            try:
                
                print(os.path)
            except:
                print('something is wrong')
        except:
            print('somethign went wrong in password creation')


        # # ===========================
        # # navigate function
        # def navigate_to_and_click(x_co,y_co):
        #     pyautogui.moveTo(x_co, y_co)
        #     time.sleep(0.5)
        #     pyautogui.click()

        # ===========================================================================
        # # clear cache and app data section

        # # icon location of tiktok
        # pyautogui.moveTo(70, 124)
        # time.sleep(0.5)

        # # hold down the left mouse button for 2 seconds
        # pyautogui.mouseDown(button='left')
        # time.sleep(2)

        # # release the left mouse button
        # pyautogui.mouseUp(button='left')

        # # app info
        # navigate_to_and_click(150, 197)
        # time.sleep(2)


        # # clear data
        # navigate_to_and_click(281, 861)
        # time.sleep(2)


        # # clear all data
        # navigate_to_and_click(104,713)
        # time.sleep(2)


        # # delete all data
        # navigate_to_and_click(290,840)
        # time.sleep(2)

        # # home button
        # navigate_to_and_click(211,934)
        # time.sleep(2)


        # # =========================================================================


        # #open tiktok
        # navigate_to_and_click(70, 124)
        # time.sleep(8)

        # # skip interests
        # navigate_to_and_click(127,871)
        # time.sleep(2)

        # navigate_to_and_click(206,848)
        # time.sleep(3)

        # pyautogui.moveTo(200, 628)
        # pyautogui.mouseDown()
        # pyautogui.dragTo(x=200, y=90, duration=1.3, button='left')
        # pyautogui.mouseUp()

        # # ==========================================================
        # # signup process start

        # # profile button
        # navigate_to_and_click(371, 872)
        # time.sleep(2)


        # # signup button 
        # navigate_to_and_click(201, 490)
        # time.sleep(2)


        # # usephone/email/username 
        # navigate_to_and_click(210,348)
        # time.sleep(2)

        # #none of above 
        # navigate_to_and_click(139,547)
        # time.sleep(2)

        # # email/username 
        # navigate_to_and_click(282,144)
        # time.sleep(2)

        # # email text field
        # navigate_to_and_click(98, 250)
        # pyautogui.click()
        # pydirectinput.write(name)
        # time.sleep(6)

        # # # include @gmail.com 
        # navigate_to_and_click(79, 588)
        # time.sleep(2)

        # #  next 
        # navigate_to_and_click(209, 397)
        # pyautogui.click()
        # time.sleep(8)

        # # password field
        # navigate_to_and_click(98, 250)
        # pydirectinput.write(password)
        # time.sleep(6)



        # # next 
        # navigate_to_and_click(203, 442)
        # time.sleep(5)

        # # selecting random year month and day (age more than 18 yo)
        # year = random.randint(3, 8)
        # print(year)

        # for i in range(year):
        #     pyautogui.moveTo(325, 684)
        #     pyautogui.mouseDown()
        #     pyautogui.dragTo(x=325, y=1070, duration=1.5, button='left')
        #     pyautogui.mouseUp()

        # month = random.randint(1, 4)
        # print(month)

        # for i in range(month):
        #     pyautogui.moveTo(208, 684)
        #     pyautogui.mouseDown()
        #     pyautogui.dragTo(x=208, y=1070, duration=1, button='left')
        #     pyautogui.mouseUp()

        # day = random.randint(1, 6)
        # print(day)

        # for i in range(day):
        #     pyautogui.moveTo(97, 684)
        #     pyautogui.mouseDown()
        #     pyautogui.dragTo(x=97, y=1070, duration=0.5, button='left')
        #     pyautogui.mouseUp()

        # # next 
        # navigate_to_and_click(209, 363)
        # time.sleep(8)

        # # dont allow 
        # navigate_to_and_click(128, 579)
        # time.sleep(2)

        # # ==============end of registration=============

        # # ===========================
        # # log out process start
        # # ===========================

        # #profile button 
        # navigate_to_and_click(371, 872)
        # time.sleep(2)

        # # burger menu 
        # navigate_to_and_click(378, 93)
        # time.sleep(2)

        # # setting and privacy 
        # navigate_to_and_click(138, 862)
        # time.sleep(2)

        # # scroll down to log out

        # for i in range(2):
        #     pyautogui.moveTo(138, 862)
        #     pyautogui.mouseDown()
        #     pyautogui.dragTo(x=325, y=1, duration=1, button='left')
        #     pyautogui.mouseUp()

        # # logout button 
        # navigate_to_and_click(118, 780)
        # time.sleep(8)

        # # logout button confirm 
        # navigate_to_and_click(207, 818)
        # time.sleep(2)

        # # save login info not now 
        # navigate_to_and_click(120, 612)
        # time.sleep(2)

        # # logout final button 
        # navigate_to_and_click(287, 556)
        # time.sleep(8)

    
except:
    print("file name should be 'names'")
    print("file extension should be '.xlsx'")
    print("make sure it is in tiktok emulator approch folder (root folder)")

