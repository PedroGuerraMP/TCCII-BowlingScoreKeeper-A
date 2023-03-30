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
        if(len(self.frames) == 10):
            return self.frames
        else: 
            raise Exception('Game unfinished')
            
    
    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def score(self) -> int:
        sum = 0
        
        for frame in self.frames:
            sum += frame.score()

        return sum

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
