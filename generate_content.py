from pytesseract import pytesseract

def process_image(path: str) -> list[str]:
  pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

  text: str = pytesseract.image_to_string(r'./test/tumblr_mjs0wx09on1s8792uo1_1280.png')

  lines: list[str] = []

  for line in text.splitlines():
    if not line.startswith('>'):
      continue

    lines.append(line)

  return lines

      
