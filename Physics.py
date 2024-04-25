#main rectangle tools and physics
import Tools as Tool
import StaticValues as Sv
import pygame




class box:

    def __init__(self) -> None:
        self.ResetAll()

    def ResetAll(self) -> None:
        #locations
        self._x:float = 0
        self._y:float = 0
        self._width:float = 1
        self._height:float = 1

        self._xCheckpoint:float = 0
        self._yCheckpoint:float = 0

        #vectors
        self._xAcceleration:float = 0
        self._yAcceleration:float = 0

        #flags
        self.physics:bool = True
        self.collisionDetection:bool = True 
    #end of ResetAll(self) 
    

    #x, y, width, heigth, top, bottom, left, right
    #x axis
    @property #x
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, input: float):
        self._x = Tool.ClampValue(input, Sv.GU_ROOM_X, Sv.GU_ROOM_WIDTH)
        self._right = self.x + self.width
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
        self._right = self.x + self.width
    @property #rigth
    def rigth(self) -> float:
        return self._right
    @rigth.setter
    def right(self, input: float):
        self.x = input - self.width

    #y axis
    @property #y
    def y(self) -> float:
        return self._y
    @y.setter
    def y(self, input: float):
        self._y = Tool.ClampValue(input, Sv.GU_ROOM_Y, Sv.GU_ROOM_HEIGHT)
        self._bottom = self.y + self.height  
    @property #top
    def top(self) -> float:
        return self.y
    @top.setter
    def top(self, input: float):
        self.y = input
    @property #heigth
    def heigth(self) -> float:
        return self._heigth
    @heigth.setter
    def heigth(self, input: float):
        self._heigth = input
        self._bottom = self.y + self.heigth
    @property #bottom
    def bottom(self) -> float:
        return self._bottom
    @bottom.setter
    def bottom(self, input: float):
        self.y = input - self.height

    #axis functions
    def SetXYrelative(self, xy: tuple[float,float]) -> None:
        self.x += xy[0]
        self.y += xy[1]


    #checkpoint
    @property #x checkpoint
    def xCheckpoint(self) -> float:
        return self._xCheckpoint
    @xCheckpoint.setter
    def xCheckpoint(self, input: float):
        self._xCheckpoint = Tool.ClampValue(input, Sv.GU_ROOM_X, Sv.GU_ROOM_WIDTH)
    @property #y checkpoint
    def yCheckpoint(self) -> float:
        return self._yCheckpoint
    @yCheckpoint.setter
    def yCheckpoint(self, input: float):
        self._yCheckpoint = Tool.ClampValue(input, Sv.GU_ROOM_Y, Sv.GU_ROOM_HEIGHT)

    #todo make a checkpoint reset that will reset the players postions and reset their volcity etc
        
    #Acceleration
    @property #x Acceleration
    def xAcceleration(self) -> float:
        return self._xAcceleration
    @xAcceleration.setter
    def xAcceleration(self, input: float):
        self._xAcceleration = Tool.ClampValue(input, -Sv.ACCELERATION_MAX, Sv.ACCELERATION_MAX)
    @property #y Acceleration
    def yAcceleration(self) -> float:
        return self._yAcceleration
    @yCheckpoint.setter
    def yAcceleration(self, input: float):
        self._yAcceleration = Tool.ClampValue(input, -Sv.ACCELERATION_MAX, Sv.ACCELERATION_MAX)

    def SetAccelerationRelative(self, xy: tuple[float,float]) -> None:
        self.xAcceleration += xy[0]
        self.yAcceleration += xy[1]

    def SetAccelerationRelativeVector(self, AngleMagnitude: tuple[float,float]) -> None:
        tmpVec = Tool.VectorNew(AngleMagnitude[0], AngleMagnitude[1])
        self.SetAccelerationRelative(tmpVec[0], tmpVec[1])

    def ZeroOutAcceleration(self) -> None:
        self.xAcceleration = 0
        self.yAcceleration = 0
        
    def GetAccelerationTuple(self) -> tuple[float,float]:
        return (self.xAcceleration, self.yAcceleration)