from graphics import *

class PPAvatar:
  def __init__(self): #defines avatar and its center, initializes at the upper left corner and pointing upper left
    self.X = 115
    self.Y = 115

    self.align = "up left"
    self.body = Image(Point(self.X, self.Y), "upleft.png")


  def move_avatar(self, key, amount):
    if key == 'W': #moves up [amount] pixels
      self.body.move(0, -1*amount)
      self.Y -= amount
    elif key == 'A': #move left [amount] pix
      self.body.move(-1*amount, 0)
      self.X -= amount
    elif key == 'S': #move down [amount] pix
      self.body.move(0, amount)
      self.Y += amount
    elif key == 'D': #move right [amount] pix
      self.body.move(amount, 0)
      self.X += amount


  def flip(self, win, orientation):
    self.body.undraw()

    center = Point(self.X, self.Y)

    if orientation == 'vert': #mirrors over vertical

      if self.align == "up left":
        self.body = Image(center, 'upright.png')
        self.align = "up right"

      elif self.align == "up right":
        self.body = Image(center, 'upleft.png')
        self.align = "up left"
      
      elif self.align == "down left":
        self.body = Image(center, 'downright.png')
        self.align = "down right"
      
      elif self.align == "down right":
        self.body = Image(center, 'downleft.png')
        self.align = "down left"

    elif orientation == 'horiz': #mirrors over horizontal
      if self.align == "up left":
        self.body = Image(center, 'downleft.png')
        self.align = "down left"

      elif self.align == "up right":
        self.body = Image(center, 'downright.png')
        self.align = "down right"
      
      elif self.align == "down left":
        self.body = Image(center, 'upleft.png')
        self.align = "up left"
      
      elif self.align == "down right":
        self.body = Image(center, 'upright.png')
        self.align = "up right"

    self.body.draw(win)