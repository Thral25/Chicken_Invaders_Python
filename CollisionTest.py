import unittest,pygame,random, math,time,sys
import Animation as anim
meat=["eatme.png"]
big_chick=["ship1.png","ship11.png"]
mid_chick=["ship2.png","ship22.png"]
small_chick=["ship3.png","ship33.png"]
class CollisonTest(unittest.TestCase):
	def collision_when_mouse_pressed(self):
			duck_big=anim.Animation(50,60,big_chick)
			duck_med=anim.Animation(100,200,mid_chick)
			duck_small=anim.Animation(400,300,small_chick)
			duck_big.update(True)
			duck_med.update(True)
			duck_small.update(True)
			result=anim.Animation.colision(duck_big,duck_med,duck_small,55,65)
			self.assertTrue(result,"big")
			self.assertTrue(result,"med")
			self.assertTrue(result,"small")
			
if __name__ == '__main__':
    unittest.main()	