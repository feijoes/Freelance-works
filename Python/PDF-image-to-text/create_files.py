import pdf2image
import pytesseract
import os
from pytesseract import Output
from sys import argv
from PIL.Image import Image
pytesseract.pytesseract.tesseract_cmd =  "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import glob






def extract_text(pdf_path) -> list:
    text: list[str] = []
    
    images: list[Image] = pdf2image.convert_from_path(pdf_path)
    
    for pil_im in images:
        ocr_dict = pytesseract.image_to_data(pil_im, lang='eng', output_type=Output.DICT)
        text.append(" ".join(ocr_dict['text']))
    return  text

def create_file(content: list[str], filename: str) -> None:
    folder = filename.split("/")[0]
    if not os.path.exists(f"{folder}"):
        os.makedirs(folder)
    with open(filename, "w") as f:
        f.writelines(content)

def main(folder: str, typefile="pdf"):
    for file in glob.glob(f"{folder}/*.{typefile}"):
        filename = file.split("\\")[-1]
        text = extract_text(file)
        create_file(text,f"{folder}/{filename}_txt.txt")
    