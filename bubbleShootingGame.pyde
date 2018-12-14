add_library('minim')
import math, random, time
import os
path = os.getcwd()
player = Minim(this)

r = 30 #bubble size
A0 = 2*r #Board length x
A1 = 525
B0 = 0 #Board length y
B1 = 750
v = 9
colorList = [[255, 128, 128], [128, 230, 128], [128, 128, 255],[255, 215, 50], [64, 224, 208], [255, 128, 255]]
dxy0 = [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]
dxy1 = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]

startBackground = loadImage(path + '/wallpaper.jpg')
gameOver = loadImage(path+'/gameover.png')
winImage = loadImage(path+'/winImage.jpg')
popMusic = player.loadFile(path+"/burstingSound.mp3")
backMusic = player.loadFile(path+"/backGroundMusic.mp3")

class bubble:
    def __init__(self, c, x, y, vx, vy, fired, filled):
        self.p2 = -10
        self.q2 = -10
        self.n2= -10
        self.m2= -10
        
        self.cache = []
        self.cntBalls = []
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
    
    def popBubble(self, b, a):
        global turn
        B.bubbleList[b][a] = bubble(self.c, a, b, 0, 0, True, True)
        B.countBubble += 1
        self.cache=[]
        self.cntBalls = []
        self.spread(b, a, self.c, 0)
        turn+=1
        if len(self.cntBalls) >= 2:
            popMusic.rewind()
            popMusic.play()
            B.bubbleList[b][a] = bubble(self.c, a, b, 0, 0, False, False)
            B.countBubble -= 1
            B.score+=100
            background(245, 245, 245)
            B.display()
            for k in self.cntBalls:
                background(245, 245, 245)
                B.bubbleList[k[0]][k[1]] = bubble(random.randint(0, 5), k[1], k[0], 0, 0, False, False)
                B.countBubble -= 1
                B.score+=100
                B.display()
            
            B.checkList = []
            for i in range(24, 1, -1):
                for j in range(20):
                    B.dropList = []
                    B.top = 25
                    if not (j<2 or j>16):
                        B.drop(i, j)
                    if B.top!=2:
                        for k in B.dropList:
                            background(245, 245, 245)
                            B.bubbleList[k[0]][k[1]] = bubble(random.randint(0, 5), k[1], k[0], 0, 0, False, False)
                            B.countBubble -= 1
                            B.score+=100
                            B.display()
        self.cntBalls = []
    
    def spread(self, b, a, ballColor, level):
        self.cache.append([b, a])
        if a<0 or b<0 or a>25 or b>25:
            return
        if B.bubbleList[b][a].filled == False:
            return
        if B.bubbleList[b][a].c != ballColor:
            return
        if level!=0 and B.bubbleList[b][a].c == ballColor:
            self.cntBalls.append([b, a])
        if b%2==0:
            for d in dxy0:
                if [b+d[0], a+d[1]] in self.cache:
                    continue
                self.spread(b+d[0], a+d[1], ballColor, level+1)
        else:
            for d in dxy1:
                if [b+d[0], a+d[1]] in self.cache:
                    continue
                self.spread(b+d[0], a+d[1], ballColor, level+1)
            
    def update(self):
        if self.fired == False and self.filled==True:
            a1, b1 = B.transtoCOD(self.p2, self.q2)
            a2, b2 = B.transtoCOD(self.n2, self.m2)
            if a1 < 40 and a1 >= 0 and b1 >=0 and b1 < 25 and a2 < 40 and a2 >= 0 and b2 >=0 and b2 < 25:
                if B.bubbleList[b1][a1].filled==True or B.bubbleList[b2][a2].filled==True:
                    if self.vx < 0:
                        if B.bubbleList[b1][a1].filled==True:
                            xl = self.rcx-self.p2
                            yl = (self.rcy-self.q2) * (-1)
                            if yl/xl > (3**0.5)/3:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1-1][a1].filled == False:
                                        self.popBubble(b1-1, a1)
                                    else:
                                        if a1+1>16:
                                            self.popBubble(b1+1, a1)
                                        else:
                                            self.popBubble(b1, a1+1)
                                else:
                                    if B.bubbleList[b1-1][a1+1].filled == False:
                                        self.popBubble(b1-1, a1+1)
                                    else:
                                        if a1+1>16:
                                            self.popBubble(b1+1, a1+1)
                                        else:
                                            self.popBubble(b1, a1+1)
                            elif yl/xl < (-1) * (3**0.5)/3:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1+1][a1].filled == False:
                                        self.popBubble(b1+1, a1)
                                    else:
                                        if a1+1>16:
                                            self.popBubble(b1+1, a1)
                                        else:
                                            self.popBubble(b1, a1+1)
                                else:
                                    if B.bubbleList[b1+1][a1+1].filled == False:
                                        if a1+1>16:
                                            self.popBubble(b1+1, a1)
                                        else:
                                            self.popBubble(b1+1, a1+1)
                                    else:
                                        if a1+1>16:
                                            self.popBubble(b1+1, a1+1)
                                        else:
                                            self.popBubble(b1, a1+1)
                            else:
                                if a1+1>16:
                                    self.popBubble(b1, a1)
                                else:
                                    self.popBubble(b1, a1+1)
                                
                        else:
                            xl = self.rcx-self.n2
                            yl = (self.rcy-self.m2) * (-1)
                            if yl/xl < 0:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2+1][a2].filled == False:
                                        self.popBubble(b2+1, a2)
                                    else:
                                        if a2-1<2:
                                            self.popBubble(b2+1, a2)
                                        else:
                                            self.popBubble(b2+1, a2-1)
                                else:
                                    if B.bubbleList[b2+1][a2+1].filled == False:
                                        if a2+1>16:
                                            self.popBubble(b2+1, a2)
                                        else:
                                            self.popBubble(b2+1, a2+1)
                                    else:
                                        self.popBubble(b2+1, a2)
                            else:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2+1][a2-1].filled == False:
                                        if a2-1<2:
                                            self.popBubble(b2+1, a2)
                                        else:
                                            self.popBubble(b2+1, a2-1)
                                    else:
                                        self.popBubble(b2+1, a2)
                                else:
                                    if  B.bubbleList[b2+1][a2].filled == False:
                                        self.popBubble(b2+1, a2)
                                    else:
                                        if a2+1>16:
                                            self.popBubble(b2+1, a2+1)
                                        else:
                                            self.popBubble(b2+1, a2+1)
                    else:
                        if B.bubbleList[b2][a2].filled==True:
                            xl = self.rcx-self.n2
                            yl = (self.rcy-self.m2) * (-1)
                            if yl/xl > (3**0.5)/3:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2+1][a2-1].filled == False:
                                        if a2-1<2:
                                            self.popBubble(b2+1, a2)
                                        else:
                                            self.popBubble(b2+1, a2-1)
                                    else:
                                        if a2-1<2:
                                            self.popBubble(b2, a2)
                                        else:
                                            self.popBubble(b2, a2-1)
                                else:
                                    if B.bubbleList[b2+1][a2].filled == False:
                                        self.popBubble(b2+1, a2)
                                    else:
                                        if a2-1<2:
                                            self.popBubble(b2, a2)
                                        else:
                                            self.popBubble(b2, a2-1)
                            elif yl/xl < (-1) * (3**0.5)/3:
                                if B.bubbleList[b2][a2].y%2==0:
                                    if B.bubbleList[b2-1][a2-1].filled == False:
                                        if a2-1<2:
                                            self.popBubble(b2-1, a2)
                                        else:
                                            self.popBubble(b2-1, a2-1)
                                    else:
                                        if a2-1<2:
                                            self.popBubble(b2, a2)
                                        else:
                                            self.popBubble(b2, a2-1)
                                else:
                                    if B.bubbleList[b2-1][a2].filled == False:
                                        self.popBubble(b2-1, a2)
                                    else:
                                        if a2-1<2:
                                            self.popBubble(b2, a2)
                                        else:
                                            self.popBubble(b2, a2-1)
                            else:
                                if a2-1<2:
                                    self.popBubble(b2, a2)
                                else:
                                    self.popBubble(b2, a2-1)
                        else:
                            xl = self.rcx-self.p2
                            yl = (self.rcy-self.q2) * (-1)
                            if yl/xl < 0:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1+1][a1].filled == False:
                                        self.popBubble(b1+1, a1)
                                    else:
                                        if a1-1<2:
                                            self.popBubble(b1+1, a1)
                                        else:
                                            self.popBubble(b1+1, a1-1)
                                else:
                                    if B.bubbleList[b1+1][a1+1].filled == False:
                                        if a1+1>16:
                                            self.popBubble(b1+1, a1)
                                        else:
                                            self.popBubble(b1+1, a1+1)
                                    else:
                                        self.popBubble(b1+1, a1)
                            else:
                                if B.bubbleList[b1][a1].y%2==0:
                                    if B.bubbleList[b1+1][a1-1].filled == False:
                                        if a1-1<2:
                                            self.popBubble(b1+1, a1)
                                        else:
                                            self.popBubble(b1+1, a1-1)
                                    else:
                                        self.popBubble(b1+1, a1)
                                else:
                                    if B.bubbleList[b1+1][a1].filled == False:
                                        self.popBubble(b1+1, a1)
                                    else:
                                        if a1+1>16:
                                            self.popBubble(b1+1, a1)
                                        else:
                                            self.popBubble(b1+1, a1+1)
                    self.vx = 0
                    self.vy = 0
                    self.p2 = -10
                    self.q2 = -10
                    self.n2= -10
                    self.m2= -10
                    self.c = random.randint(0, 5)
                    self.rcx = (A1+A0)/2
                    self.rcy = B1-100
                  
                elif b1==2 or b2==2:
                    if self.vx>0:
                        a1, b1 = B.transtoCOD(self.p2, self.q2)
                        B.bubbleList[2][a1] = bubble(self.c, a1, 2, 0, 0, True, True)
                    else:
                        a2, b2 = B.transtoCOD(self.n2, self.m2)
                        B.bubbleList[2][a2] = bubble(self.c, a2, 2, 0, 0, True, True)
                    self.vx = 0
                    self.vy = 0
                    self.p2 = -10
                    self.q2 = -10
                    self.n2= -10
                    self.m2= -10
                    self.c = random.randint(0, 5)
                    self.rcx = (A1+A0)/2
                    self.rcy = B1-100
            
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
            noStroke()
            ellipse(self.rcx, self.rcy, r-1, r-1)
    
    def findAntenna(self, a, b, L, Ox, Oy):
        if a>0:
            p1 = Ox - r/2*abs(b)/L/2
            q1 = Oy - r/2*abs(a)/L/2
            self.p2 = p1 + r*abs(a)/L*3/4
            self.q2 = q1 - r*abs(b)/L*3/4
            
            n1 = Ox + r/2*abs(b)/L/2
            m1 = Oy + r/2*abs(a)/L/2
            self.n2 = n1 + r*abs(a)/L*3/4
            self.m2 = m1 - r*abs(b)/L*3/4
        else:
            self.p1 = Ox - r/2*abs(b)/L/2
            self.q1 = Oy + r/2*abs(a)/L/2
            self.p2 = self.p1 - r*abs(a)/L*3/4
            self.q2 = self.q1 - r*abs(b)/L*3/4
            
            self.n1 = Ox + r/2*abs(b)/L/2
            self.m1 = Oy - r/2*abs(a)/L/2
            self.n2 = self.n1 - r*abs(a)/L*3/4
            self.m2 = self.m1 - r*abs(b)/L*3/4

