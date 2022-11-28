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
        self.AddButtons()

        self.root.mainloop()

    # gameWindow: None -> None
    # Crea una ventana con Tkinter utilizando los datos del objeto.
    def gameWindow(self):
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=YES)
        
        self.canvas = Canvas(self.frame,width=self.gameWidth, height=self.gameHeight-100, bg="black", takefocus=1)
        self.canvas.pack(fill=BOTH, expand=YES)     
        
        self.controls = Canvas(self.frame,width=self.gameWidth, height=100, bg="white",takefocus=5)
        self.controls.pack(fill=BOTH)
        
    def AddButtons(self):
        
        Button(self.controls, text='Left', width=10,height=1, bd='1', command=lambda: self.ship.rotate("Left")).place(x=14,y=40)
        Button(self.controls, text='Right', width=10,height=1, bd='1', command=lambda: self.ship.rotate("Right")).place(x=95,y=40)
        Button(self.controls, text='Up', width=10,height=1, bd='1', command=lambda: self.ship.accel("Up")).place(x=50,y=15)
        Button(self.controls, text='Down', width=10,height=1, bd='1', command=lambda: self.ship.accel("Down")).place(x=50,y=65)
        
        Button(self.controls, text='Color', width=6,height=2, bd='1', command=self.ship.changeColor).place(x=350,y=16)
        Button(self.controls, text='Big', width=10,height=1, bd='1', command=lambda: self.ship.changeSize("Big")).place(x=400,y=10)
        Button(self.controls, text='Small', width=10,height=1, bd='1', command=lambda: self.ship.changeSize("Small")).place(x=400,y=35)
        
        

asteroids = Game(600,600)
