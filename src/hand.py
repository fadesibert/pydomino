from tile import Tile
from random import randrange


class Hand:
    def __init__(self, tiles: list[Tile] | None = None):
        if tiles:
            self.tiles = tiles
        else:
            self.tiles: list[Tile | None] = list()

    def add_tile(self, tile: Tile):
        pass

    def play_tile(self, tile_index: int) -> Tile:
        tile = self.tiles[tile_index]
        del self.tiles[tile_index]
        return tile

    def list_hand(self) -> str:
        return ", ".join([f"{x!r}" for x in self.tiles])

    def __repr__(self):
        return self.list_hand()

    def __iter__(self):
        yield from self.tiles

    @property
    def total(self):
        return sum(self.tiles)


class Boneyard(Hand):
    # Tiles aren't optional when initializing the boneyard
    def __init__(self, tiles=list[Tile]):
        super().__init__(tiles)

    def draw_random(self):
        index = randrange(len(self.tiles))
        drawn_tile = self.tiles[index]
        del self.tiles[index]
        return drawn_tile
