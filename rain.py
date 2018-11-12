import random

class Rain():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        rand = random.randint(0, 1000)
        if rand > 500:
            self.angle = 3.05
        else:
            self.angle = -3.05
        self.speed = random.uniform(20, 25)
        self.color = color(175)
        self.length_ = random.uniform(30, 50)
        self.width_ = random.uniform(0.1, 0.15)
        
        
    def reset(self):
        self.y = 0
        self.x = random.uniform(0, width)
        rand = random.randint(0, 1000)
        if rand > 500:
            self.angle = random.uniform(3.0, 3.10)
        else:
            self.angle = random.uniform(-3.1, -3.0)
        self.speed = random.uniform(20, 25)
        self.color = color(175)
        self.length_ = random.uniform(30, 50)
        self.width_ = random.uniform(0.1, 0.15)
        
    def move(self):
        self.y += self.speed
        if self.angle > 0:
            self.x += 0.2
        else:
            self.x -= 0.2
        if self.y > height:
            self.reset()
            
    def draw(self):
        noStroke()
        pushMatrix()
        translate(self.x, self.y)
        fill(self.color)
        rectMode(CENTER)
        rotate(self.angle)
        rect(0, 0, self.width_, self.length_)
        popMatrix()
        
