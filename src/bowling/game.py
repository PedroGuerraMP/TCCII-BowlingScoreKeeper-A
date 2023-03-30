from typing import List

from bowling.frame import Frame


class BowlingGame:
    bonus: Frame

    def __init__(self):
        pass
    
    def add_frame(self, frame: Frame):
        frames = [frame]
        self.frames = frames
        pass

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def score(self) -> int:
        """ Get the score from the game """
        # To be implemented
        pass

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
