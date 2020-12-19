class TrackedNumber:
    def __init__(self):
        self._turns_said = (-1, -1)

    def say(self, turn: int):
        self._turns_said = (self._turns_said[1], turn)

    def get_number_to_say(self):
        if self._turns_said == (-1, -1):
            raise NumberNeverSaidBeforeException(
                "The number was never said before, so there is no rule for that."
            )
        elif self._turns_said[0] == -1:
            return 0
        else:
            return self._turns_said[1] - self._turns_said[0]


class NumberNeverSaidBeforeException(Exception):
    pass
