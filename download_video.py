from pytube import YouTube

def download_background_video(url):
  video = YouTube(url)
  print(f'Downloading \'{video.title}\'')
  stream = video.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
  stream.download('./result/video/')
