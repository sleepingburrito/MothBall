import pygame as Pg


class TextHelper:

   #pass None for file name to get default
   def __init__(self, x:int = 0, y:int = 0, startingText:str="", sizeFont:int = 20, filename:str = None, color:str="RED") -> None:
      self._pyGamesFont = Pg.font.Font(filename, size=sizeFont)
      self._text = startingText
      self._color = color
      self._x = x
      self._y = y

   @property
   def text(self) -> float:
      return self._text
   @text.setter
   def text(self, newText: float):
      self._text = newText

   @property
   def color(self) -> float:
      return self._color
   @color.setter
   def color(self, newColor: float):
      self._color = newColor

   @property
   def x(self) -> float:
      return self._x
   @x.setter
   def x(self, input: float):
      self._x = input

   @property
   def y(self) -> float:
      return self._y
   @y.setter
   def y(self, input: float):
      self._y = input


   def DrawTextSurface(self, drawToSurface: Pg.surface.SurfaceType) -> None:
      drawToSurface.blit(self._pyGamesFont.render(self.text, False, self.color), (self.x, self.y))
