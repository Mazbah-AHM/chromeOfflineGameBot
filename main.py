from email.mime import image
from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *
from turtle import *
import turtle

# turtle.screensize(canvwidth=1366, canvheight=768, bg='black')

# turtle.done()

replaybtn = (961,293)
dinosaur = (670,301)
data = 0

def restartGame():
    pyautogui.click(replaybtn)
    print("I just clicked play")

def image_grab():
    box = (dinosaur[0]+60, dinosaur[1], dinosaur[0]+170, dinosaur[1]+15)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()
    # print("data",a.sum())

def pressSpace():
    time.sleep(0.1)
    pyautogui.keyDown('space')

time.sleep(4)

restartGame()
while True:
    image_grab()
    if(image_grab()!=1683):
        pressSpace()
        time.sleep(0.3)


#450 33