from pytube import Playlist,YouTube
from pytube.exceptions import * 
from warning import Warning

class Head(object):      #Classe objeto que representa as funções de download dos arquivos.
    
    @staticmethod
    def download_mp4(link) -> None:    #Método estático que é responsável por fazer o download de vídeos em MP4.
        video = YouTube(link)
        video.streams.get_highest_resolution().download()
    
    @staticmethod
    def download_mp3(link) -> None:    #Método estático que é responsável por fazer converter vídeos MP4 para áudios em MP3 e realizar o seu download.
        video = YouTube(link)
        title = video.title
        invalid_characters = "'\[{]}/|" + '"'

        for letter in range(len(invalid_characters)):
            title = title.replace(invalid_characters[letter],"")

        stream = video.streams.get_audio_only()
        stream.download('MP3' ,filename= (title + '.mp3'))
    
    @staticmethod
    def download_playlist(link) -> None:  #Método estático que é responsável por fazer o download de playlists de vídeos em MP
        playlist = Playlist(link)
        try:
            video_url = YouTube(link)  
        except VideoUnavailable:
            Warning.videounavailable()
        else:
            for video in playlist.videos:
                video.streams.get_highest_resolution().download('PLAYLIST')