#main player object
import pygame as Pg
import PlayerInput as Pin
import Timing as Tim
import Physics as Phy
import DrawGraphics as Dg
import StaticValues as Sv

class player:
    


    def __init__(self, playerId: Sv.PLAYER_ID, keyStates: Pin.AllKeyStates, drawToSurface: Pg.surface.SurfaceType) -> None:
        print("Initializing player ", playerId)
        self._playerId = playerId
        self.keys = keyStates
        self.surface = drawToSurface
        self.ResetAll()

        #testing


    #end of init
    #=====================

    def ResetAll(self) -> None:
        #resets everything to be like new
        #also holds all the variables
        
        #etc
        self.active = False #if false object will not be processed in any draw or tick steps
        self._RestAllKeys()

        #players physics box
        self._pbox = Phy.box()
        self._pbox.x = Sv.PLAYER_DEFAULT_X
        self._pbox.y = Sv.PLAYER_DEFAULT_Y
        self._pbox.width = Sv.PLAYER_WIDTH
        self._pbox.height = Sv.PLAYER_HEIGHT



    #end of ResetAll
    #=========================

    #controls
    def _RestAllKeys(self) -> None:
        #movement
        self.upKey = 0
        self.downKey = 0
        self.leftKey = 0
        self.rightKey = 0
        #diagonal
        self.upLeft = 0
        self.upRight = 0
        self.downLeft = 0
        self.downRight = 0
        #other actions
        self.jumpKey = 0

    def _UpdateKeys(self) -> None:
        #takes a snapshot of current key state if you are able to use keys
        self._RestAllKeys()

        if not self.IsStunned():
            #starting key states
            self.upKey = self.keys.KeyIn[self._playerId][Sv.INPUT_ID.UP].KeyTime()
            self.downKey = self.keys.KeyIn[self._playerId][Sv.INPUT_ID.DOWN].KeyTime() 
            self.leftKey = self.keys.KeyIn[self._playerId][Sv.INPUT_ID.LEFT].KeyTime()
            self.rightKey = self.keys.KeyIn[self._playerId][Sv.INPUT_ID.RIGHT].KeyTime()
            #d-pad like lockout
            if self.upKey > 0 and self.downKey > 0:
                self.upKey = 0
                self.downKey = 0
            if self.leftKey > 0 and self.rightKey > 0:
                self.leftKey = 0
                self.rightKey = 0
            #diagonal
            if self.upKey > 0:
                if self.rightKey > 0:
                    self.upRight = min(self.upKey, self.rightKey)
                elif self.leftKey > 0:
                    self.upLeft = min(self.upKey, self.leftKey)
            elif self.downKey > 0:
                if self.rightKey > 0:
                    self.downRight = min(self.downKey, self.rightKey)
                elif self.leftKey > 0:
                    self.downLeft = min(self.downKey, self.leftKey)
            #other actions
            self.jumpKey = self.keys.KeyIn[self._playerId][Sv.INPUT_ID.JUMP].KeyTime()
        #end of update key

    #controls end
    #=========================

    #=======ticks=========
    #tick helpers (internal use only)
    
    def StartTick(self) -> None:
        if not self.active:
            return
        
        self._UpdateKeys()
        
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
   
    #=======etc=======

    def IsStunned(self) -> bool:
        #stunned means the player can not use keys to interact
        return False #todo, add what can cause the player to be stunned

    #=======end etc=======


    def Draw(self) -> None:
        if not self.active:
            return
        
        if Sv.GAME_DEBUG:
            self._pbox.DebugDrawBox(self.surface)
    #end of end draw
    #=================