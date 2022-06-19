from colorama import Back, init

init(autoreset=True)
world = [[Back.LIGHTWHITE_EX + '    ' for i in range(32)] for j in range(21)] # matriz por comprension, representa
# 20x 30 y ponemos 32 para poner los numeros y 31- 1 y 21-1 nos da 30 y
# 20, 30 x 20
ESPACIONEGRO = Back.BLACK + '    ' # variables que usaremos mas tarde para determinar un pixel negro, azul y verde
PASTO = Back.GREEN + '    '
AGUA = Back.BLUE + '    '





def draw_worldempty():
    for i in range(len(world)):  # recorremos las filas de la matriz con len
        if i == 0:
            for j in range(len(world[i])):  # selecciona todos los elementos de esas fila
                world[i][j] = str(j)  # cada uno se convierte en un string
        for l in range(32):  # seleccionar a los primeros valores de cada fila, si l es 0 entonces vemos que es la
            # primera
            if l == 0:
                world[i][l] = str(i)  # i representa a todas las filas y l representa al primer elementos de cada
                # fila y entonces
                # seleccionamos a todos los primeros elementos de cada fila para convertirlos


def draw_world(): # seleccionamos las filas que queremos pintar y el numero de columnas que pintaremos, y cambiamos
    # los pixeles balncos según el color que corresponda
    # La parte negra
    for i in range(14, 21):
        for j in range(30):
            world[i][j + 1] = ESPACIONEGRO # j + 1 es para evitar que se pinten los numeros
            tierra = world[i][j]

    # la parte verde
    for i in range(13, 14):
        for j in range(30):
            world[i][j + 1] = PASTO
            pasto = world[i][j + 1] # j + 1 es para evitar que se pinten los numeros

        # La parte de agua
        for i in range(13, 18):
            for j in range(25, 28):
                world[i][j + 1] = AGUA
                lago = world[i][j + 1] # j + 1 es para evitar que se pinten los numeros
    # 1PARTE VERDE DEL PRIMER ARBOL
    world[6][5] = Back.GREEN + '    '
    # 2PARTE VERDE DEL PRIMER ARBOL
    world[7][4] = Back.GREEN + '    '
    world[7][5] = Back.GREEN + '    '
    world[7][6] = Back.GREEN + '    '
    # 3PARTE VERDE DEL PRIMER ARBOL
    world[8][3] = Back.GREEN + '    '
    world[8][4] = Back.GREEN + '    '
    world[8][5] = Back.GREEN + '    '
    world[8][6] = Back.GREEN + '    '
    world[8][7] = Back.GREEN + '    '
    # TALLO DEL PRIMER ARBOL
    world[9][5] = Back.RED + '    '
    world[10][5] = Back.RED + '    '
    world[11][5] = Back.RED + '    '
    world[12][5] = Back.RED + '    '

    # 1PARTE VERDE DEL SEGUNDO ARBOL
    world[6][11] = Back.GREEN + '    '
    # 2PARTE VERDE DEL SEGUNDO ARBOL
    world[7][10] = Back.GREEN + '    '
    world[7][11] = Back.GREEN + '    '
    world[7][12] = Back.GREEN + '    '
    # 3PARTE VERDE DEL SEGUNDO ARBOL
    world[8][9] = Back.GREEN + '    '
    world[8][10] = Back.GREEN + '    '
    world[8][11] = Back.GREEN + '    '
    world[8][12] = Back.GREEN + '    '
    world[8][13] = Back.GREEN + '    '
    # TALLO DEL SEGUNDO ARBOL
    world[9][11] = Back.RED + '    '
    world[10][11] = Back.RED + '    '
    world[11][11] = Back.RED + '    '
    world[12][11] = Back.RED + '    '

    # 1PARTE VERDE DEL TERCER ARBOL
    world[6][17] = Back.GREEN + '    '
    # 2PARTE VERDE DEL TERCER ARBOL
    world[7][16] = Back.GREEN + '    '
    world[7][17] = Back.GREEN + '    '
    world[7][18] = Back.GREEN + '    '
    # 3PARTE VERDE DEL TERCER ARBOL
    world[8][15] = Back.GREEN + '    '
    world[8][16] = Back.GREEN + '    '
    world[8][17] = Back.GREEN + '    '
    world[8][18] = Back.GREEN + '    '
    world[8][19] = Back.GREEN + '    '
    # TALLO DEL TERCER ARBOL
    world[9][17] = Back.RED + '    '
    world[10][17] = Back.RED + '    '
    world[11][17] = Back.RED + '    '
    world[12][17] = Back.RED + '    '

    # 1PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
    world[3][22] = Back.GREEN + '    '
    # 2PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
    world[4][21] = Back.GREEN + '    '
    world[4][22] = Back.GREEN + '    '
    world[4][23] = Back.GREEN + '    '
    # 3PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
    world[5][20] = Back.GREEN + '    '
    world[5][21] = Back.GREEN + '    '
    world[5][22] = Back.GREEN + '    '
    world[5][23] = Back.GREEN + '    '
    world[5][24] = Back.GREEN + '    '
    # 4PARTE VERDE DEL CUARTO ARBOL - ARBOL GRANDE
    world[6][19] = Back.GREEN + '    '
    world[6][20] = Back.GREEN + '    '
    world[6][21] = Back.GREEN + '    '
    world[6][22] = Back.GREEN + '    '
    world[6][23] = Back.GREEN + '    '
    world[6][24] = Back.GREEN + '    '
    world[6][25] = Back.GREEN + '    '
    # TALLO DEL CUARTO ARBOL - ARBOL GRANDE
    world[7][22] = Back.RED + '    '
    world[8][22] = Back.RED + '    '
    world[9][22] = Back.RED + '    '
    world[10][22] = Back.RED + '    '
    world[11][22] = Back.RED + '    '
    world[12][22] = Back.RED + '    '

    # 1PARTE VERDE DEL QUINTO ARBOL - ARBOL PEQUEÑO 1
    world[8][25] = Back.GREEN + '    '
    # 2PARTE VERDE DEL QUINTO ARBOL - ARBOL PEQUEÑO 1
    world[9][24] = Back.GREEN + '    '
    world[9][25] = Back.GREEN + '    '
    world[9][26] = Back.GREEN + '    '
    # TALLO DEL QUINTO ARBOL . ARBOL PEQUEÑO 1
    world[10][25] = Back.RED + '    '
    world[11][25] = Back.RED + '    '
    world[12][25] = Back.RED + '    '

    # 1PARTE VERDE DEL SEXTO ARBOL - ARBOL PEQUEÑO 2
    world[8][29] = Back.GREEN + '    '
    # 2PARTE VERDE DEL SEXTO ARBOL - ARBOL PEQUEÑO 2
    world[9][28] = Back.GREEN + '    '
    world[9][29] = Back.GREEN + '    '
    world[9][30] = Back.GREEN + '    '
    # TALLO DEL SEXTO ARBOL . ARBOL PEQUEÑO 2
    world[10][29] = Back.RED + '    '
    world[11][29] = Back.RED + '    '
    world[12][29] = Back.RED + '    '

    # piedras en parte inferior
    world[17][2] = Back.WHITE + '    '
    world[14][5] = Back.WHITE + '    '
    world[18][5] = Back.WHITE + '    '
    world[14][5] = Back.WHITE + '    '
    world[16][7] = Back.WHITE + '    '
    world[19][7] = Back.WHITE + '    '
    world[16][10] = Back.WHITE + '    '
    world[19][15] = Back.WHITE + '    '
    world[18][23] = Back.WHITE + '    '
    world[17][23] = Back.WHITE + '    '
    world[16][23] = Back.WHITE + '    '
    world[15][23] = Back.WHITE + '    '
    world[15][25] = Back.WHITE + '    '
    world[19][29] = Back.WHITE + '    '
    # piedras en parte superior
    world[12][7] = Back.WHITE + '    '
    world[11][7] = Back.WHITE + '    '
    world[12][8] = Back.WHITE + '    '
    world[11][8] = Back.WHITE + '    '
    world[11][9] = Back.WHITE + '    '
    world[12][9] = Back.WHITE + '    '
    world[10][8] = Back.WHITE + '    '
    world[12][12] = Back.WHITE + '    '
    world[12][15] = Back.WHITE + '    '
    world[12][16] = Back.WHITE + '    '
    world[11][16] = Back.WHITE + '    '
    world[12][20] = Back.WHITE + '    '
    world[12][30] = Back.WHITE + '    '

    # Sol
    world[1][30] = Back.LIGHTYELLOW_EX + '    '
    world[2][30] = Back.LIGHTYELLOW_EX + '    '
    world[3][30] = Back.LIGHTYELLOW_EX + '    '
    world[1][29] = Back.LIGHTYELLOW_EX + '    '
    world[2][29] = Back.LIGHTYELLOW_EX + '    '
    world[3][29] = Back.LIGHTYELLOW_EX + '    '
    world[1][28] = Back.LIGHTYELLOW_EX + '    '
    world[2][28] = Back.LIGHTYELLOW_EX + '    '
    world[3][28] = Back.LIGHTYELLOW_EX + '    '
    world[2][27] = Back.LIGHTYELLOW_EX + '    '
    world[4][27] = Back.LIGHTYELLOW_EX + '    '
    world[4][29] = Back.LIGHTYELLOW_EX + '    '


