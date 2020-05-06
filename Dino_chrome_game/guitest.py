import pyautogui

while True:
    pyautogui.keyDown('A')
    pyautogui.keyDown('v')
    pyautogui.keyDown('i')
    pyautogui.keyDown('k')
    pyautogui.keyDown('a')


import pyautogui
import time
from numpy import asarray
from PIL import Image, ImageGrab

def hit(key):
    pyautogui.keyDown(key)

def draw():
    pass

# def isCollide(data):
#     for i in range(290,420):
#             for j in range(300,350):
#                if data[i, j] < 100:
#                    return True
#     return False

if __name__ == "__main__":
    print("Hey....Dino game about to start in 3 sec")
    time.sleep(3)
    hit('up')

    #while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit("up")
        # #print(asarray(image))
        # for i in range(290,420):
        #     for j in range(300,350):
        #         data[i, j] = 0

        # #image.show()

    
