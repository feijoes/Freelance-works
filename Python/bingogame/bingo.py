
import random

bingo = [{},{}]
ntableros = 0
def crear():
    global ntableros
    i = 1
    for i in "BINGO":
        while True:
            a = input(f"escribi los numeros de las letra {i} con un espacio").split()
            if len(a) == len(set(a)):
                print("no se puede numeros repetidos")
                continue
            if max(a) > i+14 or min(a) <= i-1:
                print(f"los numeros tienen que ser entre {i} a {i+14}")
                continue
            bingo[ntableros][i] = a 
            break
        i+=15 
    ntableros+=1
def auto():
    global ntableros
    i = 1
    for x in "BINGO":
        bingo[ntableros][x] = random.sample(range(i,i+14), 5)
        i+=15
    ntableros +=1
def printtablero(dict):
    line = list(dict.keys())
    for z in range(5):
        for i in line[z]:
            print(i ,end= " | ")
    s = list(dict.values())
    print('')
    for i in range(5):
        for j in range(5):
            if len(str(s[j][i])) == 2:
                print(s[j][i], end ='  ')
            else:
                print(s[j][i], end ='   ')
        print('\n')        
def juego():
    print ('tus tableros: ')
    anter = []
    while True:
        printtablero(bingo[0])
        if bingo[1]:
            printtablero(bingo[1])
        while True:
            foo = ''
            num =(random.randint(1,75))
            if num <=15:
                foo = 'B' +str(num)
            elif num <=30:
                foo = 'I' +str(num)
            elif num <= 45:
                foo = 'N' +str(num)
            elif num <=60:
                foo = 'G' +str(num)
            elif num <= 75:
                foo = 'O' +str(num)
            if foo not in anter:
                break
        anter.append(foo)
        print('----------------------------------------------------------------------------')
        print(f'numero sorteado : {foo}')
        print('----------------------------------------------------------------------------')
        printtablero(bingo[0])
        if bingo[1]:
            printtablero(bingo[1])
        while True:
            number = input('ves el numero que salio? numero de la tabla que salio, 1 para la primera y 2 para la segunda(si esta presente en las dos tablas pon los dos numeros con una coma  entre los dos) si no pon una "X" para saltear al proximo numero:  ').split(',')
            if number[0] == "X":
                break
            for i in number:
                passe = False
                if bingo[1]:
                    continue
                for index,valor in enumerate(bingo[int(i)-1][foo[0]]):
                    if valor == num:
                        bingo[int(i)-1][foo[0]][index] = 'x'
                        passe = True
                if not passe:
                    print(f'no hay {num} en el {i}')
            break
        for i in bingo:
            if len(set(sum(list(i.values()), []))) == 1 and set(sum(list(i.values()), [])[0]) == 'x':
                break
                
                
                
                

def menu():
    name = ""
    while True:
        print('--------------------------------------------------')
        accion = input('Menu Bingo \n --Registrar un jugador 1\n --Jugar 2\n --Ver tableros 3\n --Crear tablero 4 \nSalir "s"\n')
        if accion=='s':
            break
    
        if accion == '1':
            datos = input("ingresar tu nombre, tu edad y tu nick con un espacio entre cada informacion: ")
            name,edad,nick = datos.split()
            print(f"tu nombre es {name}, tenes {edad} años y tu nick es {nick}.")
            continue
        if not name:
            print("tenes que resgitrarte primero")
            continue
        if accion == '2' and bingo[0]:
            juego()
        elif accion == '3':
            if not bingo:
                print("no tenes tableros")
            if bingo[0]:
                printtablero(bingo[0])
            if bingo[1]:
                printtablero(bingo[1])
            
        if accion == '4':
            if ntableros == 2:
                print("ya tenes 2 tableros")
                continue
            while True:
                chose = input("deseas crear un tablero o que se genere automaticamente? (poner C para crear o una A para que sea automaticamente): ")
                if chose == "C":
                    crear()
                    break
                if chose == "A":
                    auto()
                    break
        
        
            
menu()
print('gracias por jugar!!')