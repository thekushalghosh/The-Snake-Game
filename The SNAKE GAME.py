'''
    Author : thekushalghosh
    Team   : CodeDiggers
'''
import os
import pygame
import pygame as pg
import time
import random
import webbrowser
from pygame.locals import *
 
pygame.init()
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
cyan = (0,255,255)
yellow = (255,255,0)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)
pink = (255,182,194)
violet = (59,0,93)
bright_red = (255,0,0)
bright_green = (0,255,0)

'''global bgcol

global bkcol

global ab

global aa

global spd

global scrr

global eatimg'''

eatimg = pygame.image.load('appl.png')

ab = 'bb.wav'

introm = 'introm.mp3'

aa = pygame.mixer.Sound("cc.wav")

global xs
global ys
global mvmt
global applepos
global img
global appleimage
global font
global score
global clk
global clkk

clk = 0

clkk = 0


hh = 0

scrr = 6

spd = 24

bkcol = yellow

bgcol = violet

global clickk

clickk = pygame.mixer.Sound("tick.wav")



gameDisplay = pygame.display.set_mode((display_width,display_height), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption('The SNAKE GAME (version - 1.0.0)')
clock = pygame.time.Clock()

gameIcon = pygame.image.load('ic.png')

intbg = pygame.image.load('snkbg.jpeg')
intbg = pygame.transform.scale(intbg, (800,600))
pygame.display.flip()

stnbg = pygame.image.load('settbg.png')
stnbg = pygame.transform.scale(stnbg, (800,600))
pygame.display.flip()

pygame.display.set_icon(gameIcon)

recta = intbg.get_rect()

recta = recta.move((0,0))

setta = stnbg.get_rect()

setta = recta.move((0,0))

istcbg = pygame.image.load('nxtimg.jpg')
istcbg = pygame.transform.scale(istcbg, (800,600))
pygame.display.flip()


rectis = istcbg.get_rect()

rectis = rectis.move((0,0))
gameDisplay.blit(istcbg, rectis)


def intromusic():
    pygame.mixer.music.load(introm)
    pygame.mixer.music.play(-1)
    game_intro()

def round_rect(surface, rect, color, rad=28, border=0, inside=(0,0,0,0)):
    """
    Draw a rect with rounded corners to surface.  Argument rad can be specified
    to adjust curvature of edges (given in pixels).  An optional border
    width can also be supplied; if not provided the rect will be filled.
    Both the color and optional interior color (the inside argument) support
    alpha.
    """
    rect = pg.Rect(rect)
    zeroed_rect = rect.copy()
    zeroed_rect.topleft = 0,0
    image = pg.Surface(rect.size).convert_alpha()
    image.fill((0,0,0,0))
    _render_region(image, zeroed_rect, color, rad)
    if border:
        zeroed_rect.inflate_ip(-2*border, -2*border)
        _render_region(image, zeroed_rect, inside, rad)
    surface.blit(image, rect)


def _render_region(image, rect, color, rad):
    """Helper function for round_rect."""
    corners = rect.inflate(-2*rad, -2*rad)
    for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
        pg.draw.circle(image, color, getattr(corners,attribute), rad)
    image.fill(color, rect.inflate(-2*rad,0))
    image.fill(color, rect.inflate(0,-2*rad))






def button(msg,x,y,w,h,ic,ac,r,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        round_rect(gameDisplay, (x-r,y-r,w+(2*r),h+(2*r)), ac)
        if click[0] == 1 and action != None:
            action()         
    else:
        round_rect(gameDisplay, (x-2,y-2,w+4,h+4), ic)
    smallText = pygame.font.SysFont("calibri",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    



def blocks(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

def urlfb():
    new = 2
    url = "www.facebook.com/thekushalghosh"
    webbrowser.open(url,new=new)

def urlin():
    new = 2
    url = "www.instagram.com/thekushalghosh"
    webbrowser.open(url,new=new)

def urltw():
    new = 2
    url = "www.twitter.com/thekushalghosh"
    webbrowser.open(url,new=new)

def urlqu():
    new = 2
    url = "www.quora.com/profile/Kushal-Ghosh-24"
    webbrowser.open(url,new=new)

def misc():
    global ab
    global aa
    global introm
    ab = 'bb.wav'
    aa = pygame.mixer.Sound("cc.wav")
    introm = 'introm.mp3'
    pygame.mixer.music.unpause()
    pygame.display.update()
    clock.tick(15)

def musc():
    global ab
    global aa
    global introm
    ab = 'sil.wav'
    aa = pygame.mixer.Sound("sil.wav")
    introm = 'sil.wav'
    pygame.mixer.music.pause()
    pygame.display.update()
    clock.tick(15)

def bcgcolgn():
    global bgcol
    bgcol = bright_green
    pygame.display.update()
    clock.tick(15)

def bcgcolvl():
    global bgcol
    bgcol = violet
    pygame.display.update()
    clock.tick(15)


def bcgcolpn():
    global bgcol
    bgcol = pink
    pygame.display.update()
    clock.tick(15)



def blkcolyl():
    global bkcol
    bkcol = yellow
    pygame.display.update()
    clock.tick(15)

def blkcolbl():
    global bkcol
    bkcol = black
    pygame.display.update()
    clock.tick(15)

def blkcolrd():
    global bkcol
    bkcol = bright_red
    pygame.display.update()
    clock.tick(15)


def spde():
    global spd
    global scrr
    global eatimg
    spd = 20
    scrr = 4
    eatimg = pygame.image.load('mngimg.png')
    pygame.display.update()
    clock.tick(15)


def spdm():
    global spd
    global scrr
    global eatimg
    spd = 24
    scrr = 6
    eatimg = pygame.image.load('appl.png')
    pygame.display.update()
    clock.tick(15)


def spdh():
    global spd
    global scrr
    global eatimg
    spd = 32
    scrr = 8
    eatimg = pygame.image.load('mngimg.png')
    pygame.display.update()
    clock.tick(15)



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def scores(count):
    font = pygame.font.SysFont("copperplate gothic", 25)
    name = pygame.font.SysFont("Segoe UI", 25)
    text = font.render("Your Score: "+str(count), True, black)
    hs = font.render("High Score: "+str(hh), True, black)
    hmm = name.render("By : Kushal Ghosh", True, white)
    gameDisplay.blit(text,(10,10))
    gameDisplay.blit(hs,(14,35))
    gameDisplay.blit(hmm,(600,14))


def quitgame():
    pygame.quit()
    quit()


def eat(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
        return True
    else:
        return False


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(aa)
    largeText = pygame.font.SysFont("chiller",155)
    TextSurf, TextRect = text_objects("GAME OVER", largeText)
    TextRect.center = ((display_width/2),(display_height/2.5))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
    

        button("Try Again",120,400,120,50,green,bright_green,9,game_play)
        button("Main Menu",350,400,150,50,(112,128,144),(192,192,192),9,intromusic)
        button("Exit",600,400,100,50,red,bright_red,9,quitgame)

        pygame.display.update()
        clock.tick(15) 
        
def game_intro():

    intro = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(intbg, recta)
        largeText = pygame.font.SysFont("broadway",75)
        smallText = pygame.font.SysFont("forte",68)
        name = pygame.font.SysFont("Segoe UI", 25)
        TextSurf, TextRect = text_objects("The", smallText)
        TextSurf1, TextRect1 = text_objects("SNAKE", largeText)
        TextSurf2, TextRect2 = text_objects("GAME", largeText)
        TextRect.center = (118,464)
        TextRect1.center = (329,460)
        TextRect2.center = (610,460)
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf1, TextRect1)
        gameDisplay.blit(TextSurf2, TextRect2)

        button("f",593,14,35,35,(59,89,239),(68,143,255),7,urlfb)
        button("[o]",648,14,35,35,(255,20,149),(95,95,95),7,urlin)
        button("t",703,14,35,35,(29,161,242),(0,0,255),7,urltw)
        button("Q",759,14,35,35,(239,0,0),(255,0,0),7,urlqu)


        button("Play",608,100,149,50,green,bright_green,9,countdown)
        button("Instructions",608,177,149,50,red,bright_red,9,instrc)
        button("Settings",608,257,149,50,(112,128,144),(192,192,192),9,sett)
        button("Info",608,338,149,50,yellow,(255,255,100),9,info)
        

        pygame.display.update()
        clock.tick(15)

def sett():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.blit(stnbg, setta)
        
        bgdcol = pygame.font.SysFont("Segoe UI",40)
        blkcol = pygame.font.SysFont("Segoe UI",40)
        gmms = pygame.font.SysFont("Segoe UI",40)
        sppd = pygame.font.SysFont("Segoe UI",40)
        TextSurf3, TextRect3 = text_objects("Choose Background Colour", bgdcol)
        TextSurf4, TextRect4 = text_objects("Choose Snake Colour", blkcol)
        TextSurf5, TextRect5 = text_objects("Choose Difficulty", sppd)
        TextSurf6, TextRect6 = text_objects("Game Music",gmms)
        TextRect3.center = (257,90)
        TextRect4.center = (203,210)
        TextRect5.center = (170,330)
        TextRect6.center = (132,440)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        gameDisplay.blit(TextSurf6, TextRect6)
        button("<- RETURN",302,540,150,50,(153,217,234),(163,227,244),9,game_intro)
        
        button("Green",100,120,100,50,green,bright_green,6,bcgcolgn)
        button("Violet",275,120,100,50,(167,0,237),(189,33,255),6,bcgcolvl)
        button("Pink",450,120,100,50,(255,116,140),(255,141,161),6,bcgcolpn)
        
        button("Yellow",100,240,100,50,yellow,(255,255,100),6,blkcolyl)
        button("Black",275,240,100,50,(169,169,169),(207,207,207),6,blkcolbl)
        button("Red",450,240,100,50,red,bright_red,6,blkcolrd)

        button("Easy",100,360,100,50,green,bright_green,6,spde)
        button("Medium",275,360,100,50,yellow,(255,255,100),6,spdm)
        button("Hard",450,360,100,50,red,bright_red,6,spdh)
        
        button("On",100,470,100,50,green,bright_green,6,misc)
        button("Off",275,470,100,50,red,bright_red,6,musc)
        
        pygame.display.update()
        clock.tick(15)


def info():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(cyan)

        cred = pygame.font.SysFont("Algerian",60)
        cred1 = pygame.font.SysFont("Segoe UI",25)
        cred2 = pygame.font.SysFont("Segoe UI",25)

        TextSurf6, TextRect6 = text_objects("Credits :-",cred)
        TextSurf7, TextRect7 = text_objects("Developer : KUSHAL GHOSH  :: Contact Links-",cred1)
        TextSurf8, TextRect8 = text_objects("Special thanks to Ketchapp Inc. and Gamotronix Inc. for the music.",cred2)

        TextRect6.center = (392,100)
        TextRect7.center = (300,200)
        TextRect8.center = (402,300)

        gameDisplay.blit(TextSurf6, TextRect6)
        gameDisplay.blit(TextSurf7, TextRect7)
        gameDisplay.blit(TextSurf8, TextRect8)
        button("<- RETURN",303,500,150,50,cyan,(100,255,255),6,game_intro)
        button("f",545,185,35,35,(59,89,239),(68,143,255),7,urlfb)
        button("[o]",603,185,35,35,(255,20,149),(95,95,95),7,urlin)
        button("t",660,185,35,35,(29,161,242),(0,0,255),7,urltw)
        button("Q",719,185,35,35,(239,0,0),(255,0,0),7,urlqu)
        
        pygame.display.update()
        clock.tick(15)
        

    

def instrc():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(istcbg, rectis)

        button("<- RETURN",248,500,135,44,(153,217,234),(163,227,244),9,game_intro)
    
        pygame.display.update()
        clock.tick(15)

def unpause():

    pygame.mixer.music.unpause()
    global pause
    pause = False

def paused():
    
    pygame.mixer.music.pause()
    largeText = pygame.font.SysFont("calculator",135)
    TextSurf, TextRect = text_objects("PAUSED", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
                
            

       
        button("Resume",150,450,100,50,green,bright_green,8.6,unpause)
        button("Exit",550,450,100,50,red,bright_red,8.6,quitgame)


        pygame.display.update()
        clock.tick(15)


def delay():
    t0 = time.time()
    dur = 1.0
    while True:
        time.sleep(dur)
        t1 = time.time()
        dur = 1.0 - (t1 - t0)
        if dur <= 0:
            break


def countdown():
    w = ["3","2","1"]
    gameDisplay.fill(bgcol)
    for i in w:
        pygame.time.delay(400)
        largeText = pygame.font.SysFont("calculator",135)
        TextSurf, TextRect = text_objects(i, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()



            pygame.display.update()
            clock.tick(15)
                    
            game_play()


def game_play():
    global hh

    xs = [290, 290, 290, 290, 290]
    ys = [176, 155, 135, 115, 95]

    mvmt = 0

    score = 0

    global pause

    pygame.mixer.music.load(ab)
    pygame.mixer.music.play(-1)
    
    img = pygame.Surface((20, 20))
    img.fill(bkcol)

    appleimage = eatimg
    

    applepos = (random.randint(0, 590), random.randint(0, 590))

    bldm = 20
    blhx = display_width/2
    blhy = display_height/2

    gameExit = False

    while not gameExit:
    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

            
            elif e.type == KEYDOWN:
                if e.key == K_UP and mvmt != 0:
                    mvmt = 2
                elif e.key == K_DOWN and mvmt != 2:
                    mvmt = 0
                elif e.key == K_LEFT and mvmt != 1:
                    mvmt = 3
                elif e.key == K_RIGHT and mvmt != 3:
                    mvmt = 1
                if e.key == pygame.K_p:
                    pause = True
                    paused()
        
        i = len(xs)-1
        
        while i >= 2:
            if eat(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
                crash()
            i -= 1
            
        if eat(xs[0], applepos[0], ys[0], applepos[1], 25, 25, 20, 20):
            score += scrr
            xs.append(0)
            ys.append(0)
            applepos=(random.randint(0,770),random.randint(0,563))

            
        if xs[0] < 0 or xs[0] > 786 or ys[0] < 0 or ys[0] > 572:
            crash()
            
            
        i = len(xs)-1


        
        while i >= 1:
            xs[i] = xs[i-1]
            ys[i] = ys[i-1]
            i -= 1
        if mvmt==0:
            ys[0] += spd
        elif mvmt==1:
            xs[0] += spd
        elif mvmt==2:
            ys[0] -= spd
        elif mvmt==3:
            xs[0] -= spd
            

	
        gameDisplay.fill(bgcol)

        if score > hh:
            hh = score
        scores(score)

        
 
        for i in range(0, len(xs)):
            gameDisplay.blit(img, (xs[i], ys[i]))

        gameDisplay.blit(appleimage, applepos)
         
        pygame.display.update()
        clock.tick(15)

intromusic()

