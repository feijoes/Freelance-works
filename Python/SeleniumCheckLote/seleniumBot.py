import pyautogui
from pytesseract import pytesseract
from time import sleep
import os
from twocaptcha import TwoCaptcha


URL = "https://www.bbva.pe/personas/olvido-contrasena.html"
inputNumeroImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\numeroInput.jpeg"
inputClaveImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\ClaveInput.jpeg"
ErrorImg= os.path.dirname(os.path.abspath(__file__)) + "\\img\\Error.jpeg"
SiguienteImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\Siguiente.jpeg"


def write_in_input(img: str, text:str,wait:int):
    pyautogui.moveTo(list(img))
    pyautogui.click()
    sleep(wait)
    pyautogui.write(text)
    sleep(wait)

def click(img:str):
    pyautogui.moveTo(list(img))
    pyautogui.click()

from twocaptcha import TwoCaptcha



def captchaSolver(image,key):
    solver = TwoCaptcha(key)
    id = solver.send(file=image)
    sleep(15)
    code = solver.get_result(id)
    print(code)
    return code



def check_numero(numeros : list[int],clave: str,API_KEY:str) -> None:
    try:
        #for numero in numeros:
        #    for _ in range(20): 
        #        inputNumero = pyautogui.locateOnScreen(inputNumeroImg,confidence=.5)
        #        if inputNumero:
        #            break
        #        sleep(0.5)
        #    write_in_input(inputNumeroImg,numero,0.5)
        #    sleep(1)
        #    write_in_input(inputClaveImg,clave,0.5)
        #
        pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        
    
        
        img = pyautogui.screenshot("test.jpg",region=(290,600, 270, 130))


        text:str = pytesseract.image_to_string(img,config=f'-l eng --psm 12 -c tessedit_char_whitelist=0123456789abcdfghijkmnlopqrsturstuvwxyz')
        print(text.split())
        sleep(4)
        print("sending to 2capcha")
        result = captchaSolver("./test.jpg",API_KEY)
        print(result)
        pyautogui.locateOnScreen(SiguienteImg,confidence=.5)
            
        
            
            
    except Exception as E:
        print(E)
  
    
    