class Game:
    def __init__(self):
        self.status = "Menu"
        self.score = 0
        self.bubbleList = []
        self.gameEnd = False
        self.countBubble = 0
        self.dropList = []
        self.checkList = []
        self.top = 25
        
        for i in range(27):
            temp = []
            for j in range(20):
                if j<2 or j>16 or i>=11 or i<2:
                    temp.append(bubble(random.randint(0, 5), j, i, 0, 0, False, False))
                else:
                    temp.append(bubble(random.randint(0, 5), j, i, 0, 0, True, True))
                    self.countBubble+=1
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
    
    def addlines(self):
        for i in range(23, 1, -1):
            for j in range(25):
                if not (j<2 or j>16):
                    if self.bubbleList[i][j].filled == False:
                        continue
                    if i==20:
                        check = True
                    self.bubbleList[i+2][j] = bubble(self.bubbleList[i][j].c, j, i+2, 0, 0, True, True)
        for i in range(2, 4):
            temp = []
            for j in range(18):
                if j<2 or j>16 or i>=16 or i<2:
                    self.bubbleList[i][j] = bubble(random.randint(0, 5), j, i, 0, 0, False, False)
                else:
                    B.countBubble+=1
                    self.bubbleList[i][j] = bubble(random.randint(0, 5), j, i, 0, 0, True, True)
                    
    def drop(self, i, j):
        if i<2 or j<2 or j>16 or i>24:
            return
        if self.bubbleList[i][j].filled == False:
            return
        if [i, j] in self.checkList:
            return
        self.dropList.append([i, j])
        self.checkList.append([i, j])
        if self.top > i:
            self.top = i
        if i%2 == 0:
            for t in range(6):
                self.drop(i+dxy0[t][0], j+dxy0[t][1])
        else:
            for t in range(6):
                self.drop(i+dxy1[t][0], j+dxy1[t][1])
            
        

