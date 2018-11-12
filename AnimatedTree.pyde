from tree import BinaryTree
from rain import Rain
import time
import random

t = BinaryTree()
NUM_RAIN_DROPS = 500
rain = []

def setup():
    fullScreen()
    t.set_x(width // 2)
    t.set_y(100)
    for i in range(NUM_RAIN_DROPS):
        rain.append(Rain(random.uniform(0, width), random.uniform(0, height)))
    
    

def draw():
    background(0)
    noStroke()
    t.draw(time.time())
    for i in range(NUM_RAIN_DROPS):
        rain[i].move()
        rain[i].draw()
    
def mouseClicked():
    t.insert()
