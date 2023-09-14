from typing import Tuple

NodeId = int
Coord = int


def encode_node_id(row: Coord, col: Coord) -> NodeId:
    hi_row = row << 16
    return hi_row | col


def decode_node_id(node_id: NodeId) -> Tuple[Coord, Coord]:
    HI_MASK = 0xFFFF0000
    row = (node_id & HI_MASK) >> 16
    col = node_id & ~HI_MASK
    return row, col
