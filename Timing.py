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


#fps timer
#================
class FPStimer:

   def __init__(self) -> None:
      self.ResetAll()

   def ResetAll(self) -> None:
      self._fpsTimer = 0
      self._fpsCount = 0
      self._fpsLast = 0

   #input: give how long the app has been running in ms.
   def UpdateTimePassedMs(self, timeRunningMs: int) -> int:
      if ( abs(timeRunningMs - self._fpsTimer) >= 1_000 ):
         self._fpsTimer = timeRunningMs
         self._fpsLast = self._fpsCount
         self._fpsCount = 0
      self._fpsCount += 1

   def GetFpsInt(self) -> int:
      return self._fpsLast
      
   def GetFpsStr(self) -> int:
      return str(self._fpsLast)


#timers
#================
class Timer:

   def __init__(self, lengthInMs: float) -> None:
      self.Set(lengthInMs)

   def TimeLimit(timeInTicks: int) -> int:
      return Tools.ClampValue(timeInTicks, 0, Sv.TIMER_MAX_TICKS)

   def Set(self, lengthInMs: float) -> None:
      self.ResetAllValues()
      self._timerEndTicks = self.TimeLimit(MillisecondsToTicks(lengthInMs))

   #reset start and end values to zero
   def ResetAllValues(self) -> None:
      self._timerEndTicks = 0
      self._timerStateTicks = 0

   def Reset(self) -> None:
      self._timerStateTicks = 0

   #Set the timer to the end time.
   def EndNow(self) -> None:
      self._timerStateTicks = self._timerEndTicks

   #True if the timer is passed, false if not.
   def IsDone(self) -> bool:
      return self._timerStateTicks >= self._timerEndTicks

   #Run each tick to update the timer.
   def Tick(self) -> None:
      self._timerStateTicks += 1 if self._timerStateTicks < Sv.TIMER_MAX_TICKS else 0

   def GetMillisecondsPassed(self) -> float:
      return TicksToMilliseconds(self._timerStateTicks)

   #Return range 0.0 - 1.0+, 0 is not started, 1+ is done.
   #1.0 or more is considered done.
   def PercentageCompleted(self) -> float:
      if self._timerEndTicks == 0:
         return 1
      else:
         return self._timerStateTicks / self._timerEndTicks