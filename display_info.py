import cv2
import numpy as np
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

"""
Planet class to make things easier to handle.

"""
class Planet(object):
    name = ""
    distanceFromSun = 0 #in lightyears
    size = 0 # multiplier only. x times of earth's
    gravity = 0 # multiplier only. x times of earth's
    moons = [] # only the names
    elementsFound = []
    orbitTime = 0 # in days (earth)
    dayTime = 0 # in days (earth)

    def __init__(self, name, distanceFromSun, size, gravity, moons, elementsFound, orbitTime, dayTime):
        self.name = name
        self.distanceFromSun = distanceFromSun
        self.size = size
        self.gravity = gravity
        self.moons = moons
        self.elementsFound = elementsFound
        self.orbitTime = orbitTime
        self.dayTime = dayTime

def click_and_display(event, x, y, flags, param):
    # grab references to the global variables
    global img

    # if the left mouse button was clicked, record the starting
    if event == cv2.EVENT_LBUTTONUP:
        # print(x,y)
        # draw a circle on where we clicked
        cv2.circle(img, (x,y), 3, (0,0,255), thickness=-1, lineType=8) # color BGR

        # display info
        info = prepare_info()

        # get the font
        fontsize = 10
        font = ImageFont.truetype("spacefont.ttf", fontsize)

        # load the image to PIL format
        img_pil = Image.fromarray(img)

        # draw the font
        draw = ImageDraw.Draw(img_pil)
        clickingOffset = 50 # how far should the information be displayed (in pixels)
        draw.text((x + clickingOffset, y), info, font=font, fill=(0,0,255,0)) # color BGR

        # back to opencv format
        img = np.array(img_pil)

        # add a line to the info
        textOffset = 90 # enough long to cover the text body on X axis
        cv2.line(img, (x, y), (x+clickingOffset + textOffset, y), (0, 0, 255), 1)

        # display it
        cv2.imshow("image", img)

def prepare_info():
    # Create a planet
    planet = Planet("Mercury", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)

    #TODO: How to do know which planet is clicked? We need to find a solution here below.
    """if(mercury):
        planet = Planet("Mercury", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif(venus):
        planet = Planet("Venus", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif(earth):
        planet = Planet("Earth", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif(mars):
        planet = Planet("Mars", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif(jupiter):
        planet = Planet("Jupiter", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif(saturn):
        planet = Planet("Saturn", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif(uranus):
        planet = Planet("Uranus", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif (neptune):
        planet = Planet("Neptune", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    elif (pluto):
        planet = Planet("Pluto", 1000000, 0.5, 0.1, ['Moon A', 'Moon B'], ['Hydrogen, Nitrogen'], 8, 0.15)
    else:
        planet = Planet("Sun", 0, 0.5, 0.1, ['None'], ['Hydrogen, Helium'], 8, 0.15)
    """

    info = "-Planet Info" \
           "\n--Name: " + planet.name +\
           "\n--Distance from the Sun: " + str(planet.distanceFromSun) + " lightyears" +\
           "\n--Size: x" + str(planet.size) + " of Earth" +\
           "\n--Gravity: x" +str(planet.gravity) + " of Earth" +\
           "\n--Moons: " + str(planet.moons) +\
           "\n--Elements Found: " + str(planet.elementsFound) +\
           "\n--Orbit Time: " + str(planet.orbitTime) + " Earth days" +\
           "\n--Day Time: " + str(planet.dayTime) + " Earth days"

    # print(info)
    return info

if __name__ == "__main__":
    img = cv2.imread('solar_system.jpg',1)
    clone = img.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_display)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", img)
        key = cv2.waitKey(1) & 0xFF

        # if the 'c' key is pressed, break from the loop
        if key == ord("c"):
            break

    # close all open windows
    cv2.destroyAllWindows()