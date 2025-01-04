from abc import ABC, abstractmethod
from hand import Hand


class Player(ABC):
    def __init__(self, name: str, hand: Hand | None = None):
        self.name = name
        self.score = 0
        if not Hand:
            self.hand = Hand()
        else:
            self.hand = hand

    def new_hand(self, hand: Hand):
        self.hand = hand

    def available_moves(self, edges: tuple[int, int] | None):
        if not edges:
            return enumerate(self.hand)
        for idx, tile in enumerate(self.hand):
            if (
                tile.left == edges[0]
                or tile.left == edges[1]
                or tile.right == edges[0]
                or tile.right == edges[1]
            ):
                yield idx, tile

    def draw(self, yard):
        new_tile = yard.draw_random()
        print(f"Drew {new_tile=}")
        self.hand.add_tile(new_tile)

    @abstractmethod
    def play(self, edges: tuple[int] | None):
        pass

    @property
    def points_in_hand(self):
        return self.hand.total


class HumanPlayer(Player):
    def play(self, edges: tuple[int] | None) -> int:
        a = list(self.available_moves(edges))
        print(f"Available moves: {a}")
        breakpoint()


class ComputerPlayer(Player):
    def choose_best_move(go_tiles):
        pass

    def play(self):
        a = self.available_moves(edges)
        pass


if __name__ == "__main__":
    a = HumanPlayer("Thing")
    b = ComputerPlayer("Other")

    print(isinstance(a, HumanPlayer))
    print(isinstance(a, Player))
