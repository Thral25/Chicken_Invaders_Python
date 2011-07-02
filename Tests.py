import unittest,pygame
import Animation as anim
meat=["eatme.png"]
big_chick=["ship1.png","ship11.png"]
mid_chick=["ship2.png","ship22.png"]
small_chick=["ship3.png","ship33.png"]
class InvadersTest(unittest.TestCase):
	def test_setfood_setup_check(self):
		food=anim.Animation(5,5,meat)
		food.setfood(15,20)
		self.assertTrue(food.x,15)
		self.assertTrue(food.y,20)
		self.assertTrue(food.ttl,True)
	 
	def colision_when_mouse_pressed(self):
		duck_big=anim.Animation(50,60,big_chick)
		duck_med=anim.Animation(100,200,mid_chick)
		duck_small=anim.Animation(400,300,small_chick)
		result=anim.Animation.collision(duck_big,duck_med,duck_small,55,65)
		self.assertEqual(result,"big")
		self.assertEqual(result,"med")
		self.assertEqual(result,"small")
		
if __name__ == '__main__':
    unittest.main()	