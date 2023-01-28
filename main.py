from generate_content import image_to_text, text_to_mp3

def main():
  text = image_to_text('./test/tumblr_mjs0wx09on1s8792uo1_1280.png')

  # for line in text:
  #   print(line)

  audio = text_to_mp3("./audio.mp3", ["Hello World"])

if __name__ == "__main__":
  main()
