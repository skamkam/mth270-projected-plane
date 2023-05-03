from graphics import *
from PPavatar import *

WIDTH = 400
HEIGHT = 400

win = GraphWin("Projective plane", WIDTH, HEIGHT)

def square_creation(): #creates projective plane
  rect = Rectangle(Point(50, 50), Point(350, 350))

  leftedge = Polygon(Point(50, 200), Point(60, 210), Point(40, 210))

  rightedge = Polygon(Point(350, 210), Point(340, 200), Point(360, 200))

  topedge = Line(Point(250, 50), Point(200, 50))
  topedge.setArrow('last')

  bottomedge = Line(Point(150, 350), Point(200, 350))
  bottomedge.setArrow('last')

  pp = [rect, leftedge, rightedge, topedge, bottomedge]
  for obj in pp: #draws objects to window
    obj.setWidth(3)
    obj.draw(win)


def main():
  square_creation()
  avatar = PPAvatar()
  avatar.body.draw(win) #draws the avatar to window

  win.getMouse()

  direction = ''
  while direction != 'Q':
    direction = win.checkKey().upper()
    avatar.move_avatar(direction, 5)
    
    difY = abs(avatar.Y - 200) * 2
    difX = abs(avatar.X - 200) * 2

    if avatar.X < 50: #passes left border
      avatar.flip(win, 'horiz') #mirrors over horizontal line
      avatar.move_avatar('D', 300)
      if avatar.Y < 200: #if above middle horiz line
        avatar.move_avatar('S', difY) #moves down by twice the difference between previous Y position and middle line
      elif avatar.Y > 200:
        avatar.move_avatar('W', difY)

    elif avatar.X > 350: #passes right border
      avatar.flip(win, 'horiz')
      avatar.move_avatar('A', 300)
      if avatar.Y < 200: #above middle line
        avatar.move_avatar('S', difY)
      elif avatar.Y > 200:
        avatar.move_avatar('W', difY)

    elif avatar.Y < 50: #passes top border
      avatar.flip(win, 'vert')
      avatar.move_avatar('S', 300)
      if avatar.X < 200: #left of middle vert line
        avatar.move_avatar('D', difX) #moves right by twice the difference between previous X pos and middle vertical line
      elif avatar.X > 200: #right of middle
        avatar.move_avatar('A', difX)

    elif avatar.Y > 350: #passes bottom border
      avatar.flip(win, 'vert')
      avatar.move_avatar('W', 300)
      if avatar.X < 200: #left of middle
        avatar.move_avatar('D', difX)
      elif avatar.X > 200: #right of middle
        avatar.move_avatar('A', difX)


if __name__ == '__main__':
  main() #calls main module