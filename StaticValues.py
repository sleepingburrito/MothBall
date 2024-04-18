#Holds the static values and magic numbers used during the game. These values should never change during run time.
import math
import os
from enum import IntEnum
from enum import Enum
from enum import auto


#app info
#======================
#Moth Ball
#Started: 3/18/2024

#--glossary--
# GU - Game Units spacial. 1 game unit is the smallest whole unit.
# Tick - Is the smallest amount of time unit in the game. Time length amount depends on tick rate.

#======================
#build settings
#======================
GAME_NAME = "Moth Ball"
GAME_VERSION = "0.0.0"
GAME_DEBUG = True


#======================
#game units
#======================

#--spacial--
GU_ROOM_X = 0
GU_ROOM_Y = 0
GU_ROOM_WIDTH = 960
GU_ROOM_HEIGHT = 540
GU_WIDTH_HALF = GU_ROOM_WIDTH / 2
GU_HEIGHT_HALF = GU_ROOM_HEIGHT / 2

#--temporal--
TICK_RATE = 60 #refresh rate
MILLISECONDS_IN_SECOND = 1000
MILLISECONDS_IN_TICK = MILLISECONDS_IN_SECOND / TICK_RATE
TICKS_IN_MILLISECOND = TICK_RATE / MILLISECONDS_IN_SECOND
#timer
TIMER_MAX_VALUE_MILLISECONDS = MILLISECONDS_IN_SECOND * 60 * 60 #1 hour
TIMER_MAX_TICKS = math.trunc(TIMER_MAX_VALUE_MILLISECONDS * TICKS_IN_MILLISECOND) #max value a timer can be


#======================
#miscellaneous
#======================

#--ect--
IS_NON = -1 #Universal for no value.

class DIRECTION(IntEnum):
    UP = math.radians(180) #aka: top / y
    DOWN = 0 #aka: bottom
    LEFT = math.radians(270) #aka: x
    RIGHT = math.radians(90)
    DOWN_RIGHT = math.radians(45)
    DOWN_LEFT = math.radians(315)
    UP_RIGHT = math.radians(135)
    UP_LEFT = math.radians(225)
    

#--math--


#======================
#physics
#======================

#--speed/velocity--
#--If amount is hit in a single tick it will be limited to the values below. Based off the objects magnitude.
ACCELERATION_MAX = 8
VELOCITY_MAX = 16

#--friction--
#Values are in per 1 millisecond, always postive values.
#How much you want it to go down divided by the time in a tick. Example: Only want to take 0.01% away, so 0.01/MILLISECONDS_IN_TICK = ending value.
FRICTION_AIR_PERCENTAGE = 1 - (MILLISECONDS_IN_TICK * 0.00025) 
FRICTION_GROUND_PERCENTAGE = 1 - (MILLISECONDS_IN_TICK * 0.0018)

#--etc--
GRAVITY_ACCELERATION = MILLISECONDS_IN_TICK * 0.01


#======================
#player
#======================
class PLAYER_ID(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    #Should always be numerical starting from zero counting up with no gaps.
    ONE = auto()
    TWO = auto()

#--timing--
class PLAYER_TIMER_ID(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    #index into timer array
    PLACEHOLDER = auto()

#timer amounts - amount are in milliseconds
PLAYER_TIMER_PLACEHOLDER = 0

#--etc--
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 64
PLAYER_MAX_HP = 100


#input
#======================
class INPUT_ID(IntEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    START = auto()
    BACK = auto()
    ACTION = auto()
    JUMP = auto()
    PLACE_HOLDER1 = auto()
    PLACE_HOLDER2 = auto()
    PLACE_HOLDER3 = auto()
    PLACE_HOLDER4 = auto()
    PLACE_HOLDER5 = auto()
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


#maps
#======================



#graphics
#======================
SCREEN_WIDTH = GU_ROOM_WIDTH
SCREEN_HEIGTH = GU_ROOM_HEIGHT

DEBUG_BOX_COLOR = "red"
DEBUG_BOX_WIDTH = 1
DEBUG_SHADOW_COLOR = "blue"

DEFAULT_BG_COLOR = "black"