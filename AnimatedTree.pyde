from tree import BinaryTree
from rain import Rain
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
    backgroundImage.resize(width, height)
    Tree = loadImage("Tree2.png")
    Tree.resize(width, height)
    t.set_x(width // 2)
    t.set_y(190)
    for i in range(NUM_RAIN_DROPS):
        rain.append(Rain(random.uniform(0, width), random.uniform(0, height // 5)))
    
    

def draw():
    background(backgroundImage)
    noStroke()
    t.draw()
    for i in range(NUM_RAIN_DROPS):
        rain[i].move()
        rain[i].draw()
    image(Tree, 0, 0)
    
def mouseClicked():
    t.insert()
