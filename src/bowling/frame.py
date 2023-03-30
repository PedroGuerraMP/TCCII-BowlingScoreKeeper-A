class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        self.first_throw = first_throw
        self.second_throw = second_throw

    def score(self) -> int:
        return self.first_throw + self.second_throw

    def is_strike(self) -> bool:
        if(self.first_throw == 10 and self.second_throw  == 0):
            return True
        else:
            return False
        pass

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        # To be implemented
        pass

    def is_last_frame(self) -> bool:
        """ Return whether the frame is a last frame of the game """
        # To be implemented
        pass

    def bonus(self) -> int:
        """ Bonus throw """
        # To be implemented
        pass
