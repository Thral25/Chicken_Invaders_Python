import unittest
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
		
		
	def update_duck_test(self):
		duck_big=anim.Animation(50,60,big_chick)
		duck_med=anim.Animation(100,200,mid_chick)
		duck_small=anim.Animation(400,300,small_chick)		
		duck_big.update(True)
		self.assertTrue(duck_big.ttl,True)
		self.assertNotTrue(duck_big.vx,0)
		self.assertNotTrue(duck_big.vy,0)
		self.assertNotTrue(len(duck_big.size),0)
		
	def update_food_test(self):	
		food=anim.Animation(5,5,meat)
		food.setfood(15,20)
		food.update(False)
		self.assertTrue(food.vx,0)
		self.assertNotTrue(food.vy,0)
		
if __name__ == '__main__':
    unittest.main()	