B = Game()
backMusic.play()
u = bubble(random.randint(0, 5), 0, 0, 0, 0, False, True)

turn = 0
Started = False

def setup():
    size(575, 750)
    background(0)

def draw():
    global turn, B
    if B.gameEnd == True:
        background(245, 245, 245)
        noFill()
        strokeWeight(4)
        stroke(255, 255, 255)
        rect(2*r-1, r*(3**(0.5))/2*2-1, 700-8*r+5, 650, 10)
        strokeWeight(2)
        stroke(200, 0, 0)
        line(2*r, r+r*(3**(0.5))/2*22, 700-6*r, r+r*(3**(0.5))/2*22)
        B.display()
        image(gameOver, (575-388)/2, 100)
        
    elif B.status == "Play":
        background(245, 245, 245)
        noFill()
        strokeWeight(4)
        stroke(255, 255, 255)
        rect(2*r-1, r*(3**(0.5))/2*2-1, 700-8*r+5, 650, 10)
        strokeWeight(2)
        stroke(200, 0, 0)
        line(2*r, r+r*(3**(0.5))/2*22, 700-6*r, r+r*(3**(0.5))/2*22)
        B.display()
        u.display()
        if turn >= 40:
            B.addlines()
            turn = 0
        for j in range(3, 16):
            if B.bubbleList[23][j].filled == True:
                B.gameEnd = True
        if B.countBubble == 0:
            image(winImage, -10, 60)
        
    elif B.status == "Menu":
        image(startBackground, 0, -300, 575, 840*575/450)
        textSize(24)
        if 575//2.5-30 < mouseX < 575//2.5 + 160 and 750//3 < mouseY < 750//3+50:
            fill(255,0,0)
        else:
            fill(255)
        text("Play Game", 575//2.5+8, 750//3+40)
        textSize(24)
        if 575//2.5-30 < mouseX < 575//2.5 + 160 and 750//2-60 < mouseY < 750//2-10:
            fill(255,0,0)
        else:
            fill(255)
        text("Instruction", 575//2.5+8, 750//2-20)
    
    elif B.status == "Instruction":
        image(startBackground, 0, -300, 575, 840*575/450)
        textSize(15)
        fill(255)
        text("The objective of this game is to clear the field by forming\ngroups of three or more like-colored bubbles. The player\ncan shoot the bubble at the bottom of the wall of bubbles\nby simply clicking its direction on the field. The game ends\nwhen the bubbles reach the bottom red line of the screen,\nor when there are no bubbles remaining on the playing field.", 70, 750//3+40)
        
def mouseClicked():
    if B.status == "Play":
        B.click()
    elif B.status == "Menu":
        if 575//2.5-30 < mouseX < 575//2.5 + 160 and 750//3 < mouseY < 750//3+50:
            B.status = "Play"
        if 575//2.5-30 < mouseX < 575//2.5 + 160 and 750//2-60 < mouseY < 750//2-10:
            B.status = "Instruction"
    elif B.status == "Instruction":
        B.status = "Menu"
