import sys
import pyautogui
import time

def main() :

    pyautogui.PAUSE = 0.0001
    time.sleep(2)
    list = ['a', 'b', 'c']
    for i in range(50) :
        for i in ['test', 'spam', 'bot'] :
            pyautogui.typewrite(i)
            pyautogui.press('enter')
# attendre quelques secondes (le temps que tu click sur la window steamchat)
#
main()
