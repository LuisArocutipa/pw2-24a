from interpreter import draw
from chessPictures import *

draw(square.join(square.negative()).horizontalRepeat(4).up(square.negative().join(square).horizontalRepeat(4)).verticalRepeat(2))