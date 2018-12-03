import math

r = 40 #bubble size
A0 = 0 #Board length x
A1 = 800
B0 = 0 #Board length y
B1 = 800
v=15

class bubble:
    def __init__(self, c, x, y, vx, vy, fired):
        self.c = c
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.fired = fired #boolean value whether the bubble has been fired
        if fired == True:
            if self.y%2==0:
                self.rcx = r/2+self.x*r
                self.rcy = r/2+self.y*r*(3**(0.5))/2
            else:
                self.rcx = r+self.x*r
                self.rcy = r/2+self.y*r*(3**(0.5))/2
        else:
            self.rcx = (A1+A0)/2
            self.rcy = B1-100
            
    def update(self):
        if self.rcx + r/2 + self.vx > A1:
            self.vx = (-1) * self.vx
            self.rcx = A1 - r/2
            self.rcy += self.vy
        elif self.rcx + r/2 + self.vx < A0:
            self.vx = (-1) * self.vx
            self.rcx = A0 + r/2
            self.rcy += self.vy
        else:
            self.rcx += self.vx
            self.rcy += self.vy
    
    def display(self):
        self.update()
        fill(255, 0, 0)
        ellipse(self.rcx, self.rcy, r, r)
            

class Game:
    def __init__(self):
        self.bubbleList = []
        for i in range(15):
            for j in range(15):
                self.bubbleList.append(bubble("red", i, j, 0, 0, True))
    
    def display(self):
        for circle in self.bubbleList:
            circle.display()
    
    def click(self):
        a = mouseX - (A1+A0)/2
        b = mouseY - (B1-100)
        dis = (a**2 + b**2)**0.5
        self.bubbleList[-1].vx = v * a/dis
        self.bubbleList[-1].vy = v * b/dis
        self.bubbleList[-1].fired = True
        

B = Game()
B.bubbleList.append(bubble("red", 0, 0, 0, 0, False))

def setup():
    size(800, 800)
    background(0)

def draw():
    background(0)
    B.display()

def mouseClicked():
    B.click()
