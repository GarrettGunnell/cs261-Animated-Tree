from tree import BinaryTree
from rain import Rain
import time

t = BinaryTree()
r = Rain(100, 0)

def setup():
    fullScreen()
    t.set_x(width // 2)
    t.set_y(100)
    

def draw():
    background(255)
    noStroke()
    t.draw(time.time())
    r.move()
    r.draw()
    
def mouseClicked():
    t.insert()
