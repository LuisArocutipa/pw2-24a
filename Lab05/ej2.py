from interpreter import draw
from chessPictures import *

draw(knight.join(knight.negative()).up(knightVertical.negative().join(knightVertical)))