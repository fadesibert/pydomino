from tile import Tile
from enum import Enum
from exceptions import InvalidMoveError


class Edge(Enum):
    LEFT = 1
    RIGHT = 2


class Board:
    def __init__(self):
        self.tiles = list()

    @property
    def edges(self) -> tuple[int, int]:
        if not self.tiles:
            return None
        left_tile = self.tiles[0]
        right_tile = self.tiles[-1]
        return (left_tile.left, right_tile.right)

    def display_board(self):
        if not self.tiles:
            return "Board Empty"
        return ":".join([repr(x) for x in self.tiles])

    def play_tile(self, tile: Tile, play_edge: Edge | None = None):
        current_edges = self.edges
        if not self.tiles:
            self.tiles.append(tile)
            return None
        if play_edge:
            if play_edge == Edge.LEFT:
                if not tile.right == current_edges[0]:
                    if not tile.left == current_edges[0]:
                        raise InvalidMoveError(tile, current_edges)
                    elif tile.left == current_edges[0]:
                        tile.reverse()
                backwards = list(reversed(self.tiles))
                backwards.append(tile)
                self.tiles = list(reversed(backwards))
            elif play_edge == Edge.RIGHT:
                if not tile.left == current_edges[1]:
                    if not tile.right == current_edges[1]:
                        raise InvalidMoveError(tile, current_edges)
                    elif tile.right == current_edges[1]:
                        tile.reverse()
                self.tiles.append(tile)
        else:
            print("No edge specified, trying both")
            try:
                self.play_tile(tile, play_edge=Edge.LEFT)
            except InvalidMoveError:
                try:
                    self.play_tile(tile, play_edge=Edge.RIGHT)
                except InvalidMoveError as e:
                    raise e

    def __repr__(self):
        return self.display_board()

    def clear(self):
        self.tiles = list()
