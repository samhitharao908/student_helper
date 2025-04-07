from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt_obj = yt.streams.filter(only_audio=True, file_extension='mp3')
try:
    yt_obj.download(output_path='tmp/audio_files/')
except:
    print("There was an error in downloading the file")