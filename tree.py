import random
import math

class BinaryTree():
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.indentation = 450
        self.color = color(167, 105, 181, 150)
        self.left = None
        self.right = None
        self.parent = None
        
    def is_leaf(self):
        return self.left is None and self.right is None
    
    def has_parent(self):
        return self.parent is not None
    
    def is_left_child(self):
        return self.parent.left is self
    
    def is_right_child(self):
        return self.parent.right is self
        
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        
    def draw_self(self, time):
        noStroke()
        fill(self.color)
        ellipse(self.x, self.y, 26, 26)
        if self.has_parent():
            self.grow()
            stroke(167, 105, 181, 150)
            if self.is_left_child():
                line(self.parent.x, self.parent.y, self.x, self.y)
            elif self.is_right_child():
                line(self.parent.x, self.parent.y, self.x, self.y)
            
    def draw(self, time):
        self.draw_self(time)
        
        if self.left is not None:
            self.left.draw(time)
        if self.right is not None:
            self.right.draw(time)
        
    def insert(self):
        rand = random.randint(0, 100)
        
        if rand >= 50:
            if self.right is None:
                self.right = BinaryTree(self.x, self.y)
                self.right.indentation = self.indentation * 0.5
                self.right.parent = self
            else:
                self.right.insert()
        else:
            if self.left is None:
                self.left = BinaryTree(self.x, self.y)
                self.left.indentation = self.indentation * 0.5
                self.left.parent = self
            else:
                self.left.insert()
                
    def grow(self):
        if self.y < self.parent.y + 160:
            self.y += 1
        if self.is_left_child() and self.x > (self.parent.x - self.parent.indentation):
            self.x -= 1
        if self.is_right_child() and self.x < (self.parent.x + self.parent.indentation):
            self.x += 1
