import pyautogui

# move cursor to top left corner to cancel execution

width, height = pyautogui.size()
print(width, height)

print(pyautogui.position())
pyautogui.moveTo(10, 10)
pyautogui.moveTo(1000, 1000, duration = 3)
pyautogui.moveRel(10, -1000, duration = 1)  # relative to current position
pyautogui.click(375, 18)  # click at coords
# pyautogui.doubleClick(375, 18)
# pyautogui.middleClick(375, 18)
# pyautogui.drag() # draw a line
# pyautogui.dragRel()
# pyautogui.typewrite("Hello World", interval=0.2)
pyautogui.click()
pyautogui.typewrite(['F1'])
# print(pyautogui.KEYBOARD_KEYS)
pyautogui.typewrite(['backspace', 'l', 'i', 's', 't', 's', 'home', 'N', 'e',
                    's', 't', 'e', 'd', 'space', 'enter'], interval=0.2)
# pyautogui.screenshot('screenie.jpg')  # pillow object
pyautogui.click(1920, 1070)
print(pyautogui.locateOnScreen('screenie_bin.jpg', grayscale=False, confidence=.9))  # find something and return its XY coords, requires module opencv-python
bin_x, bin_y = pyautogui.locateCenterOnScreen('screenie_bin.jpg', grayscale=False, confidence=.9)
pyautogui.doubleClick(bin_x, bin_y)
