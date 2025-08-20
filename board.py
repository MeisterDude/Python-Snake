
from constants import SIZE_SQUARE


def board_to_screen(pos, size):
    # converts board position to screen position (upper left corner of square)
    return (pos[0] * (SIZE_SQUARE + 1)) + 1 + ((SIZE_SQUARE - size)) / 2, (pos[1] * (SIZE_SQUARE + 1)) + 1 + ((SIZE_SQUARE - size) / 2)