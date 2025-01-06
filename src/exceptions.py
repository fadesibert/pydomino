class NoMovesError(Exception):
    pass


class InvalidMoveError(Exception):
    pass


class BoneyardEmptyError(NoMovesError):
    pass
