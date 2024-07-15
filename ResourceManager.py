#Manages all the smaller parts of the game in one larger place.
#You will typically only need one of these for the whole game.
import pygame as Pg
import PlayerInput as Pin
import Timing as Tim
import Physics as Phy
import DrawGraphics as Dg
import StaticValues as Sv


class MainResourceManager:

    #private variables, only meant to be used on the inside of this object
    pauseGamePlay = False
    

    def __init__(self) -> None:
        #Single instance objects
        print("Initializing MainResourceManager")
        self.mainGameKeys = Pin.AllKeyStates()
        self.masterClock = Tim.MasterClock(0)
        
        #players
        for players in Sv.PLAYER_ID:
            pass
        self.players = []

        #etc
        self.fpsCounterText = Dg.TextHelper(Sv.DEBUG_FPS_X, Sv.DEBUG_FPS_Y, "", Sv.DEBUG_FPS_SIZE, None, Sv.DEBUG_BOX_COLOR)
        self.fpsTimer = Tim.FPStimer()

        #--test--


    #end of init
    #====================


    def TickEverything(self) -> None:
        #etc
        self.mainGameKeys.TickAllKeys()
        self.masterClock.TickMasterClock()

        #fps display
        self.fpsTimer.UpdateTimePassedMs(Pg.time.get_ticks())
        self.fpsCounterText.text = self.fpsTimer.GetFpsStr()


        #--test--
        

    #end of TickEverything
    #====================


    def TickDrawEverything(self, drawToSurface: Pg.surface.SurfaceType) -> None:
        
        #--etc--
        self.fpsCounterText.DrawTextSurface(drawToSurface)

        #--test--


    #end of TickDrawEverything
    #====================