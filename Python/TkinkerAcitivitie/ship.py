import math

# Campos:
# _d: Dict
# canvas: canvas
# width, height: num, num
# speed, turnspeed, acceleration: num, num, num
# (x0, y0), (x1, y1), (x2, y2): (num, num), (num, num), (num, num)
# (x, y): (num, num)
# ship: 
class Ship:

    # centroid: None -> num, num
    # Calcula la posición del punto medio de la figura
    def centroid(self):
        return 1 / 3 * (self.x0 + self.x1 + self.x2), 1 / 3 * (self.y0 + self.y1 + self.y2)

    # Constructor
    def __init__(self, canvas, x, y, width, height, turnspeed, acceleration=1):
        self._d = {'Up':1, 'Down':-1, 'Left':1, 'Right':-1}

        self.canvas = canvas
        self.width = width
        self.height = height
        self.speed = 0
        self.turnspeed = turnspeed
        self.acceleration = acceleration

        self.x0, self.y0 = x, y

        self.bearing = -math.pi / 2

        self.x1 = self.x0 + self.width / 2
        self.y1 = self.y0 - self.height

        self.x2 = self.x0 + self.width
        self.y2 = self.y0

        self.x, self.y = self.centroid()

        self.ship = self.canvas.create_polygon((self.x0, self.y0, self.x1, self.y1, self.x2, self.y2), outline="white", width=3)

    # changeCoords: None -> None
    # Actualiza las coordenadas de la figura ship
    def changeCoords(self):
        self.canvas.coords(self.ship,self.x0, self.y0, self.x1, self.y1, self.x2, self.y2)

    # rotate: event -> None
    # Si se produce un evento que utilice esta función, rota la figura ship
    def rotate(self, event=None):
        t = self._d[event.keysym] * self.turnspeed * math.pi / 180 # the trig functions generally take radians as their arguments rather than degrees; pi/180 radians is equal to 1 degree

        self.bearing -= t

        # _rot: num, num -> num, num
        # Calcula la posición del vector tras rotarse
        def _rot(x, y):
            #note: the rotation is done in the opposite fashion from for a right-handed coordinate system due to the left-handedness of computer coordinates
            x -= self.x
            y -= self.y
            _x = x * math.cos(t) + y * math.sin(t)
            _y = -x * math.sin(t) + y * math.cos(t)
            return _x + self.x, _y + self.y

        self.x0, self.y0 = _rot(self.x0, self.y0)
        self.x1, self.y1 = _rot(self.x1, self.y1)
        self.x2, self.y2 = _rot(self.x2, self.y2)
        self.x, self.y = self.centroid()

        self.changeCoords()

    # accel: event -> None
    # Si se produce un evento que utilice esta función, mueve la posición de la figura ship
    def accel(self, event=None):
        mh = int(self.canvas['height'])
        mw = int(self.canvas['width'])
        self.speed += self.acceleration * self._d[event.keysym]

        self.x0 += self.speed * math.cos(self.bearing)
        self.x1 += self.speed * math.cos(self.bearing)
        self.x2 += self.speed * math.cos(self.bearing)

        self.y0 += self.speed * math.sin(self.bearing)
        self.y1 += self.speed * math.sin(self.bearing)
        self.y2 += self.speed * math.sin(self.bearing)

        self.x, self.y = self.centroid()

        if self.y < - self.height / 2:
            self.y0 += mh
            self.y1 += mh
            self.y2 += mh
        elif self.y > mh + self.height / 2:
            self.y0 += mh
            self.y1 += mh
            self.y2 += mh

        if self.x < -self.width / 2:
            self.x0 += mw
            self.x1 += mw
            self.x2 += mw
        elif self.x > mw + self.width / 2:
            self.x0 -= mw
            self.x1 -= mw
            self.x2 -= mw
            
        self.x, self.y = self.centroid()

        self.changeCoords()