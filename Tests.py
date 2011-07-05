import unittest,pygame
import Animation as anim
meat=["eatme.png"]
big_chick=["ship1.png","ship11.png"]
mid_chick=["ship2.png","ship22.png"]
small_chick=["ship3.png","ship33.png"]
class InvadersTest(unittest.TestCase):
	def test_init(self):
		duck=anim.Animation(50,60,big_chick)	
		self.assertEqual(duck.x,50)
		self.assertEqual(duck.y,60)
		self.assertEqual(duck.vx,0)
		self.assertEqual(duck.vy,0)
		self.assertNotEqual(len(duck.pictures),0)
		
	def test_setfood_setup_check(self):		
		food=anim.Animation(5,5,meat)
		food.setfood(15,20)
		food.setfood(15,20)
		self.assertTrue(food.x,15)
		self.assertTrue(food.y,20)
		self.assertTrue(food.ttl,True)
				
	def test_update_duck_test(self):
		pygame.init()
		duck_big=anim.Animation(50,60,big_chick)
		duck_med=anim.Animation(100,200,mid_chick)
		duck_small=anim.Animation(400,300,small_chick)		
		screen=pygame.display.set_mode((800,600),0,32)
		duck_big.update(True)
		self.assertTrue(duck_big.ttl,True)
		self.assertNotEqual(duck_big.vx,0)
		self.assertNotEqual(duck_big.vy,0)
		self.assertNotEqual(len(duck_big.size),0)
		
	def test_update_food_test(self):	
		pygame.init()
		food=anim.Animation(5,5,meat)
		food.setfood(15,20)
		screen=pygame.display.set_mode((800,600),0,32)
		food=anim.Animation(5,5,meat)
		food.update(False)
		self.assertEqual(food.vx,0)
		self.assertNotEqual(food.vy,0)
		
	def test_collision_when_mouse_isnt_pressed(self):
		pygame.init()
		duck_big=anim.Animation(50,60,big_chick)
		duck_med=anim.Animation(100,200,mid_chick)
		duck_small=anim.Animation(400,300,small_chick)
		screen=pygame.display.set_mode((800,600),0,32)
		duck_big.update(True)
		duck_med.update(True)
		duck_small.update(True)
		result=anim.Animation.colision(duck_big,duck_med,duck_small,55,65)
		self.assertNotEqual(result,"big")
		self.assertNotEqual(result,"med")
		self.assertNotEqual(result,"small")		
		self.assertTrue(result,"missed")
	
	
if __name__ == '__main__':
    unittest.main()	