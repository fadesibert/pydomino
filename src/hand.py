from tile import Tile
from random import randrange


class Hand:
    def __init__(self, tiles: list[Tile] | None = None):
        if tiles:
            self.tiles = tiles
        else:
            self.tiles: list[Tile | None] = list()

    def add_tile(self, Tile):
        pass

    def play_tile(self, Tile):
        pass

    def list_hand(self) -> str:
        return ", ".join([f"{x!r}" for x in self.tiles])

    def __repr__(self):
        return self.list_hand()


class Boneyard(Hand):
    # Tiles aren't optional when initializing the boneyard
    def __init__(self, tiles=list[Tile]):
        super().__init__(tiles)

    def draw_random(self):
        index = randrange(len(self.tiles))
        drawn_tile = self.tiles[index]
        del self.tiles[index]
        return drawn_tile
