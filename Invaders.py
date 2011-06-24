import pygame, sys, random, math,threading,time
from pygame.locals import *
base=["sight.png","moonsmall.jpg"]
big_chick=["ship1.png","ship11.png"]
mid_chick=["ship2.png","ship22.png"]
small_chick=["ship3.png","ship33.png"]
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
		
	def update(self):
		ms=self.clock.tick()
		sec=ms/1000.
		pic=pygame.image.load(self.picture).convert_alpha()
		self.ttl+=sec
		speed=120*sec
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
			self.vx=-math.fabs(self.vx)
		elif self.y+self.size[1]>600:
			self.vy=-math.fabs(self.vy)
		elif self.x<0:
			self.vx=math.fabs(self.vx)
		elif self.y<0:
			self.vy=math.fabs(self.vy)
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
	duck_b=Animation(170,250,mid_chick)
	duck_c=Animation(75,400,small_chick)
	pygame.mouse.set_visible(0)
	speed=3
	curtime=int(time.time())%100
	runtime=0
	font_score = pygame.font.Font(None,25)
	font_end = pygame.font.Font(None,40)	
	while duck_a.ttl<60:
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
		if(runtime==0):		
			runtime=int(time.time())%100-curtime
		else:
			runtime=runtime+int(time.time())%100-runtime
		screen.blit(bg,(0,0))				
		pic1=pygame.image.load(duck_a.picture).convert_alpha()
		pic2=pygame.image.load(duck_b.picture).convert_alpha()
		pic3=pygame.image.load(duck_c.picture).convert_alpha()
		screen.blit(pic1,(duck_a.x,duck_a.y))
		screen.blit(pic2,(duck_b.x,duck_b.y))
		screen.blit(pic3,(duck_c.x,duck_c.y))
		if(score>200)and(score<400)and(speed==3):
			duck_a.vx=duck_a.vx*1.5
			duck_a.vy=duck_a.vy*1.5
			duck_b.vx=duck_b.vx*1.5
			duck_b.vy=duck_b.vy*1.5
			duck_c.vx=duck_c.vx*1.5
			duck_c.vy=duck_c.vy*1.5
			speed=speed-1
		elif(score>400)and(score<700)and(speed==2):
			duck_a.vx=duck_a.vx*1.7
			duck_a.vy=duck_a.vy*1.7
			duck_b.vx=duck_b.vx*1.7
			duck_b.vy=duck_b.vy*1.7
			duck_c.vx=duck_c.vx*1.7
			duck_c.vy=duck_c.vy*1.7
			speed=speed-1
		elif(score>700)and(speed==1):
			duck_a.vx=duck_a.vx*2
			duck_a.vy=duck_a.vy*2
			duck_b.vx=duck_b.vx*2
			duck_b.vy=duck_b.vy*2
			duck_c.vx=duck_c.vx*2
			duck_c.vy=duck_c.vy*2
			speed=0
		duck_a.update()
		duck_b.update()
		duck_c.update()
		x,y=pygame.mouse.get_pos()
		x-= mouse.get_width()/2
		y-=mouse.get_height()/2
		screen.blit(mouse,(x,y))
		if (x>=duck_a.x) and(x<duck_a.x+duck_a.size[0])and(y>=duck_a.y)and(y<duck_a.y+duck_a.size[1])and(True in pygame.mouse.get_pressed()):
			score=score+2
			duck_a.x=random.randint(50,750)
			duck_a.y=random.randint(50,550)
		if (x>=duck_b.x) and(x<duck_b.x+duck_b.size[0])and(y>=duck_b.y)and(y<duck_b.y+duck_b.size[1])and(True in pygame.mouse.get_pressed()):
			score=score+10
			duck_b.x=random.randint(50,750)
			duck_b.y=random.randint(50,550)
		if (x>=duck_c.x) and(x<duck_c.x+duck_c.size[0])and(y>=duck_c.y)and(y<duck_c.y+duck_c.size[1])and(True in pygame.mouse.get_pressed()):
			score=score+30
			duck_c.x=random.randint(50,750)
			duck_c.y=random.randint(50,550)	
		score_text = font_score.render(str(score), 1, (10, 10, 10))
		screen.blit(score_text,(735,45))	
		pygame.display.update()
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
		if(duck_a.ttl>60):
			end = font_end.render("Game Over", 1, (5, 5, 5))
			screen.blit(score_text,(735,45))	
			screen.blit(end,(300,200))
			pygame.display.update()
		