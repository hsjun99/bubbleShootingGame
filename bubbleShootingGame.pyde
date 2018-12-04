import math

r = 40 #bubble size
A0 = 0 #Board length x
A1 = 800
B0 = 0 #Board length y
B1 = 800
v=10

class bubble:
    def __init__(self, c, x, y, vx, vy, fired):
        self.p1 = 0
        self.q1 = 0
        self.p2 = 0
        self.q2 = 0
        
        self.n1 = 0
        self.m1=0
        self.n2=0
        self.m2=0
        
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
            
            self.findAntenna(self.vx, self.vy, v, self.rcx, self.rcy)
            
            
        elif self.rcx - r/2 + self.vx < A0:
            self.vx = (-1) * self.vx
            self.rcx = A0 + r/2
            self.rcy += self.vy
            
            self.findAntenna(self.vx, self.vy, v, self.rcx, self.rcy)
            
        else:
            self.rcx += self.vx
            self.rcy += self.vy
            
            self.p1 += self.vx
            self.q1 += self.vy
            self.p2 += self.vx
            self.q2 += self.vy
            
            self.n1 += self.vx
            self.m1 += self.vy
            self.n2 += self.vx
            self.m2 += self.vy
        
    
    def display(self):
        self.update()
        fill(255, 0, 0)
        ellipse(self.rcx, self.rcy, r, r)
        if self.fired==False:
            stroke(0, 255, 0)
            line(self.p1, self.q1, self.p2, self.q2)
            line(self.n1, self.m1, self.n2, self.m2)
    
    def findAntenna(self, a, b, L, Ox, Oy):
        if a>0:
            self.p1 = Ox - r/2*abs(b)/L
            self.q1 = Oy - r/2*abs(a)/L
            self.p2 = self.p1 + r*abs(a)/L
            self.q2 = self.q1 - r*abs(b)/L
            
            self.n1 = Ox + r/2*abs(b)/L
            self.m1 = Oy + r/2*abs(a)/L
            self.n2 = self.n1 + r*abs(a)/L
            self.m2 = self.m1 - r*abs(b)/L
        else:
            self.p1 = Ox - r/2*abs(b)/L
            self.q1 = Oy + r/2*abs(a)/L
            self.p2 = self.p1 - r*abs(a)/L
            self.q2 = self.q1 - r*abs(b)/L
            
            self.n1 = Ox + r/2*abs(b)/L
            self.m1 = Oy - r/2*abs(a)/L
            self.n2 = self.n1 - r*abs(a)/L
            self.m2 = self.m1 - r*abs(b)/L
            

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
        #self.bubbleList[-1].fired = True
        self.bubbleList[-1].findAntenna(a, b, dis, (A1+A0)/2, B1-100)        
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
