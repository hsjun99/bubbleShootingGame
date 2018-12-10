import math, random

r = 30 #bubble size
A0 = 0 #Board length x
A1 = 800
B0 = 0 #Board length y
B1 = 800
v=8
colorList = [[255, 0, 0], [0, 255, 0], [0, 0, 255],[255, 255, 0], [0, 255, 255], [255, 0, 255]]

class bubble:
    def __init__(self, c, x, y, vx, vy, fired, filled):
        self.p2 = -10
        self.q2 = -10
        self.n2= -10
        self.m2= -10
        
        self.c = c
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.fired = fired #boolean value whether the bubble has been fired
        self.filled = filled
        if fired == True:
            if self.y%2==0:
                self.rcx = r/2+self.x*r
                self.rcy = r/2+self.y*r*(3**(0.5))/2
            else:
                self.rcx = r+self.x*r
                self.rcy = r/2+self.y*r*(3**(0.5))/2
        elif filled == True:
            self.rcx = (A1+A0)/2
            self.rcy = B1-100
            
    def update(self):
        if self.fired == False and self.filled==True:
            a1, b1 = B.transtoCOD(self.p2, self.q2)
            a2, b2 = B.transtoCOD(self.n2, self.m2)
            if a1 < 20 and a1 >= 0 and b1 >=0 and b1 < 20 and a2 < 20 and a2 >= 0 and b2 >=0 and b2 < 20:
                if B.bubbleList[b1][a1].filled==True or B.bubbleList[b2][a2].filled==True:
                    self.rcx = (A1+A0)/2
                    self.rcy = B1-100
                    if self.vx < 0:
                        if B.bubbleList[b1][a1].filled==True:
                            xl = self.rcx-self.p2
                            yl = (self.rcy-self.q2) * (-1)
                            if yl/xl > (3**0.5)/3:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1-1][a1].filled == False:
                                       # fill(colorList[self.c][0], colorList[self.c][1], colorList[self.c][2])
                                       # ellipse(B.bubbleList[b1-1][a1], self.rcy, r-2, r-2)
                                        B.bubbleList[b1-1][a1] = bubble(self.c, a1, b1-1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1][a1+1] = bubble(self.c, a1+1, b1, 0, 0, True, True)
                                else:
                                    if B.bubbleList[b1-1][a1+1].filled == False:
                                        B.bubbleList[b1-1][a1+1] = bubble(self.c, a1+1, b1-1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1][a1+1] = bubble(self.c, a1+1, b1, 0, 0, True, True)
                            elif yl/xl < (-1) * (3**0.5)/3:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1+1][a1].filled == False:
                                        B.bubbleList[b1+1][a1] = bubble(self.c, a1, b1+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1][a1+1] = bubble(self.c, a1+1, b1, 0, 0, True, True)
                                else:
                                    if B.bubbleList[b1+1][a1+1].filled == False:
                                        B.bubbleList[b1+1][a1+1] = bubble(self.c, a1+1, b1+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1][a1+1] = bubble(self.c, a1+1, b1, 0, 0, True, True)
                            else:
                                B.bubbleList[b1][a1+1] = bubble(self.c, a1+1, b1, 0, 0, True, True)
                                
                        else:
                            xl = self.rcx-self.n2
                            yl = (self.rcy-self.m2) * (-1)
                            if yl/xl < 0:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2+1][a2].filled == False:
                                        B.bubbleList[b2+1][a2] = bubble(self.c, a2, b2+1, 0, 0, True, True)
                                    else:
                                         B.bubbleList[b2+1][a2-1] = bubble(self.c, a2-1, b2+1, 0, 0, True, True)
                                else:
                                    if B.bubbleList[b2+1][a2+1].filled == False:
                                        B.bubbleList[b2+1][a2+1] = bubble(self.c, a2+1, b2+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b2+1][a2] = bubble(self.c, a2, b2+1, 0, 0, True, True)
                            else:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2+1][a2-1].filled == False:
                                        B.bubbleList[b2+1][a2-1] = bubble(self.c, a2-1, b2+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b2+1][a2] = bubble(self.c, a2, b2+1, 0, 0, True, True)
                                else:
                                    if  B.bubbleList[b2+1][a2].filled == False:
                                        B.bubbleList[b2+1][a2] = bubble(self.c, a2, b2+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b2+1][a2+1] = bubble(self.c, a2+1, b2+1, 0, 0, True, True)
                    
                    else:
                        if B.bubbleList[b2][a2].filled==True:
                            xl = self.rcx-self.n2
                            yl = (self.rcy-self.m2) * (-1)
                            if yl/xl > (3**0.5)/3:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2+1][a2-1].filled == False:
                                        B.bubbleList[b2+1][a2-1] = bubble(self.c, a2-1, b2+1, 0, 0, True, True)
                                    else:
                                         B.bubbleList[b2][a2-1] = bubble(self.c, a2-1, b2, 0, 0, True, True)
                                else:
                                    if B.bubbleList[b2+1][a2].filled == False:
                                        B.bubbleList[b2+1][a2] = bubble(self.c, a2, b2+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b2][a2-1] = bubble(self.c, a2-1, b2, 0, 0, True, True)
                            elif yl/xl < (-1) * (3**0.5)/3:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2-1][a2-1].filled == False:
                                        B.bubbleList[b2-1][a2-1] = bubble(self.c, a2-1, b2-1, 0, 0, True, True)
                                    else:
                                         B.bubbleList[b2][a2-1] = bubble(self.c, a2-1, b2, 0, 0, True, True)
                                else:
                                    if B.bubbleList[b2-1][a2].filled == False:
                                        B.bubbleList[b2-1][a2] = bubble(self.c, a2, b2-1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b2][a2-1] = bubble(self.c, a2-1, b2, 0, 0, True, True)
                            else:
                                B.bubbleList[b2][a2-1] = bubble(self.c, a2-1, b2, 0, 0, True, True)
                                
                        else:
                            xl = self.rcx-self.p2
                            yl = (self.rcy-self.q2) * (-1)
                            if yl/xl < 0:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1+1][a1].filled == False:
                                        B.bubbleList[b1+1][a1] = bubble(self.c, a1, b1+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1+1][a1-1] = bubble(self.c, a1-1, b1+1, 0, 0, True, True)
                                else:
                                    if B.bubbleList[b1+1][a1+1].filled == False:
                                        B.bubbleList[b1+1][a1+1] = bubble(self.c, a1+1, b1+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1+1][a1] = bubble(self.c, a1, b1+1, 0, 0, True, True)
                            else:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1+1][a1-1].filled == False:
                                        B.bubbleList[b1+1][a1-1] = bubble(self.c, a1-1, b1+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1+1][a1] = bubble(self.c, a1, b1+1, 0, 0, True, True)
                                else:
                                    if B.bubbleList[b1+1][a1].filled == False:
                                        B.bubbleList[b1+1][a1] = bubble(self.c, a1, b1+1, 0, 0, True, True)
                                    else:
                                        B.bubbleList[b1+1][a1+1] = bubble(self.c, a1+1, b1+1, 0, 0, True, True)
                    self.vx = 0
                    self.vy = 0
                    self.p2 = -10
                    self.q2 = -10
                    self.n2= -10
                    self.m2= -10
                    self.c = random.randint(0, 5)
                    
                    
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
            
            elif self.vx!=0 or self.vy!=0:
                self.rcx += self.vx
                self.rcy += self.vy
            
                self.p2 += self.vx
                self.q2 += self.vy
            
                self.n2 += self.vx
                self.m2 += self.vy
        
    
    def display(self):
        self.update()
        if self.filled == True:
            fill(colorList[self.c][0], colorList[self.c][1], colorList[self.c][2])
            ellipse(self.rcx, self.rcy, r, r)
    
    def findAntenna(self, a, b, L, Ox, Oy):
        if a>0:
            p1 = Ox - r/2*abs(b)/L
            q1 = Oy - r/2*abs(a)/L
            self.p2 = p1 + r*abs(a)/L*2.15/4
            self.q2 = q1 - r*abs(b)/L*2.15/4
            
            n1 = Ox + r/2*abs(b)/L
            m1 = Oy + r/2*abs(a)/L
            self.n2 = n1 + r*abs(a)/L*2.15/4
            self.m2 = m1 - r*abs(b)/L*2.15/4
        else:
            self.p1 = Ox - r/2*abs(b)/L
            self.q1 = Oy + r/2*abs(a)/L
            self.p2 = self.p1 - r*abs(a)/L*2.15/4
            self.q2 = self.q1 - r*abs(b)/L*2.15/4
            
            self.n1 = Ox + r/2*abs(b)/L
            self.m1 = Oy - r/2*abs(a)/L
            self.n2 = self.n1 - r*abs(a)/L*2.15/4
            self.m2 = self.m1 - r*abs(b)/L*2.15/4
            

