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
        last_frame_was_strike: bool = False
        for frame in self.frames:
            if(last_frame_was_strike):
                sum += (frame.score()*2)
            else:
                sum += frame.score()
                
            last_frame_was_strike = frame.is_strike()
        
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
