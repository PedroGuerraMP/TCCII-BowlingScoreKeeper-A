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

    def test_get_game_finished(self):
        game = BowlingGame() 
        frame1 = Frame(1, 2)
        frame2 = Frame(1, 2)
        frame3 = Frame(1, 2)
        frame4 = Frame(1, 2)
        frame5 = Frame(1, 2)
        frame6 = Frame(1, 2)
        frame7 = Frame(1, 2)
        frame8 = Frame(1, 2)
        frame9 = Frame(1, 2)
        frame10 = Frame(1, 2)
        
        frameList = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]
        
        game.add_frame(frame1)
        game.add_frame(frame2)
        game.add_frame(frame3)
        game.add_frame(frame4)
        game.add_frame(frame5)
        game.add_frame(frame6)
        game.add_frame(frame7)
        game.add_frame(frame8)
        game.add_frame(frame9)
        game.add_frame(frame10)
        
        self.assertListEqual(game.get_game(), frameList)

    def test_get_game_unfinished(self):
        game = BowlingGame() 
        frame1 = Frame(1, 2)
        frame2 = Frame(1, 2)
        frame3 = Frame(1, 2)
        frame4 = Frame(1, 2)
        frame5 = Frame(1, 2)
        frame6 = Frame(1, 2)
        frame7 = Frame(1, 2)
        frame8 = Frame(1, 2)
        frame9 = Frame(1, 2)
        frame10 = Frame(1, 2)
        
        frameList = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]
        
        game.add_frame(frame1)
        game.add_frame(frame2)
        game.add_frame(frame3)
        game.add_frame(frame4)
        game.add_frame(frame5)
        game.add_frame(frame6)
        game.add_frame(frame7)
        
        with self.assertRaises(Exception) as context:
            game.get_game()

        self.assertTrue('Game unfinished', context.exception)

    def test_add_frames_finished_game(self):
        game = BowlingGame() 
        frame1 = Frame(1, 2)
        frame2 = Frame(1, 2)
        frame3 = Frame(1, 2)
        frame4 = Frame(1, 2)
        frame5 = Frame(1, 2)
        frame6 = Frame(1, 2)
        frame7 = Frame(1, 2)
        frame8 = Frame(1, 2)
        frame9 = Frame(1, 2)
        frame10 = Frame(1, 2)
                
        game.add_frame(frame1)
        game.add_frame(frame2)
        game.add_frame(frame3)
        game.add_frame(frame4)
        game.add_frame(frame5)
        game.add_frame(frame6)
        game.add_frame(frame7)
        game.add_frame(frame8)
        game.add_frame(frame9)
        game.add_frame(frame10)
        
        with self.assertRaises(Exception) as context:
            game.add_frame(frame1)
            
        self.assertTrue('Game already finished', context.exception)
        
    def test_get_finished_game_score(self):
        game = BowlingGame() 
        frame1 = Frame(1, 2)
        frame2 = Frame(1, 2)
        frame3 = Frame(1, 2)
        frame4 = Frame(1, 2)
        frame5 = Frame(1, 2)
        frame6 = Frame(1, 2)
        frame7 = Frame(1, 2)
        frame8 = Frame(1, 2)
        frame9 = Frame(1, 2)
        frame10 = Frame(1, 2)
                
        game.add_frame(frame1)
        game.add_frame(frame2)
        game.add_frame(frame3)
        game.add_frame(frame4)
        game.add_frame(frame5)
        game.add_frame(frame6)
        game.add_frame(frame7)
        game.add_frame(frame8)
        game.add_frame(frame9)
        game.add_frame(frame10)
        
        self.assertEqual(game.score(),30) 
        
        
if __name__ == '__main__':
    unittest.main()