class Game:
    def __init__(self):
        self.bubbleList = []
        for i in range(20):
            temp = []
            for j in range(20):
                if j>15 or i>=16:
                    temp.append(bubble(random.randint(0, 5), j, i, 0, 0, False, False))
                else:
                    temp.append(bubble(random.randint(0, 5), j, i, 0, 0, True, True))
                
            self.bubbleList.append(temp)
    
    def display(self):
        for items in self.bubbleList:
            for item in items:
                item.display()
            
    def transtoCOD(self, x, y):
        ry = (y - r*(1-(3**(0.5))/2))/(r*(3**(0.5))/2)
        if int(ry) %2 == 0 :
            rx1 = x//r
            rx2 = (x-r/2)//r
            dis1 = (r/2+rx1*r - x)**2 + (r/2+int(ry)*r*(3**(0.5))/2 - y)**2
            dis2 = (r+rx2*r - x)**2 + (r/2+(int(ry)+1)*r*(3**(0.5))/2 - y)**2
        else:
            rx1 = (x-r/2)//r
            rx2 = x//r
            dis1 = (r+rx1*r - x)**2 + (r/2+int(ry)*r*(3**(0.5))/2 - y)**2
            dis2 = (r/2+rx2*r - x)**2 + (r/2+(int(ry)+1)*r*(3**(0.5))/2 - y)**2
        
        if dis1 > dis2:
            rx = rx2
            ry = int(ry)+1
        else:
            rx = rx1
            ry = int(ry)
        
        return int(rx), ry
    
    def click(self):
        a = mouseX - (A1+A0)/2
        b = mouseY - (B1-100)
        dis = (a**2 + b**2)**0.5
        u.vx = v * a/dis
        u.vy = v * b/dis
        u.findAntenna(a, b, dis, (A1+A0)/2, B1-100)

B = Game()
u = bubble(random.randint(0, 5), 0, 0, 0, 0, False, True)

def setup():
    size(800, 800)
    background(0)

def draw():
    background(0)
    B.display()
    u.display()

def mouseClicked():
    B.click()
