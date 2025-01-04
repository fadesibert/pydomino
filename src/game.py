from tile import Tile
from hand import Hand, Boneyard
from board import Board, Edge
from itertools import combinations_with_replacement

default_range = range(0, 7)
default_tups = list(combinations_with_replacement(default_range, 2))
default_tiles = [Tile(x, y) for x, y in default_tups]


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


def play_tile(hand: Hand, index: int, board: Board, side: Edge | None = None) -> Board:
    tile_to_play = hand.play_tile(index)
    print(f"{tile_to_play=}")
    # Catch some errors here
    try:
        board.play_tile(tile_to_play, side)
    except ValueError:
        print("Invalid play! Returning tile to hand")
        hand.add_tile(tile_to_play)
        return board
    print(f"Played {tile_to_play}")
    print(f"{board=}")
    return board


if __name__ == "__main__":
    b = setup_boneyard()
    print(b)
    hand_0, hand_1 = setup_hands(b)
    board = Board()
    print(f"{hand_0=} {hand_0.total=}")
    print(f"{hand_1=} {hand_1.total=}")
    print(f"Cheating: {b=}")
    print(board)

    board = play_tile(hand_0, 3, board)
    board = play_tile(hand_1, 4, board)
    ## Randomly draw all tiles
    # for i in range(0,36):
    #    t = b.draw_random()
    #    print(f'Drew: {t!r}')
    #    print(f'Boneyard: {b!r}')
