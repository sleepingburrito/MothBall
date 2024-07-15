#main player object
import pygame as Pg
import PlayerInput as Pin
import Timing as Tim
import Physics as Phy
import DrawGraphics as Dg
import StaticValues as Sv

class player:
    


    def __init__(self, playerId: Sv.PLAYER_ID) -> None:
        print("Initializing player ", playerId)
        self._playerId = playerId
        self.ResetAll()

        #testing


    #end of init
    #=====================

    def ResetAll(self) -> None:
        #resets everything to be like new
        #also holds all the variables
        
        self.active = False #if false object will not be processed in any draw or tick steps

        #players physics box
        self._pbox = Phy.box()
        self._pbox.x = Sv.PLAYER_DEFAULT_X
        self._pbox.y = Sv.PLAYER_DEFAULT_Y
        self._pbox.width = Sv.PLAYER_WIDTH
        self._pbox.height = Sv.PLAYER_HEIGHT

    #end of ResetAll
    #=========================

    #=======ticks=========
    #tick helpers (internal use only)
    
    def StartTick(self) -> None:
        if not self.active:
            return
        
    #end of start tick
    #=================


    def Tick(self) -> None:
        if not self.active:
            return
        
    #end of tick
    #=================


    def EndTick(self) -> None:
        if not self.active:
            return
    #end of end tick
    #=================
    
    #=======end of ticks=========
   

    def Draw(self, drawToSurface: Pg.surface.SurfaceType) -> None:
        if not self.active:
            return
        
        if Sv.GAME_DEBUG:
            self._pbox.DebugDrawBox(drawToSurface)
    #end of end draw
    #=================