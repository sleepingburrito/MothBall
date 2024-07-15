#This is the starting point of the game, this is the first scrip to run. It initializes everything and runs it.
import pygame as Pg
import StaticValues as Sv
import ResourceManager as Rm
import DrawGraphics as Dg
import Timing as Time


#setup
#===============
print("Game: ", Sv.GAME_NAME, Sv.GAME_VERSION,"Starting Initialization.") 

#pygame setup
print("Setting up pygame")
Pg.init()
Pg.mixer.init()
PgScreenSurface = Pg.display.set_mode((Sv.SCREEN_WIDTH, Sv.SCREEN_HEIGTH))
PgClock = Pg.time.Clock()

#global variable setup
keepGameRunning = True
mainResourceManager = Rm.MainResourceManager()

#debug testing


#main game loop
#======================
print("starting main game loop")

while keepGameRunning:

    #--poll events, close game when user clicks X--
    for event in Pg.event.get():
        if event.type == Pg.QUIT:
            keepGameRunning = False


    #main game tick
    #======================
    mainResourceManager.TickEverything()

    #debug testing tick
    #=====================



    #main draw
    #======================
    #Clear Screen
    PgScreenSurface.fill(Sv.DEFAULT_BG_COLOR)

    #main draw
    mainResourceManager.TickDrawEverything(PgScreenSurface)



    #end draw
    Pg.display.flip() #Pygame flip() the display to put your work on screen
    PgClock.tick(Sv.TICK_RATE) #limit frame rate

#exit code
print("Game: ", Sv.GAME_NAME, Sv.GAME_VERSION,"Exit was successful.") 