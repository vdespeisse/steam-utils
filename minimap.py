import sys
import pyautogui, time

speed = 200.0
def getSpeed(length):
    return abs(length)/speed
def main():
    def fuck():
        #f
        pyautogui.moveRel(0,-50,0.16)
        pyautogui.moveRel(30,0,0.16)
        time.sleep(0.01)
        pyautogui.mouseUp()
        pyautogui.moveRel(-30,18,0.1)
        pyautogui.mouseDown() #
        pyautogui.moveRel(15,0,0.16)

        #next letter
        pyautogui.mouseUp()
        pyautogui.moveRel(25,-18,0.1)
        pyautogui.mouseDown() #
        #u
        pyautogui.moveRel(0,40,0.16)
        pyautogui.moveRel(10,10,0.16)
        pyautogui.moveRel(5,0,0.1)
        pyautogui.moveRel(10,-10,0.16)
        pyautogui.moveRel(0,-40,0.16)
        #next letter
        time.sleep(0.05)
        pyautogui.mouseUp()
        pyautogui.moveRel(10,0,0.1)
        pyautogui.mouseDown()
        #c
        pyautogui.mouseUp()
        pyautogui.moveRel(30,0,0.1)
        pyautogui.mouseDown()
        pyautogui.moveRel(-15,0,0.16)
        pyautogui.moveRel(-5,10,0.16)
        pyautogui.moveRel(-5,10,0.16)
        pyautogui.moveRel(0,10,0.16)
        pyautogui.moveRel(5,10,0.16)
        pyautogui.moveRel(5,10,0.16)
        pyautogui.moveRel(15,0,0.16)



    pyautogui.PAUSE = 0.001
    time.sleep(3.5)
    pyautogui.keyUp("ctrl")
    pyautogui.keyDown("ctrl")
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    fuck()
    time.sleep(0.2)
    pyautogui.keyUp("ctrl")
    pyautogui.mouseUp()


# attendre quelques secondes (le temps que tu click sur la window steamchat)
#
main()
