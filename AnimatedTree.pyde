from tree import BinaryTree

t = BinaryTree()

def setup():
    fullScreen()
    t.set_x(width // 2)
    t.set_y(100)
    

def draw():
    background(255)
    noStroke()
    t.draw()
    
def mouseClicked():
    t.insert()
