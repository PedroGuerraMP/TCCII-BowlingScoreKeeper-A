from typing import List

from bowling.frame import Frame


class BowlingGame:
    bonus: Frame

    def __init__(self):
        self.frames = []
        pass
    
    def add_frame(self, frame: Frame):
        if(len(self.frames) < 10):
            self.frames.append(frame)
        else: 
            raise Exception('Game already finished')
        pass

    def get_game(self):
        self.isGameFinished()
        
        return self.frames
            
    
    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def score(self) -> int:
        sum = 0

        self.isGameFinished()

        for frame in self.frames:
            sum += frame.score()
        
        return sum       
        

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
    
    def isGameFinished(self):
        if(len(self.frames) != 10):
            raise Exception('Game unfinished')
        else:
            pass
