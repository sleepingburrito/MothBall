#main rectangle tools and physics
import Tools as Tool
import StaticValues as Sv
import math
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

        #axis-aligned bounding box truncated to whole game units.
        self._AABBTrunc: tuple[int,int,int,int] = [self._x, self._y, self._x + self._width, self._y + self._height]

        #vectors
        self._xAcceleration:float = 0
        self._yAcceleration:float = 0

        self._xVelocity:float = 0
        self._yVelocity:float = 0

        #flags
        self.physics:bool = True
        self.collisionDetection:bool = True

        #timing
        #how long you have touched that wall
        #postive is touching and negative is not
        self._leftWallTimer:int = 0
        self._topWallTimer:int = 0
        self._rigthWallTimer:int = 0
        self._bottomWallTimer:int = 0

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
        self.UpdateSelfAABB()
    @property #left
    def left(self) -> float:
        return self.x
    @left.setter
    def left(self, input: float):
        self.x = input
        self.UpdateSelfAABB()
    @property #width
    def width(self) -> float:
        return self._width
    @width.setter
    def width(self, input: float):
        self._width = input
        self._right = self.x + self.width
        self.UpdateSelfAABB()
    @property #rigth
    def rigth(self) -> float:
        return self._right
    @rigth.setter
    def right(self, input: float):
        self.x = input - self.width
        self.UpdateSelfAABB()

    #y axis
    @property #y
    def y(self) -> float:
        return self._y
    @y.setter
    def y(self, input: float):
        self._y = Tool.ClampValue(input, Sv.GU_ROOM_Y, Sv.GU_ROOM_HEIGHT)
        self._bottom = self.y + self.height
        self.UpdateSelfAABB()
    @property #top
    def top(self) -> float:
        return self.y
    @top.setter
    def top(self, input: float):
        self.y = input
        self.UpdateSelfAABB()
    @property #heigth
    def heigth(self) -> float:
        return self._heigth
    @heigth.setter
    def heigth(self, input: float):
        self._heigth = input
        self._bottom = self.y + self.heigth
        self.UpdateSelfAABB()
    @property #bottom
    def bottom(self) -> float:
        return self._bottom
    @bottom.setter
    def bottom(self, input: float):
        self.y = input - self.height
        self.UpdateSelfAABB()

    #axis functions
    def SetXYrelative(self, xy: tuple[float,float]) -> None:
        self.x += xy[0]
        self.y += xy[1]

    #bounding box
    #update bounding box to own cords.
    def UpdateSelfAABB(self) -> None:
        self._AABBTrunc = [math.trunc(self.left), math.trunc(self.top), math.trunc(self.right), math.trunc(self.bottom)]

    @property
    def boxAABB(self) -> tuple[int, int, int, int]:
        return self._AABBTrunc
    @boxAABB.setter
    def boxAABB(self, boxNew: tuple[int, int, int, int]):
        self.left = boxNew[0]
        self.top = boxNew[1]
        self.rigth = boxNew[2]
        self.bottom = boxNew[3]
        self._AABBTrunc = boxNew


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
    @yAcceleration.setter
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
    
    
    #velocity
    @property #x velocity
    def xVelocity(self) -> float:
        return self._xVelocity
    @xVelocity.setter
    def xVelocity(self, input: float):
        self._xVelocity = Tool.ClampValue(input, -Sv.VELOCITY_MAX, Sv.VELOCITY_MAX)
    @property #y velocity
    def yVelocity(self) -> float:
        return self._yVelocity
    @yVelocity.setter
    def yVelocity(self, input: float):
        self._yVelocity = Tool.ClampValue(input, -Sv.VELOCITY_MAX, Sv.VELOCITY_MAX)

    @property #xy velocity
    def xyVelocity(self) -> tuple[float,float]:
        return (self.xVelocity, self.yVelocity)
    @xyVelocity.setter
    def xyVelocity(self, input: tuple[float,float]):
        self.xVelocity = input[0]
        self.yVelocity = input[1]

    @property #velocity magnitude
    def velocityMagnitude(self) -> float:
        return Tool.VectorMagnitude(self.xyVelocity)
    @velocityMagnitude.setter
    def velocityMagnitude(self, input: float):
        self.xyVelocity = Tool.VectorNew(self.velocityAngle, input)

    @property #velocity angle
    def velocityAngle(self) -> float:
        return Tool.VectorAngle(self.xyVelocity)
    @velocityAngle.setter
    def velocityAngle(self, input: float):
        self.xyVelocity = Tool.VectorNew(input, self.velocityMagnitude)

    def SetVelocityRelativeAddXY(self, xy: tuple[float,float]) -> None:
        self.xVelocity += xy[0]
        self.yVelocity += xy[1]

    def SetVelocityRelativeAddAngleMagnitude(self, angleMagnitude: tuple[float,float]) -> None:
        tmp = Tool.VectorNew(angleMagnitude[0], angleMagnitude[1])
        self.xVelocity += tmp[0]
        self.yVelocity += tmp[1]

    def SetVelocityRelativeMultiplyXY(self, xy: tuple[float,float]) -> None:
        self.xVelocity *= xy[0]
        self.yVelocity *= xy[1]

    def GetVelocityDirectionMoving(self, whichAxis: Sv.AXIS) -> Sv.DIRECTION:
        speed = self.xyVelocity[whichAxis.value]
        if speed < 0:
            return Sv.DIRECTION.RIGHT if Sv.AXIS.X == whichAxis else Sv.DIRECTION.UP
        elif speed > 0:
            return Sv.DIRECTION.LEFT if Sv.AXIS.X == whichAxis else Sv.DIRECTION.DOWN
        else: #if it is zero
            return Sv.DIRECTION.NON

    def ZeroOutVelocity(self) -> None:
        self._xVelocity = 0
        self._yVelocity = 0
