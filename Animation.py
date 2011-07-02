import pygame, sys, random, math,time
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
		self.ttl=0
		
	def update(self,alien_flag):
		ms=self.clock.tick()
		sec=ms/1000.
		pic=pygame.image.load(self.picture).convert_alpha()
		if alien_flag:
			self.ttl+=sec
		else:
			self.ttl=True
		speed=150*sec
		self.size=[pic.get_width(),pic.get_height()]
		if(alien_flag):
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
				self.vx=-math.fabs(self.vx)
			elif self.y+self.size[1]>600:
				self.vy=-math.fabs(self.vy)
			elif self.x<0:
				self.vx=math.fabs(self.vx)
			elif self.y<0:
				self.vy=math.fabs(self.vy)
			self.x+=self.vx
			self.y+=self.vy
		else:
			self.vx=0
			self.vy=math.fabs(speed) + 2
			self.y+=self.vy
			if self.y>600:
				self.vy=0
		
	def setfood(self,x,y):
		self.x=x
		self.y=y
		self.ttl=True	
		
	def colision(duck_a,duck_b,duck_c,x,y):
		ducks={'big':duck_a,'med':duck_b,'small':duck_c}
		for key ,duck in ducks.iteritems():
			if (x>=duck.x) and(x<duck.x+duck.size[0])and(y>=duck.y)and(y<duck.y+duck.size[1])and(True in pygame.mouse.get_pressed()):
				duck.x=random.randint(50,750)
				duck.y=random.randint(50,550)
				return key
		return "missed"