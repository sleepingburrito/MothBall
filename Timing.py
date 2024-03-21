#This holds timers and other timing tools.
import math
import StaticValues as Sv
import Tools

#time helpers
def MinutesToTicks(minutes: float) -> int:
  return math.trunc(minutes * 60 * Sv.MILLISECONDS_IN_SECOND * Sv.TICKS_IN_MILLISECOND)

def SecondsToTicks(seconds: float) -> int:
  return math.trunc(seconds * Sv.MILLISECONDS_IN_SECOND * Sv.TICKS_IN_MILLISECOND)

def MillisecondsToTicks(milliseconds: float) -> int:
  return math.trunc(milliseconds * Sv.TICKS_IN_MILLISECOND)

def TicksToMilliseconds(ticks: int) -> float:
   return ticks * Sv.MILLISECONDS_IN_TICK

def KeepTicksInRange(ticks: int) -> int:
  return Tools.ClampValue(ticks, -Sv.TIMER_MAX_TICKS, Sv.TIMER_MAX_TICKS)


#master clock
#================
#Meant to only have one per game. Helper if something just needs a constant upwards time source of ticks starting at 0 during game boot.
class MasterClock:
    
    #read and right internal, read only external.
    masterTickTimer = 0

    def __init__(self, StartingValue: int = 0) -> None:
        self.ResetMasterClock()
        self.masterTickTimer = StartingValue

    #Ticks - Set master clock to this time, only positive hole values.
    def SetMasterClock(self, ticks: int) -> None:
       if (ticks < 0):
          ticks = 0
       self.masterTickTimer = math.trunc(ticks)

    def ResetMasterClock(self) -> None:
       self.masterTickTimer = 0

    def TickMasterClock(self) -> None:
       self.masterTickTimer += 1

    def MasterClockToMs(self) -> float:
       return TicksToMilliseconds(self.masterTickTimer)