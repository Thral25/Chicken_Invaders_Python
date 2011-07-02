import pygame, sys, random, math,time
import Animation as anim
from pygame.locals import *
base=["sight.png","moonsmall.jpg"]
meat=["eatme.png"]
big_chick=["ship1.png","ship11.png"]
mid_chick=["ship2.png","ship22.png"]
small_chick=["ship3.png","ship33.png"]
class Game: 
	def speedup(ducks,incr):
		for duck in ducks:
			duck.vx=duck.vx*incr
			duck.vy=duck.vy*incr
	def draw_ducks(ducks,screen):
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
	ducks=[anim.Animation(70,50,big_chick), anim.Animation(170,250,mid_chick), anim.Animation(80,400,small_chick)]
	foods=[anim.Animation(0,600,meat),anim.Animation(0,600,meat),anim.Animation(0,600,meat)]
	pygame.mouse.set_visible(0)
	speed=3
	font_score = pygame.font.Font(None,25)
	font_end = pygame.font.Font(None,40)	
	while ducks[0].ttl<60:
		screen.blit(bg,(0,0))	
		x,y=pygame.mouse.get_pos()
		x-= mouse.get_width()/2
		y-=mouse.get_height()/2
		screen.blit(mouse,(x,y))
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()	
		draw_ducks(ducks,screen)
		if(score>200)and(score<400)and(speed==3):
			speedup(ducks,1.4)
			speed=speed-1
		elif(score>400)and(score<700)and(speed==2):
			speedup(ducks,1.6)
			speed=speed-1
		elif(score>700)and(speed==1):
			speedup(ducks,2)
			speed=0
		colide=anim.Animation.colision(ducks[0],ducks[1],ducks[2],x,y)
		if(colide=="big"):
			score=score+2
			foods[0].setfood(x,y)
		elif(colide=="med"):
			score=score+10
			foods[1].setfood(x,y)
		elif(colide=="small"):
			score=score+30
			foods[2].setfood(x,y)
		for food in foods:
			if (food.ttl==True):
				if (food.y<600):
					food_pic=pygame.image.load(food.picture).convert_alpha()
					screen.blit(food_pic,(food.x,food.y))
				else:
					food.ttl=False			
			food.update(False)				
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
		if(ducks[0].ttl>60):
			end = font_end.render("Game Over", 1, (5, 5, 5))
			screen.blit(score_text,(735,45))	
			screen.blit(end,(300,200))
			pygame.display.update()