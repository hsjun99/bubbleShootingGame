import math
r = 40

class bubble:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    def display(self):
        if self.y%2==0:
            fill(255, 0, 0)
            ellipse(r/2+self.x*r, r/2+self.y*r*(3**(0.5))/2, r, r)
        else:
            fill(255, 0, 0)
            ellipse(r+self.x*r, r/2+self.y*r*(3**(0.5))/2, r, r)
      

class Board:
    def __init__(self):
        self.bubbleList = []
        for i in range(15):
            for j in range(15):
                self.bubbleList.append(bubble("red", i, j))
    
    def display(self):
        for circle in self.bubbleList:
            circle.display()

B = Board()

def setup():
    size(800, 800)
    background(0)

def draw():
    background(0)
    B.display()
    
