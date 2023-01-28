from pytesseract import pytesseract
import playsound, os, base64
from requests import Response, post

def image_to_text(path: str) -> list[str]:
  pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

  text: str = pytesseract.image_to_string(r"./test/tumblr_mjs0wx09on1s8792uo1_1280.png")

  lines: list[str] = []

  for line in text.splitlines():
    if not line.startswith(">"):
      continue

    lines.append(line)

  return lines

def text_to_mp3(filename: str, text: list[str]) -> any:
  session_id = "29e72eb587092137fbe1e42b3178098a"
  tts(session_id, req_text=text[0], play=True)
  # response = post_request(session_id, "Hello World", "en_au_001")
  # output = handle_response(response)

  # if not output["success"]:
  #   print(output["status"])
  #   return

  # write_mp3(filename, output["data"])
  # play_sound(filename)

def sanitize_text(text: str) -> str:
  text = text.replace("+", "plus")
  text = text.replace(" ", "+")
  text = text.replace("&", "and")

def post_request(session_id: str, text: str, speaker: str) -> Response:
  text = sanitize_text(text)

  headers: dict[str, str] = {
    "User-Agent": "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)",
    "Cookie": f"sessionid={session_id}"
  }

  url: str = f"https://api16-normal-v6.tiktokv.com/media/api/text/speech/invoke/?text_speaker={speaker}&req_text={text}&speaker_map_type=0&aid=1233"

  return post(url, headers=headers)

def handle_response(response: Response) -> dict[str, str]:
  if response.json()["message"] == "Couldn't load speech. Try again.":
    return {"status": "Session ID is invalid", "status_code": 5, "success": False }

  vstr = [response.json()["data"]["v_str"]][0]
  # msg = [response.json()["message"]][0]
  # scode = [response.json()["status_code"]][0]
  # log = [response.json()["extra"]["log_id"]][0]
  
  dur = [response.json()["data"]["duration"]][0]
  # spkr = [response.json()["data"]["speaker"]][0]

  return { "data": base64.b64decode(vstr), "duration": dur, "success": True }

def write_mp3(filename: str, data: any) -> None:
  with open(filename, "wb") as out:
    out.write(data)

def play_sound(filename: str) -> None:
  playsound.playsound(filename)

def tts(session_id: str, text_speaker: str = "en_us_c3po", req_text: str = "TikTok Text To Speech", filename: str = "voice.mp3", play: bool = False):
  req_text = req_text.replace("+", "plus")
  req_text = req_text.replace(" ", "+")
  req_text = req_text.replace("&", "and")

  headers = {
    "User-Agent": "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)",
    "Cookie": f"sessionid={session_id}"
  }

  url = f"https://api16-normal-v6.tiktokv.com/media/api/text/speech/invoke/?text_speaker={text_speaker}&req_text={req_text}&speaker_map_type=0&aid=1233"

  r = post(url, headers = headers)

  if r.json()["message"] == "Couldn't load speech. Try again.":
    output_data = {"status": "Session ID is invalid", "status_code": 5}
    print(output_data)
    return output_data

  vstr = [r.json()["data"]["v_str"]][0]
  msg = [r.json()["message"]][0]
  scode = [r.json()["status_code"]][0]
  log = [r.json()["extra"]["log_id"]][0]
  
  dur = [r.json()["data"]["duration"]][0]
  spkr = [r.json()["data"]["speaker"]][0]

  b64d = base64.b64decode(vstr)

  with open(filename, "wb") as out:
    out.write(b64d)

  output_data = {
    "status": msg.capitalize(),
    "status_code": scode,
    "duration": dur,
    "speaker": spkr,
    "log": log
  }

  print(output_data)

  if play is True:
    playsound.playsound(filename)
    os.remove(filename)

  return output_data
