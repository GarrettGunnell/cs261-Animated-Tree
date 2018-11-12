from tree import BinaryTree
from rain import Rain
import time

t = BinaryTree()

def setup():
    fullScreen()
    t.set_x(width // 2)
    t.set_y(100)
    

def draw():
    background(255)
    noStroke()
    t.draw(time.time())
    
def mouseClicked():
    t.insert()
