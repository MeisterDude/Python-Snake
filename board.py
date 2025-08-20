
from constants import SIZE_SQUARE


def board_to_screen(pos):
    # converts board position to screen position (upper left corner of square)
    return (pos[0] * (SIZE_SQUARE + 1)) +1, (pos[1] * (SIZE_SQUARE + 1)) +1