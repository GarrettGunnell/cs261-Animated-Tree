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
        
    def draw(self):
        fill(self.color)
        ellipse(self.x, self.y, 50, 50)
        
    def insert(self):
        rand = random.randint(0, 100)
        
        if rand >= 50:
            if self.right is None:
                self.right = BinaryTree(self.x * 1.5, self.y + 50)
                self.right.parent = self
            else:
                self.right.insert()
        else:
            if self.left is None:
                self.left = BinaryTree(self.x // 2, self. y + 50)
                self.left.parent = self
            else:
                self.left.insert()
