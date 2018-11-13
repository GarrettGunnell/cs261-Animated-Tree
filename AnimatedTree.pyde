from tree import BinaryTree
from rain import Rain
import time
import random

t = BinaryTree()
NUM_RAIN_DROPS = 200
rain = []
backgroundImage = None
Tree = None

def setup():
    global backgroundImage
    global Tree
    fullScreen()
    backgroundImage = loadImage("Tree.png")
    Tree = loadImage("Tree2.png")
    t.set_x(width // 2)
    t.set_y(190)
    for i in range(NUM_RAIN_DROPS):
        rain.append(Rain(random.uniform(0, width), random.uniform(0, 200)))
    
    

def draw():
    background(backgroundImage)
    noStroke()
    t.draw(time.time())
    for i in range(NUM_RAIN_DROPS):
        rain[i].move()
        rain[i].draw()
    image(Tree, 0, 0)
    
def mouseClicked():
    t.insert()
