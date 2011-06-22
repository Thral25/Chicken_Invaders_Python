import pygame, sys, random, math
from pygame.locals import *
base=["sight.png","moonsmall.jpg"]
big_chick=["ship1.png","ship11.png"]
class Animation:
	def __init__(self,x,y,pictures):
		self.x=x
		self.y=y
		self.time=0
		self.pictures=pictures
		self.picture=pictures[0]
		self.clock=pygame.time.Clock()
		self.vx=0
		self.vy=0
		self.size=[]
		
	def update(self):
		ms=self.clock.tick()
		sec=ms/1000.
		pic=pygame.image.load(self.picture).convert_alpha()
		sec=self.clock.tick()/1000.
		speed=1000*sec
		self.size=[pic.get_width(),pic.get_height()]
		if(self.vx==0)or(self.vy==0):
			self.vx=speed
			self.vy=speed
		if (sec != self.time)and(self.picture !=self.pictures[1]) :
			self.time=sec
			self.picture=self.pictures[1]
		elif (sec != self.time)and(self.picture !=self.pictures[0]):
			self.time=sec
			self.picture=self.pictures[0]
		if self.x+self.size[0]>800:
			self.vx=-math.fabs(speed)
		elif self.y+self.size[1]>600:
			self.vy=-math.fabs(speed)
		elif self.x<0:
			self.vx=math.fabs(speed)
		elif self.y<0:
			self.vy=math.fabs(speed)
		self.x+=self.vx
		self.y+=self.vy	
class Game(Animation): 
	pygame.init()
	score=0
	screen=pygame.display.set_mode((800,600),0,32)
	bg=pygame.image.load(base[1])
	screen.blit(bg,(0,0))
	mouse=pygame.image.load(base[0])
	duck_a=Animation(10,50,big_chick)
	pygame.mouse.set_visible(0)
	while True:		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		screen.blit(bg,(0,0))			
		x,y=pygame.mouse.get_pos()
		x-= mouse.get_width()/2
		y-=mouse.get_height()/2
		screen.blit(mouse,(x,y))
		pic1=pygame.image.load(duck_a.picture).convert_alpha()
		screen.blit(pic1,(duck_a.x,duck_a.y))
		duck_a.update()
		if (x>=duck_a.x) and(x<=duck_a.x+duck_a.size[0])and(y>=duck_a.y)and(y<=duck_a.y+duck_a.size[1])and(True in pygame.mouse.get_pressed()):
			score=score+1
			duck_a.x=random.randint(50,750)
			duck_a.y=random.randint(50,550)
		pygame.display.update()
