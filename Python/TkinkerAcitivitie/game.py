from tkinter import *
from ship import *

# Campos:
# root: Tkinter
# gameWidth, gameHeight: num, num
# ship: Ship
class Game:
    # Constructor
    def __init__(self, gameWidth, gameHeight):
        self.root = Tk()
        self.gameWidth = gameWidth
        self.gameHeight = gameHeight
        self.gameWindow()

        self.ship = Ship(self.canvas, x=self.gameWidth / 2,y=self.gameHeight / 2, width=50, height=50, turnspeed=10, acceleration=5)
        self.root.bind('<Left>', self.ship.rotate)
        self.root.bind('<Right>', self.ship.rotate)
        self.root.bind('<Up>', self.ship.accel)
        self.root.bind('<Down>', self.ship.accel)

        self.root.mainloop()

    # gameWindow: None -> None
    # Crea una ventana con Tkinter utilizando los datos del objeto.
    def gameWindow(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)

        self.canvas = Canvas(self.frame,width=self.gameWidth, height=self.gameHeight, bg="black", takefocus=1)
        self.canvas.pack(fill=BOTH, expand=YES)     

asteroids = Game(600,600)
