import unittest
from bowling.frame import Frame
from bowling.game import BowlingGame


class TestGames(unittest.TestCase):
    
    def test_add_frame(self):
        game = BowlingGame()
        frame = Frame(1, 2)
        
        game.add_frame(frame)
        
        self.assertTrue( game.frames.index(frame) >= 0 )

    def test_add_frames(self):
        game = BowlingGame()
        frame1 = Frame(1, 2)
        frame2 = Frame(1, 2)
        
        game.add_frame(frame1)
        game.add_frame(frame2)
        
        self.assertTrue( game.frames.index(frame1) >= 0 )
        self.assertTrue( game.frames.index(frame2) >= 0 )

if __name__ == '__main__':
    unittest.main()
