from generate_content import image_to_text, text_to_mp3

def main():
  text = image_to_text('./result/greentext/mt4v52fso7d51.jpg')

  # for line in text:
  #   print(line)

  text_to_mp3(text)

if __name__ == "__main__":
  main()
