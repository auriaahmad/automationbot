import os
import time
import subprocess
import pyautogui
import pygetwindow as gw
import pyperclip
import pydirectinput
import random
# ================================================

print("start connection with Androind")
os.system('runas /user:Auria "cmd /k scrcpy"')
time.sleep(5)

print("connection established")

active_window = gw.getActiveWindow()

# Get the title of the active window
window_title = active_window.title

# Print the window title
print(window_title)

#moving emulator window to upper left corner
active_window.moveTo(0, 0)

# ===========================================================================
# clear cache and app data section

# icon location of tiktok
pyautogui.moveTo(70, 124)
time.sleep(0.5)

# hold down the left mouse button for 2 seconds
pyautogui.mouseDown(button='left')
time.sleep(2)

# release the left mouse button
pyautogui.mouseUp(button='left')

# app info
pyautogui.moveTo(150, 197)
time.sleep(0.5)


# Click app info
pyautogui.click()
time.sleep(2)


# clear data
pyautogui.moveTo(281, 861)
time.sleep(0.5)


# Click clear data
pyautogui.click()
time.sleep(2)


# =========================================================================


#manual locate tiktok icon's co ordinates in emulator
# pyautogui.moveTo(70, 124)
# time.sleep(0.5)

# # Click the tiktok icon
# pyautogui.click()
# time.sleep(5)



# #manual locate profile button co ordinates in tiktop app
# pyautogui.moveTo(371, 872)
# time.sleep(0.5)

# # Click the profile button
# pyautogui.click()
# time.sleep(10)


# #manual locate signup button co ordinates in tiktop app
# pyautogui.moveTo(201, 490)
# time.sleep(0.5)

# # Click the signup button
# pyautogui.click()
# time.sleep(10)

# #manual locate signup2 link co ordinates in tiktop app
# pyautogui.moveTo(294, 874)
# time.sleep(0.5)

# # Click the signup2 link
# pyautogui.click()
# time.sleep(10)

# #manual locate usephone/email/username ==> 210,348 co ordinates in tiktop app
# pyautogui.moveTo(210,348)
# time.sleep(0.5)

# # Click the usephone/email/username
# pyautogui.click()
# time.sleep(10)

# #manual locate none of above ==> 139,547 co ordinates in tiktop app
# pyautogui.moveTo(139,547)
# time.sleep(0.5)

# # Click the  none of above
# pyautogui.click()
# time.sleep(2)

# #manual locate email/username ==> 282,144 co ordinates in tiktop app
# pyautogui.moveTo(282,144)
# time.sleep(0.5)

# # Click the  email/username
# pyautogui.click()
# time.sleep(10)

# name = "alexali090078601"
# # pyperclip.copy(name)

# #manual locate text field ==> 98,250 co ordinates in tiktop app
# pyautogui.moveTo(98, 250)
# time.sleep(0.5)

# # Click the  email/username
# pyautogui.click()
# pydirectinput.write(name)



# #manual locate @gmail.com ==> 79, 588 co ordinates in tiktop app
# pyautogui.moveTo(79, 588)
# time.sleep(0.5)

# # Click the  @gmail.com
# pyautogui.click()
# time.sleep(2)

# #manual locate paste ==> 38, 180 co ordinates in tiktop app
# pyautogui.moveTo(38, 180)
# time.sleep(0.5)

# # Click the  paste
# pyautogui.click()
# time.sleep(2)

# #manual locate next ==> 209, 397 co ordinates in tiktop app
# pyautogui.moveTo(209, 397)
# time.sleep(0.5)

# # Click the  next
# pyautogui.click()
# time.sleep(5)

# password = "abcd..1234"
# # pyperclip.copy(password)
# #manual locate text field ==> 98,250 co ordinates in tiktop app
# pyautogui.moveTo(98, 250)
# time.sleep(0.5)

# # # Click the  password field
# pyautogui.click()
# pydirectinput.write(password)



# #manual locate next ==> 203, 442 co ordinates in tiktop app
# pyautogui.moveTo(203, 442)
# time.sleep(0.5)

# # Click the  next
# pyautogui.click()
# time.sleep(5)

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

# #manual locate next ==> 209, 363 co ordinates in tiktop app
# pyautogui.moveTo(209, 363)
# time.sleep(0.5)

# # # Click the  next
# pyautogui.click()
# time.sleep(10)

# # #manual locate dont allow ==> 128, 579 co ordinates in tiktop app
# pyautogui.moveTo(128, 579)
# time.sleep(0.5)

# # # Click the  next
# pyautogui.click()
# time.sleep(2)

#manual locate profile button co ordinates in tiktop app
# pyautogui.moveTo(371, 872)
# time.sleep(0.5)

# # Click the profile button
# pyautogui.click()
# time.sleep(5)

# #manual locate burger button co ordinates in tiktop app
# pyautogui.moveTo(378, 93)
# time.sleep(0.5)

# # Click the burger button
# pyautogui.click()
# time.sleep(2)
# #manual locate setting and privacy co ordinates in tiktop app
# pyautogui.moveTo(138, 862)
# time.sleep(0.5)

# # Click the setting and privacy
# pyautogui.click()
# time.sleep(5)


# for i in range(2):
#     pyautogui.moveTo(138, 862)
#     pyautogui.mouseDown()
#     pyautogui.dragTo(x=325, y=1, duration=1, button='left')
#     pyautogui.mouseUp()

# #manual locate logout button co ordinates 118, 780 in tiktop app
# pyautogui.moveTo(118, 780)
# time.sleep(0.5)

# # Click the setting and privacy
# pyautogui.click()
# time.sleep(10)

# #manual locate logout button co ordinates 207, 818 in tiktop app
# pyautogui.moveTo(207, 818)
# time.sleep(0.5)

# # Click the setting and privacy
# pyautogui.click()
# time.sleep(5)

# #manual locate logout button co ordinates 120, 612 in tiktop app
# pyautogui.moveTo(120, 612)
# time.sleep(0.5)

# # Click the setting and privacy
# pyautogui.click()
# time.sleep(5)

# #manual locate logout button co ordinates 287, 556 in tiktop app
# pyautogui.moveTo(287, 556)
# time.sleep(0.5)

# # Click the setting and privacy
# pyautogui.click()
# time.sleep(5)