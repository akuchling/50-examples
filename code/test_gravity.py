
import unittest, math
import gravity

class TestGravity(unittest.TestCase):
    def test_attraction(self):
        b1 = gravity.Body()
        b2 = gravity.Body()
        b1.mass = b2.mass = 1
        b1.px, b1.py = 0,0
        b2.px, b2.py = 100,0

        fx, fy = b1.attraction(b2)
        self.assertAlmostEqual(fx, gravity.G/100**2, places=15)
        self.assertAlmostEqual(fy, 0, places=15)

        fx, fy = b2.attraction(b1)
        self.assertAlmostEqual(fx, -gravity.G/100**2, places=15)
        self.assertAlmostEqual(fy, 0, places=15)

        b2.py = 100
        fx, fy = b1.attraction(b2)
        self.assertAlmostEqual(fx, gravity.G/20000 * (math.sqrt(2)/2),
                               places=15)
        self.assertAlmostEqual(fy, gravity.G/20000 * (math.sqrt(2)/2),
                               places=15)

        
if __name__ == '__main__':
    unittest.main()
