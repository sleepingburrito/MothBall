#main rectangle tools and physics
import Tools as Tool
import StaticValues as Sv
import pygame




class box:

    def __init__(self) -> None:
        self.ResetAll()

    def ResetAll(self) -> None:
        #locations
        self.x = 0
        self.y = 0
        self.width = 1
        self.height = 1

    

    #x, y, width, heigth, top, bottom, left, right
    @property #X
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, input: float):
        self._x = Tool.ClampValue(input, Sv.GU_ROOM_X, Sv.GU_ROOM_WIDTH)
        self._right = self._x + self.width
    @property #left
    def left(self) -> float:
        return self.x
    @left.setter
    def left(self, input: float):
        self.x = input
    @property #width
    def width(self) -> float:
        return self._width
    @width.setter
    def width(self, input: float):
        self._width = input
        self._right = self._x + self.width
    @property #rigth
    def rigth(self) -> float:
        return self._right
    @rigth.setter
    def right(self, input: float):
        self.x = self.x - self.width


    @property
    def y(self) -> float:
        return self._y
    @x.setter
    def y(self, input: float):
        self._y = Tool.ClampValue(input, Sv.GU_ROOM_Y, Sv.GU_ROOM_HEIGHT)

    @property
    def top(self) -> float:
        return self.y
    @top.setter
    def top(self, input: float):
        self.y = input


    def SetXrelative(self, x: float) -> None:
        self.x += x

    def SetYrelative(self, y: float) -> None:
        self.y += y