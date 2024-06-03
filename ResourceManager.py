#Manages all the smaller parts of the game in one larger place.
#You will typically only need one of these for the whole game.
import pygame as Pg
import PlayerInput as Pin
import Timing as Tim

class MainResourceManager:

    #private variables, only meant to be used on the inside of this object
    pauseGamePlay = False
    

    def __init__(self) -> None:
        #Single instance objects
        print("Initializing MainResourceManager")
        self.mainGameKeys = Pin.AllKeyStates()
        self.masterClock = Tim.MasterClock(0)


    def TickEverything(self) -> None:
        self.mainGameKeys.TickAllKeys()
        self.masterClock.TickMasterClock()