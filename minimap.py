import sys
import pyautogui, time

def main():
    pyautogui.PAUSE = 0.001
    time.sleep(4)
    pyautogui.keyDown("ctrl")
    pyautogui.dragRel(200, 0, 1, button='left')

    pyautogui.keyUp("ctrl")

# attendre quelques secondes (le temps que tu click sur la window steamchat)
#
main()
