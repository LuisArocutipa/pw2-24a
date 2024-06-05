from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = []
    for value in self:
        inv = ""
        for x in value:
            inv = x + inv
        vertical.append(inv)
    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = []
    for value in self:
        horizontal.insert(0, value)
    return Picture(horizontal)

  def negative(self):
    negative = []
    for value in self.img:
        new = ""
        for x in value:
          new += self._invColor(x)
        negative.append(new)
    return Picture(negative)

  def join(self, p):
    joinAr = []
    for value in range(len(self.img)):
      joinAr.append(self.img[value] + p.img[value])
    return Picture(joinAr)

  def up(self, p):
    upAr = self.img + p.img
    return Picture(upAr)

  def under(self, p):
    underAr = []
    for value in range(len(self.img)):
      new = ""
      for x in range(len(self.img)):
        if p.img[value][x] == " ":
          new += self.img[value][x]
        else:
          new += p.img[value][x]
      underAr.append(new)
    return Picture(underAr)
  
  def horizontalRepeat(self, n):
    horizontalAr = []
    for value in self.img:
      horizontalAr.append(value*n)
    return Picture(horizontalAr)

  def verticalRepeat(self, n):
    verticalAr = self.img*n
    return Picture(verticalAr)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
