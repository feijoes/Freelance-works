import pyautogui
from pytesseract import pytesseract
from time import sleep
import os
import cv2 as cv
URL = "https://www.bbva.pe/personas/olvido-contrasena.html"
inputNumeroImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\numeroInput.jpeg"
inputClaveImg = os.path.dirname(os.path.abspath(__file__)) + "\\img\\ClaveInput.jpeg"
def write_in_input(img: str, text:str,wait:int):
    pyautogui.moveTo(list(img))
    pyautogui.click()
    sleep(wait)
    pyautogui.write(text)
    sleep(wait)

def check_numero(numeros : list[int],clave: str) -> None:
    try:
        #for numero in numeros:
        #    for _ in range(20): 
        #        inputNumero = pyautogui.locateOnScreen(inputNumeroImg,confidence=.5)
        #        if inputNumero:
        #            break
        #        sleep(0.5)
#
        #    write_in_input(inputNumeroImg,numero,0.5)
        #    sleep(1)
        #    write_in_input(inputClaveImg,clave,0.5)
        
        pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        
       
 
        os.system("convert test.png --morphology Erode Disk:2 captcha5.tif")
        os.system("convert test.png --morphology Dilate Disk:1.5 captcha5.tif")
        os.system(" convert test.png --threshold 41% captcha5.tif")
        
        pyautogui.screenshot("test.png",region=(290,600, 270, 130))
        img = cv.imread("./test.png")
    
        text:str = pytesseract.image_to_string(img,config=f'-l eng --psm 12 -c tessedit_char_whitelist=0123456789abcdfghijkmnlopqrsturstuvwxyz')
        print(text.split())
    
            
            
            
    except Exception as E:
        print(E)
        sleep(100)
    
    