import pdf2image
import pytesseract
from pytesseract import Output
from sys import argv
from PIL.Image import Image
pytesseract.pytesseract.tesseract_cmd =  "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import glob

folder: str = argv[1]

typefile: str = ".pdf" if len(argv) < 3 else argv[2]




def extract_text(pdf_path) -> list:
    text: list[str] = []
    
    images: list[Image] = pdf2image.convert_from_path(pdf_path)
    
    for pil_im in images:
        ocr_dict = pytesseract.image_to_data(pil_im, lang='es', output_type=Output.DICT)
        text.append(" ".join(ocr_dict['text']))
    return  text

def create_file(content: list[str], filename: str) -> None:
    with open(filename) as f:
        f.write(content)

for file in glob.glob(f"{folder}/*.{typefile}"):
    filename = file.split("\\")[-1]
    text = extract_text(file)
    create_file(text,f"{folder}_txt/{filename}_txt")
    