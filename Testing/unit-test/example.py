import unittest

class rectangle:
    def __init__(self, width, height):
        self.width = width 
        self.height = height 

    def get_area(self):
        return self.width * self.height 
    
    def set_width(self, width):
        self.width = width 

    def set_height(self, height):
        self.height = height 

class testrectangle(unittest.TestCase):
    def runTest(self):
        rectangles = rectangle(2,3)
        self.assertEqual(rectangles.get_area(), 6, 'incorrest area')
    def test_negative_case(self):
        rectangles = rectangle(-1,2)
        self.assertEqual(rectangles.get_area(), -1, 'incorrect negative')
    
    def test_assert_raises(self): 
        """using assertRaises to detect if an expected error is raised when running a particular block of code"""
        with self.assertRaises(ZeroDivisionError):
            a = 1 / 0

class testgetarea(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.rectangle = rectangle(0,0)

    def test_normal_case(self):
        self.rectangle.set_width(2)
        self.rectangle.set_height(3)
        self.assertEqual(self.rectangle.get_area(), 6, 'incorrect area')
    
    def test_geq(self):
        self.assertGreaterEqual(self.rectangle.get_area(), -1) 
    
    def test_assert_raises(self):
        with self.assertRaises(ZeroDivisionError):
            a = 1 / 0

calculate_area = unittest.TestLoader() \
                 .loadTestsFromTestCase(testgetarea)

runner = unittest.TextTestRunner() 
runner.run(calculate_area)
#unittest.main()