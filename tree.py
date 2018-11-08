import random

class BinaryTree():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = color(167, 105, 181, 150)
        self.left = None
        self.right = None
        self.parent = None
        
    def draw(self):
        fill(self.color)
        ellipse(self.x, self.y, 100, 100)
