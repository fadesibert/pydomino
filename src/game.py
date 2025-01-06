from tile import Tile
from hand import Hand, Boneyard
from board import Board, Edge
from player import Player, HumanPlayer
from itertools import combinations_with_replacement
from exceptions import NoMovesError, InvalidMoveError

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
    if index <= -1:
        # Player chose to pass
        print("Turn was passed")
        board.turn_pass()
        return board

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


def turn_loop(player: Player, board: Board, yard: Boneyard) -> tuple[Player, Board]:
    print(f"{player.name=}")
    TURN_HALT = False
    while not TURN_HALT:
        edges = board.edges
        tile_idx = player.play(edges)
        try:
            if tile_idx == 99:
                raise NoMovesError
            board = play_tile(player.hand, tile_idx, board)
            TURN_HALT = True
        except NoMovesError:
            # No Moves - draw a tile
            print("No moves found and a NoMovesError handled was thrown")
            player.draw(yard)
    return (player, board)


def round_loop(player_1: Player, player_2: Player):
    ROUND_HALT = False
    b = setup_boneyard()
    board = Board()
    hand_0, hand_1 = setup_hands(b)
    player_1.new_hand(hand=hand_0)
    player_2.new_hand(hand=hand_1)

    while not ROUND_HALT:
        player_1, board = turn_loop(player_1, board, b)
        if player_1.domino or board.round_over:
            ROUND_HALT = True
        player_2, board = turn_loop(player_2, board, b)
        if player_2.domino or board.round_over:
            ROUND_HALT = True

    p1_remain = player_1.points_in_hand
    p2_remain = player_2.points_in_hand
    print(f"{p1_remain=} {p2_remain=}")
    if p1_remain == p2_remain:
        print("DRAW!")
    if p1_remain < p2_remain:
        player_1.score += p2_remain
        print(
            f"{player_1.name} wins - round score = {p2_remain}, running score = {player_1.score=}"
        )

    elif p1_remain > p2_remain:
        player_2.score += p1_remain
        print(
            f"{player_2.name} wins - round score = {p1_remain}, running score = {player_2.score=}"
        )


if __name__ == "__main__":
    p1 = HumanPlayer(name="Alice")
    p2 = HumanPlayer(name="Bob")
    round_loop(p1, p2)

    print(f"{p1.score=}")
    print(f"{p2.score=}")
