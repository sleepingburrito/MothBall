#Manages all the smaller parts of the game in one larger place.
#You will typically only need one of these for the whole game.
import pygame as Pg
import PlayerInput as Pin
import Timing as Tim
import Physics as Phy

class MainResourceManager:

    #private variables, only meant to be used on the inside of this object
    pauseGamePlay = False
    

    def __init__(self) -> None:
        #Single instance objects
        print("Initializing MainResourceManager")
        self.mainGameKeys = Pin.AllKeyStates()
        self.masterClock = Tim.MasterClock(0)
        
        #players
        self.players = [] #make sure to type hint that this is a list of player types

        #--test--
        self.testphy = Phy.box()
        self.testphy.x = 100
        self.testphy.y = 150
        self.testphy.width = 50
        self.testphy.height = 100


    def TickEverything(self) -> None:
        self.mainGameKeys.TickAllKeys()
        self.masterClock.TickMasterClock()

        #--test--
        self.testphy.TickPhysics()

    def TickDrawEverything(self, drawToSurface: Pg.surface.SurfaceType) -> None:
        
        #--test--
        self.testphy.DebugDrawBox(drawToSurface)