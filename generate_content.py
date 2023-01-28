from pytesseract import pytesseract
import playsound, os, base64
from requests import Response, post

def image_to_text(path: str) -> list[str]:
  pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

  text: str = pytesseract.image_to_string(path)

  lines: list[str] = []

  for line in text.splitlines():
    if not line.startswith(">"):
      continue

    lines.append(line)

  return lines

def text_to_mp3(text: list[str]):
  full_text = ""

  for line in text:
    full_text += line + ","

  session_id = "29e72eb587092137fbe1e42b3178098a"
  return tts(session_id, full_text)

def tts(session_id: str, text: str, speaker: str = "en_us_001"):
  text = text.replace("+", "plus")
  text = text.replace(" ", "+")
  text = text.replace("&", "and")
  text = text.replace(">", "")

  headers = {
    "User-Agent": "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)",
    "Cookie": f"sessionid={session_id}"
  }

  url = f"https://api16-normal-v6.tiktokv.com/media/api/text/speech/invoke/?text_speaker={speaker}&req_text={text}&speaker_map_type=0&aid=1233"

  r = post(url, headers = headers)

  if r.json()["message"] == "Couldn't load speech. Try again.":
    output_data = {"status": "Session ID is invalid", "status_code": 5}
    print(output_data)
    return output_data

  vstr = [r.json()["data"]["v_str"]][0]
  # msg = [r.json()["message"]][0]
  # scode = [r.json()["status_code"]][0]
  # log = [r.json()["extra"]["log_id"]][0]
  
  # dur = [r.json()["data"]["duration"]][0]
  # spkr = [r.json()["data"]["speaker"]][0]

  b64d = base64.b64decode(vstr)

  with open("./result/audio/voice.mp3", "wb") as out:
    out.write(b64d)

  # output_data = {
  #   "status": msg.capitalize(),
  #   "status_code": scode,
  #   "duration": dur,
  #   "speaker": spkr,
  #   "log": log
  # }

  # if play is True:
  #   playsound.playsound(filename)
  #   os.remove(filename)

  return [r.json()["data"]["duration"]][0]
