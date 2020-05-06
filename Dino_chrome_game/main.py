import pyautogui
import time
from numpy import asarray
from PIL import Image, ImageGrab

def hit(key):
    pyautogui.keyDown(key)

def draw():
    pass

def isCollide(data):
     # Draw the rectangle for bird
    for i in range(200,250):
            for j in range(315,372):
                if data[i, j] < 100:
                    hit('down')
                    return
    # Draw the rectangle for cactus
    for i in range(200,250):
            for j in range(380,430):
               if data[i, j] < 100:
                    hit('up')
                    return
    return

if __name__ == "__main__":
    print("Hey....Dino game about to start in 3 sec")
    time.sleep(3)
    #hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        
        # #print(asarray(image))

        # Draw the rectangle for cactus
        for i in range(200,350):
            for j in range(380,480):
                data[i, j] = 0

        # Draw the rectangle for bird
        for i in range(200,350):
            for j in range(,350):
                data[i, j] = 171

        image.show()
        break

    
