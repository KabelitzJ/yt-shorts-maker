from moviepy import editor

def create_video(background: str, foreground: str, voice: str, destination: str):
  video = editor.VideoFileClip(background)
  audio = editor.AudioFileClip(voice)

  print(audio.duration)

  clip = video.subclip(0.0, audio.duration)
  clip.audio = editor.CompositeAudioClip([audio])

  image = editor.ImageClip(foreground)
  image = image.set_start(0.0)
  image = image.set_duration(audio.duration)
  # image = image.margin(right=100, top=100, left=100, bottom=100)
  image = image.resize(width=200, height = 400)
  image = image.set_pos(("center", "center"))

  final = editor.CompositeVideoClip([clip, image])

  final.write_videofile(destination)
