import random

class BinaryTree():
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.color = color(167, 105, 181, 150)
        self.left = None
        self.right = None
        self.parent = None
        
    def is_leaf(self):
        return self.left is None and self.right is None
        
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        
    def draw_self(self):
        noStroke()
        fill(self.color)
        ellipse(self.x, self.y, 25, 25)
        try:
            stroke(10)
            line(self.parent.x, self.parent.y, self.x, self.y)
        except:
            pass
            
    def draw(self):
        self.draw_self()
        
        if self.left is not None:
            self.left.draw()
        if self.right is not None:
            self.right.draw()
        
    def insert(self):
        rand = random.randint(0, 100)
        
        if rand >= 50:
            if self.right is None:
                self.right = BinaryTree(self.x * 1.25, self.y + 100)
                self.right.parent = self
            else:
                self.right.insert()
        else:
            if self.left is None:
                self.left = BinaryTree(self.x * 0.75, self. y + 100)
                self.left.parent = self
            else:
                self.left.insert()
