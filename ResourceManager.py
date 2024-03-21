#Manages all the smaller parts of the game in one larger place.
#You will typically only need one of these for the whole game.
import pygame as Pg
import PlayerInput as Pin

class MainResourceManager:

    #private variables, only meant to be used on the inside of this object
    pauseGamePlay = False
    

    def __init__(self) -> None:
        #Single instance objects
        self.mainGameKeys = Pin.AllKeyStates()

    def TickEverything(self) -> None:
        self.mainGameKeys.TickAllKeys()