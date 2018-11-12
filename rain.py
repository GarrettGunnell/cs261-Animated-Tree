import random

class Rain():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(-10, 10)
        self.speed = 2
        self.color = color(175, 200, 20)
        self.length_ = 20
        self.width_ = 1
        
        
    def reset(self):
        self.y = 0
        self.x = random.uniform(0, width)
        
    def move(self):
        self.y += self.speed
        if self.angle > 0:
            self.x += 0.2
        else:
            self.x -= 0.2
        if self.y > height:
            self.reset()
            
    def draw(self):
        pushMatrix()
        translate(self.x, self.y)
        fill(self.color)
        rotate(self.angle)
        rect(0, 0, self.width_, self.length_)
        popMatrix()
        
