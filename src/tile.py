from dataclasses import dataclass


class TileException(ValueError):
    pass


@dataclass
class Tile:
    left: int
    right: int

    def __post_init__(self):
        if self.left < 0 or self.left > 6:
            raise TileException(self.left)
        if self.right < 0 or self.right > 6:
            raise TileException(self.right)

    def __repr__(self):
        return f"[{self.left} | {self.right}]"

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __hash__(self):
        # left | right != right | left
        return hash(f"left:{self.left}|right{self.right}")


if __name__ == "__main__":
    t = Tile(left=3, right=6)
    print(t)