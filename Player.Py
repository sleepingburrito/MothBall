#main player object
import pygame as Pg
import PlayerInput as Pin
import Timing as Tim
import Physics as Phy
import DrawGraphics as Dg
import StaticValues as Sv

class Player:
    
    def ResetAll(self) -> None:
        #players physics box
        self._pbox = Phy.box()
        self._pbox.x = Sv.PLAYER_DEFAULT_X
        self._pbox.y = Sv.PLAYER_DEFAULT_Y
        self._pbox.width = Sv.PLAYER_WIDTH
        self._pbox.height = Sv.PLAYER_HEIGHT
        
    #end of ResetAll
    #=========================
    

    def __init__(self, playerId: Sv.PLAYER_ID) -> None:
        print("Initializing player ", playerId)
        self._playerId = playerId
        self.ResetAll()

        #testing


    #end of init
    #=====================