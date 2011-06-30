import pygame, sys, random, math,time
import Animation as anim
from pygame.locals import *
base=["sight.png","moonsmall.jpg"]
meat=["eatme.png"]
big_chick=["ship1.png","ship11.png"]
mid_chick=["ship2.png","ship22.png"]
small_chick=["ship3.png","ship33.png"]
class Game: 
	def speedup(duck_a,duck_b,duck_c,incr):
		duck_a.vx=duck_a.vx*incr
		duck_a.vy=duck_a.vy*incr
		duck_b.vx=duck_b.vx*incr
		duck_b.vy=duck_b.vy*incr
		duck_c.vx=duck_c.vx*incr
		duck_c.vy=duck_c.vy*incr
	def draw_ducks(duck_a,duck_b,duck_c,screen):
		ducks=[duck_a,duck_b,duck_c]
		for duck in ducks:
			pic=pygame.image.load(duck.picture).convert_alpha()
			screen.blit(pic,(duck.x,duck.y))
			duck.update(True)
	pygame.init()
	score=0
	screen=pygame.display.set_mode((800,600),0,32)
	bg=pygame.image.load(base[1])
	screen.blit(bg,(0,0))
	mouse=pygame.image.load(base[0])
	duck_a=anim.Animation(70,50,big_chick)
	duck_b=anim.Animation(170,250,mid_chick)
	duck_c=anim.Animation(80,400,small_chick)
	food_a=anim.Animation(0,600,meat)
	food_pic_a=pygame.image.load(food_a.picture).convert_alpha()
	food_b=anim.Animation(0,600,meat)
	food_pic_b=pygame.image.load(food_b.picture).convert_alpha()
	food_c=anim.Animation(0,600,meat)
	food_pic_c=pygame.image.load(food_c.picture).convert_alpha()
	pygame.mouse.set_visible(0)
	speed=3
	font_score = pygame.font.Font(None,25)
	font_end = pygame.font.Font(None,40)	
	while duck_a.ttl<60:
		screen.blit(bg,(0,0))	
		x,y=pygame.mouse.get_pos()
		x-= mouse.get_width()/2
		y-=mouse.get_height()/2
		screen.blit(mouse,(x,y))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()	
		draw_ducks(duck_a,duck_b,duck_c,screen)
		if(score>200)and(score<400)and(speed==3):
			speedup(duck_a,duck_b,duck_c,1.4)
			speed=speed-1
		elif(score>400)and(score<700)and(speed==2):
			speedup(duck_a,duck_b,duck_c,1.6)
			speed=speed-1
		elif(score>700)and(speed==1):
			speedup(duck_a,duck_b,duck_c,2)
			speed=0
		colide=anim.Animation.colision(duck_a,duck_b,duck_c,x,y)
		if(colide=="big"):
			score=score+2
			food_a.setfood(x,y)
		elif(colide=="med"):
			score=score+10
			food_b.setfood(x,y)
		elif(colide=="small"):
			score=score+30
			food_c.setfood(x,y)
		if (food_a.ttl==True):
			if (food_a.y<600):
				screen.blit(food_pic_a,(food_a.x,food_a.y))
			else:
				food_a.ttl=False
		if (food_b.ttl==True):
			if (food_b.y<600):
				screen.blit(food_pic_b,(food_b.x,food_b.y))
			else:
				food_b.ttl=False
		if (food_c.ttl==True):
			if (food_c.y<600):	
				screen.blit(food_pic_c,(food_c.x,food_c.y))
			else:
				food_c.ttl=False
		food_a.update(False)
		food_b.update(False)
		food_c.update(False)				
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
	