def draw_player(yi, xi):   # Mismo proceso que el anterior para dibujar al avatar

    # Avatar
    world[yi][xi] = Back.MAGENTA + '    ' # la mano
    world[yi][xi-1] = Back.CYAN + '    '  # centro
    world[yi-1][xi-1] = Back.CYAN + '    ' # pies
    world[yi+1][xi-1] = Back.CYAN + '    ' # cabeza
def fill(yi, xi):
    world[yi][xi] =  Back.LIGHTWHITE_EX + '    '
    world[yi][xi-1] = Back.LIGHTWHITE_EX + '    '
    world[yi-1][xi-1] =  Back.LIGHTWHITE_EX + '    '
    world[yi+1][xi-1] =  Back.LIGHTWHITE_EX + '    '

def arbol(yi,xi):
    global world
    if world[yi][xi] == Back.RED + '    ':
        print('AAA')
        return True
    print(world[yi][xi])
    return False

    
def piedra(yi,xi):
    global world
    if world[yi][xi] == Back.WHITE + '    ':
        print('BBB')
        return True
    print(world[yi][xi])
    return False

def destroy(yi, xi):
    world [yi][xi] = Back.LIGHTWHITE_EX + '    '
def collect(yi, xi):
    countwood = 0  #inicia la cuenta en 0
    countrock = 0
    #indicadores de la mano del jugador
    #recibe el zx y el zy para que collect se ejecute siempre en el espacio
    #de la mano del jugador sin importar el numero de comandos

    #Verifica que la mano del jugador se encuentra en el mismo espacio que un arbol
    if arbol(yi,xi):
        countwood +=1
    # Verifica que la mano del jugador se encuentra en el mismo espacio que una piedra
    if piedra(yi,xi):
        countrock += 1
    #Retorna el contador de los bloques destruidos
    destroy(yi, xi)
    
    return countwood, countrock


