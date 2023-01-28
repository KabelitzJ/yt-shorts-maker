from generate_content import image_to_text, text_to_mp3
from download_video import download_background_video
from create_video import create_video

def main():
  text = image_to_text('./result/greentext/rjjq31qtl6231.jpg')

  # for line in text:
  #   print(line)

  text_to_mp3(text)

  # download_background_video('https://www.youtube.com/watch?v=Pt5_GSKIWQM')

  create_video("./result/video/background.mp4", "./result/greentext/rjjq31qtl6231.jpg", "./result/audio/voice.mp3", "./result/video/result.mp4")

if __name__ == "__main__":
  main()
