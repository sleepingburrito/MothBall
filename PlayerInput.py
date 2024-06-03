#Handles input from the player
import pygame as Pg
import StaticValues as Sv
import Timing as Ti
import Tools

#Glossary
#key - any type of input a player can do. 

#Keeps track of a single key state. This object is mostly meant to only be used in here for the AllKeyStates class
class KeyState:
    
    #inputId, what key it will monitor
    def __init__(self, inputId: Sv.INPUT_ID) -> None:
        self.FullReset()
        self.SetKeyId(inputId)

    def FullReset(self) -> None:
        self._inputTickState = 0
        self.inputId = Sv.IS_NON

    def TimerReset(self) -> None:
        self._inputTickState = 0

    def SetKeyId(self, newInputId: Sv.INPUT_ID) -> None:
        if newInputId in Sv.INPUT_ID:
            self.inputId = newInputId
        else:
            raise Exception("unknown input id")

    #isInputActive: Provide the state of the key, if its down give true, else false.
    #This is meant to be updated with each game tick.
    def Tick(self, isInputActive: bool) -> None:
        if isInputActive == True:
            self._inputTickState = max(1, self._inputTickState + 1) #reset key timer and add one to it
        elif isInputActive == False:
            self._inputTickState = min(0, self._inputTickState - 1)
        else:
            raise Exception("unknown input state")
        #keep in timer range
        self._inputTickState = Ti.KeepTicksInRange(self._inputTickState)

    #Returns true if the key is down.
    def IsKeyActive(self) -> bool:
        return self._inputTickState > 0
    
    #How long the key has been down or up in milliseconds. Positive is down, negative is up.
    def KeyTime(self) -> float:
        return Ti.TicksToMilliseconds(self._inputTickState)


#Keeps track of all keys states. Will most likely only need one of these for the whole game.
class AllKeyStates:

    #private read and write, public read only
    KeyIn: list[KeyState] = []

    def __init__(self) -> None:
        print("Initializing AllKeyStates")
        self.KeyIn.clear()
        for playerId in Sv.PLAYER_ID:
            #Make list list for each player to store their input
            self.KeyIn.append([]) 
            for inputType in Sv.INPUT_ID:
                #make a KeyState for each key
                self.KeyIn[playerId.value].append(KeyState(inputType.value))

    #Updates key states, call once per tick.
    def TickAllKeys(self) -> None:
        #test/todo: as of now keymappings are hard coded
        
        #poll keys pygames
        tmpKeys = Pg.key.get_pressed()

        #update keystate based off polled keys
        for playerId in Sv.PLAYER_ID:
            for inputType in Sv.INPUT_ID:
                #tmpPlayerId = playerId.value #test as of now both players share the same keys
                keydown = False
                #key mapping
                match inputType.value:
                    case Sv.INPUT_ID.UP:
                        keydown = tmpKeys[Pg.K_w]
                    case Sv.INPUT_ID.DOWN:
                        keydown = tmpKeys[Pg.K_s]
                    case Sv.INPUT_ID.LEFT:
                        keydown = tmpKeys[Pg.K_a]
                    case Sv.INPUT_ID.RIGHT:
                        keydown = tmpKeys[Pg.K_d]
                    case Sv.INPUT_ID.JUMP:
                        keydown = tmpKeys[Pg.K_SPACE]
                #update key input
                self.KeyIn[playerId.value][inputType.value].Tick(keydown)    