def move_player2(wood, rock): #Recibe los valores en el modulo para guardar la cuenta de collect
    xi = 3
    yi = 11
    #hacemos un bucle para jugar el tiempo deseado
    while True:
        moves = input('$ ').split() #aqui recibe los comandos en una string yse convierte el string en una lista para manejarla
            #aqui se cambian las coordenadas de los pixeles del cuerpo del jugador para poder moverlo despues
        for i in moves:
            if i == 'right':
                # es necesario para que el jugador no tenga un clon
                fill(yi,xi)
                xi +=1
                
            elif i == 'left':
                # es necesario para que el jugador no tenga un clon
                fill(yi,xi)
                xi -=1
                
            elif i == 'down':
                # es necesario para que el jugador no tenga un clon
                fill(yi,xi)
                yi += 1
                
            elif i == 'top':
                # es necesario para que el jugador no tenga un clon
                fill(yi,xi)
                yi -= 1
                
        if "extract" in moves: #se llama a la funcion colect se si se ingreso el comando extract
            ex = collect(yi, xi)
            wood += ex[0]
            rock += ex[1]  #guarda la cuenta de cada bucle
        if "destroy" in moves: #se llama a la funcion destroy se si se ingreso el comando destroy
                destroy(xi, yi)
                
        if xi in range(1, 31) and yi in range(1, 21): # se verifica que el jugador este dentro del mundo
                draw_player(yi, xi)
                print('$ Welcome to minecraft world XYZ')
                for y in range(21): # de aca en adelante imprimimos la matriz
                    for x in range(len(world[y])):
                        if x <= 30:
                            print(world[y][x].center(4), end='') # para imprimir la matriz, y end para que se haga fila
                            # y no columna, ya que el
                        elif x == 31:
                            print()
                            break
                print("Wood blocks:", wood)
                print("Stone blocks:", rock)
        else:
                print("Invalid operation") # si el jugador se sale del mundo sale operacion invalida


def main():
    draw_worldempty()
    draw_world() # llamamos a las funciones anteriores porque nos serviran pora que se ejecute
    wood = 0
    rock = 0
    
    while True:
        option = input('$ ').strip()#se ingresa el init para iniciar el programa
        if option == 'init':
            break
    move_player2(wood, rock)   #se ejecutan las funciones
    
main()