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
        self._right:float = self._x + self._width
        self._bottom:float = self._y + self._height

        self._xMin = Sv.GU_ROOM_X
        self._yMin = Sv.GU_ROOM_Y
        self._xMax = Sv.GU_ROOM_WIDTH
        self._yMax = Sv.GU_ROOM_HEIGHT

        self.x = self._x
        self.y = self._y
        self.width = self._width
        self.height = self._height

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
        #is in ticks
        self._wallTimers:dict[Sv.DIRECTION, int] = { Sv.DIRECTION.LEFT: 0, Sv.DIRECTION.UP: 0, Sv.DIRECTION.RIGHT: 0, Sv.DIRECTION.DOWN: 0,  }

    #end of ResetAll(self) 
    

    #x, y, width, height, top, bottom, left, right
    #x axis
    @property #x
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, input: float):
        self._x = self.LimitXaxis(input)
        self._right = self.x + self.width
        self.UpdateSelfAABB()
    @property #x center
    def xCenter(self) -> float:
        return self.x + self.width / 2
    @xCenter.setter
    def xCenter(self, input: float):
        self.x = input - self.width / 2
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
    @property #lmits (min x, max x)
    def xMinMax(self) -> float:
        return (self._xMin, self._xMax)
    @xMinMax.setter
    def xMinMax(self, input: float):
        self._xMin = Tool.ClampValue(input[0], Sv.GU_ROOM_X, Sv.GU_ROOM_WIDTH)
        self._xMax = Tool.ClampValue(input[1], Sv.GU_ROOM_X, Sv.GU_ROOM_WIDTH)


    #y axis
    @property #y
    def y(self) -> float:
        return self._y
    @y.setter
    def y(self, input: float):
        self._y = self.LimitYaxis(input)
        self._bottom = self.y + self.height
        self.UpdateSelfAABB()
    @property #y center
    def yCenter(self) -> float:
        return self.y + self.height / 2
    @yCenter.setter
    def yCenter(self, input: float):
        self.y = input - self.height / 2
    @property #top
    def top(self) -> float:
        return self.y
    @top.setter
    def top(self, input: float):
        self.y = input
        self.UpdateSelfAABB()
    @property #height
    def height(self) -> float:
        return self._height
    @height.setter
    def height(self, input: float):
        self._height = input
        self._bottom = self.y + self.height
        self.UpdateSelfAABB()
    @property #bottom
    def bottom(self) -> float:
        return self._bottom
    @bottom.setter
    def bottom(self, input: float):
        self.y = input - self.height
        self.UpdateSelfAABB()
    @property #lmits (min y, max y)
    def yMinMax(self) -> float:
        return (self._yMin, self._yMax)
    @yMinMax.setter
    def yMinMax(self, input: float):
        self._yMin = Tool.ClampValue(input[0], Sv.GU_ROOM_Y, Sv.GU_ROOM_HEIGHT)
        self._yMax = Tool.ClampValue(input[1], Sv.GU_ROOM_Y, Sv.GU_ROOM_HEIGHT)

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

    #returns tuple in SDL box format for drawing
    def GetPyGamesSdlBoxXYWH(self) -> tuple[int, int, int, int]:
        return  [math.trunc(self.x), math.trunc(self.y), math.trunc(self.width), math.trunc(self.height)]

    #Limit helpers: put in x/y and it will return x/y clamped to its min and max value set
    def LimitXaxis(self, inputX: float) -> float:
        return Tool.ClampValue(inputX, self._xMin, self._xMax)

    def LimitYaxis(self, inputX: float) -> float:
        return Tool.ClampValue(inputX, self._yMin, self._yMax)

    #checkpoint
    @property #x checkpoint
    def xCheckpoint(self) -> float:
        return self._xCheckpoint
    @xCheckpoint.setter
    def xCheckpoint(self, input: float):
        self._xCheckpoint = self.LimitXaxis(input)
    @property #y checkpoint
    def yCheckpoint(self) -> float:
        return self._yCheckpoint
    @yCheckpoint.setter
    def yCheckpoint(self, input: float):
        self._yCheckpoint = self.LimitYaxis(input)


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
        self._xVelocity = Tool.RoundToZero(Tool.ClampValue(input, -Sv.VELOCITY_MAX, Sv.VELOCITY_MAX), Sv.VELOCTIY_MIN)
    @property #y velocity
    def yVelocity(self) -> float:
        return self._yVelocity
    @yVelocity.setter
    def yVelocity(self, input: float):
        self._yVelocity = Tool.RoundToZero(Tool.ClampValue(input, -Sv.VELOCITY_MAX, Sv.VELOCITY_MAX), Sv.VELOCTIY_MIN)

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

    def SetVelocityRelativeMultiplyXYMagnitude(self, xy: tuple[float,float], magnitudeMult: float) -> None:
        self.xVelocity *= xy[0]
        self.yVelocity *= xy[1]
        self.velocityMagnitude = self.velocityMagnitude * magnitudeMult

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


    #==physics==

    def _WallPositionCollisionHelper(self, currentPosition: float, isTouchinWall: bool, positionIfInWall: float, directionTimer: Sv.DIRECTION) -> float:
        #meant to help physics with walls
        #returns what the postion should be at
        #also sets the wall timers
        timerAddValue: int = 0
        if isTouchinWall:
            #in/on wall
            currentPosition = positionIfInWall
            timerAddValue = 1
        else:
            #not on wall
            timerAddValue = -1
        #reset the wall timer if wall state changes
        if Tool.CopySign(self._wallTimers[directionTimer]) != timerAddValue:
            self._wallTimers[directionTimer] = 0
        #add what state you are in now
        self._wallTimers[directionTimer] += timerAddValue
        #return the new postion
        return currentPosition
    
    def _WallVelocityCollisionHelper(self, velocity: float, isHeadingToWall: bool, timerWallValue: int) -> float:
        #meant to help physics with walls
        #returns what the Velocity should be at
        if isHeadingToWall and timerWallValue > 0:
            velocity = 0
        return velocity

    def TickPhysics(self) -> None:
        #Acceleration
        self.SetVelocityRelativeAddXY((self.xAcceleration, self.yAcceleration))
        self.ZeroOutAcceleration()

        #velocity
        #Friction
        self.velocityMagnitude = self.velocityMagnitude * (Sv.FRICTION_GROUND_PERCENTAGE if self._wallTimers[Sv.DIRECTION.DOWN] >= 0 else Sv.FRICTION_AIR_PERCENTAGE)

        #x/y
        self.SetXYrelative(self.xyVelocity)

        #walls
        self.x = self._WallPositionCollisionHelper(self.x, self.x <= self._xMin, self._xMin, Sv.DIRECTION.LEFT)
        self.right = self._WallPositionCollisionHelper(self.right, self.right >= self._xMax, self._xMax, Sv.DIRECTION.RIGHT)
        self.y = self._WallPositionCollisionHelper(self.y, self.y <= self._yMin, self._yMin, Sv.DIRECTION.UP)
        self.bottom = self._WallPositionCollisionHelper(self.bottom, self.bottom >= self._yMax, self._yMax, Sv.DIRECTION.DOWN)

        #wall and velocity
        self.xVelocity = self._WallVelocityCollisionHelper(self.xVelocity, self.xVelocity < 0, self._wallTimers[Sv.DIRECTION.LEFT])
        self.xVelocity = self._WallVelocityCollisionHelper(self.xVelocity, self.xVelocity > 0, self._wallTimers[Sv.DIRECTION.RIGHT])
        self.yVelocity = self._WallVelocityCollisionHelper(self.yVelocity, self.yVelocity < 0, self._wallTimers[Sv.DIRECTION.UP])
        self.yVelocity = self._WallVelocityCollisionHelper(self.yVelocity, self.yVelocity > 0, self._wallTimers[Sv.DIRECTION.DOWN])


    #overlap
    def CheckBoxOverlap(self, boxToCheckAABB: tuple[int,int,int,int]) -> bool:
        return Tool.BoxIsOverlap(self.boxAABB, boxToCheckAABB)

    def CheckPointOverlap(self, pointToCheckXY: tuple[int, int]) -> bool:
        return Tool.PointInBox(pointToCheckXY, self.boxAABB)

    #debug
    def DebugDrawBox(self, drawToSurface: pygame.surface.SurfaceType) -> None:
        if Sv.GAME_DEBUG:
            pygame.draw.rect(drawToSurface, Sv.DEBUG_BOX_COLOR, self.GetPyGamesSdlBoxXYWH(), width = Sv.DEBUG_BOX_WIDTH)
