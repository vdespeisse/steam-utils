import sys
import pyautogui, time

def main():
    pyautogui.PAUSE = 0.05
    time.sleep(2)
    pyautogui.keyDown("alt")
    for i in range(200):
        pyautogui.click()

    pyautogui.keyUp("alt")

# attendre quelques secondes (le temps que tu click sur la window steamchat)
#
main()
