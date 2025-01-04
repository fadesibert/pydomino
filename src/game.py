from tile import Tile
from hand import Hand, Boneyard
from itertools import product

default_range = range(0, 6)
default_tiles = list()
for l in default_range:
    for r in default_range:
        default_tiles.append(Tile(l, r))


def setup_boneyard() -> Boneyard:
    b = Boneyard(default_tiles)
    return b


def setup_hands(yard: Boneyard, start_num_tiles: int = 7) -> tuple[Hand, Hand]:
    h0 = []
    h1 = []
    for i in range(0, start_num_tiles):
        h0.append(yard.draw_random())
        h1.append(yard.draw_random())
    return (Hand(h0), Hand(h1))


if __name__ == "__main__":
    b = setup_boneyard()
    print(b)
    hand_0, hand_1 = setup_hands(b)
    print(hand_0)
    print(hand_1)

    ## Randomly draw all tiles
    # for i in range(0,36):
    #    t = b.draw_random()
    #    print(f'Drew: {t!r}')
    #    print(f'Boneyard: {b!r}')
