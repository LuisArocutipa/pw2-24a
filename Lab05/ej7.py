from interpreter import draw
from chessPictures import *

draw(square.under(rock.negative()).join(square.negative().under(knight.negative())).join(square.under(bishop.negative())).join(square.negative().under(queen.negative()))
    .join(square.under(king.negative())).join(square.negative().under(bishop.negative())).join(square.under(knight.negative())).join(square.negative().under(rock.negative()))
    .up(square.negative().under(pawn.negative()).join(square.under(pawn.negative())).horizontalRepeat(4))
    .up(square.join(square.negative()).horizontalRepeat(4).up(square.negative().join(square).horizontalRepeat(4)).verticalRepeat(2))
    .up(square.under(pawn).join(square.negative().under(pawn)).horizontalRepeat(4))
    .up(square.negative().under(rock).join(square.under(knight)).join(square.negative().under(bishop)).join(square.under(queen))
    .join(square.negative().under(king)).join(square.under(bishop)).join(square.negative().under(knight)).join(square.under(rock))))