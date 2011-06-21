list=["sight.png","moonsmall.jpg"]
big_chick=["ship1.png","ship11.png"]
import pygame, sys
from pygame.locals import *
class Animation:
	def __init__(self,x,y,pictures):
		self.x=x
		self.y=y
		self.time=0
		self.pictures=pictures
		self.picture=pictures[0]
		self.clock=pygame.time.Clock()
		
	def update(self):
		ms=self.clock.tick()
		sec=ms/1000.
		if (sec != self.time)and(self.picture !=self.pictures[1]) :
			self.time=sec
			self.picture=self.pictures[1]
		elif (sec != self.time)and(self.picture !=self.pictures[0]):
			self.time=sec
			self.picture=self.pictures[0]
	
class Game(Animation): 
	pygame.init()
	score=0
	screen=pygame.display.set_mode((800,600),0,32)
	bg=pygame.image.load(list[1])
	screen.blit(bg,(0,0))
	mouse=pygame.image.load(list[0])
	duck_a=Animation(10,50,big_chick)
	while True:		
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		screen.blit(bg,(0,0))	
		pygame.mouse.set_visible(0)		
		x,y=pygame.mouse.get_pos()
		x-= mouse.get_width()/2
		y-=mouse.get_height()/2
		screen.blit(mouse,(x,y))
		pic1=pygame.image.load(duck_a.picture).convert_alpha()
		screen.blit(pic1,(duck_a.x,duck_a.y))
		duck_a.update()
		pygame.display.update()
