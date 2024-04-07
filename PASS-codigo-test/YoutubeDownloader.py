from pytube import YouTube
url = input("Coloque a URL do vídeo: ")
video = YouTube(url)
print('Baixando video....')
download = video.streams.get_highest_resolution()
downloadpath = r"C:\Users\hoolf\Videos"
download.download(downloadpath)
print('O download foi um sucesso!')