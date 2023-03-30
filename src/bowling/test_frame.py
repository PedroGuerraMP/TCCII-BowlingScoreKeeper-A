import unittest

from bowling.frame import Frame


class TestFrames(unittest.TestCase):
    
    def test_get_score(self):
        throw1 = 5
        throw2 = 4
        frame = Frame(throw1, throw2)
        
        self.assertEqual((throw1+throw2), frame.score())



if __name__ == '__main__':
    unittest.main()
