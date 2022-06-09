from pytube.exceptions import *
import PySimpleGUI as sg
from head import Head
from warning import Warning

class Main(object): #Classe objeto que representa a parte principal do aplicativo.
    def __init__(self) -> None:
        super().__init__()
        
    def start(self) -> None: #Método utilizado para exibir a interface do aplicativo utilizando a biblioteca PySimpleGUI e executar as opções.
        sg.theme('DarkBlue4')
        layout = [
            [sg.Text('')],
            [sg.Text('')],
            [sg.Canvas(background_color='#6A5ACD', size=(2000,10))],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('SOFTWARE DE DOWNLOAD', font=('Consolas', 20))],
            [sg.Button('MP3', size=(10,2) )],
            [sg.Button('MP4',size=(10,2) )],
            [sg.Button('PLAYLIST',size=(10,2))],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Canvas(background_color='#6A5ACD', size=(2000,10))],
            [sg.Text('')],
            [sg.Text('')],
            [sg.Text('Produced by Alex, Amadeus and Gabriel', font=('Arial', 7))],
        ]   
       
        main_window = sg.Window('Software de Download', layout, size =(600,500), element_justification=('center'),icon="img\\main_icon.ico")
        
        while True: #Executa as opções de acordo com a escolha do usuário.
            button, values = main_window.Read()

            if values == sg.WINDOW_CLOSED:
                break
            else:
                if button == 'MP3':
                    self.janela_mp3()
                    
                if button == 'MP4':
                    self.janela_mp4()
                    
                if button == 'PLAYLIST':
                    self.janela_playlist()

    def janela_mp3(self) -> None: #Método utilizado para exibir a interface do download de áudios em MP3 e executar as opções.
        layout1 =[
            [sg.Text('────── ♪  MP3  ♪ ──────', font=('Consolas', 12))],
            [sg.Text('')],
            [sg.Text('𝐈𝐍𝐒𝐈𝐑𝐀 𝐎 𝐋𝐈𝐍𝐊 𝐃𝐎 𝐕𝐈𝐃𝐄𝐎')],
            [sg.Input(key='-LINK-')],
            [sg.Text('')],
            [sg.Button('Baixar', size=(13,1))],
        ]
        
        window_mp3 = sg.Window('MP3', layout1, size =(300,200), element_justification= 'center',icon='img\\mp3icon.ico')
        button,values = window_mp3.Read()
        try:
            if values == sg.WINDOW_CLOSED:
                window_mp3.hide()

            if button == 'Baixar':
                link = values ['-LINK-']
                Head.download_mp3(link)
                Warning.popup_success()
                window_mp3.hide()

        except RegexMatchError:         #Tratamento de excessão para caso ocorra um erro inesperado.
            Warning.popup_error()
            window_mp3.hide()
        
        except VideoUnavailable:        #Tratamento de excessão para caso o vídeo selecionado não esteja disponível.
            Warning.videounavailable()
            window_mp3.hide()
        
        except ExtractError:              #Tratamento de excessão para caso ocorra um erro de extração.
            Warning.extract()        
            window_mp3.hide()
            
            
    def janela_mp4(self) -> None:  #Método utilizado para exibir a interface do download de vídeos em MP4 e executar as opções.
        layout2 =[
            [sg.Text('────── ♪  MP4  ♪ ──────', font=('Consolas', 12))],
            [sg.Text('')],
            [sg.Text('𝐈𝐍𝐒𝐈𝐑𝐀 𝐎 𝐋𝐈𝐍𝐊 𝐃𝐎 𝐕𝐈𝐃𝐄𝐎')],
            [sg.Input(key='-LINK-')],
            [sg.Text('')],
            [sg.Button('Baixar', size=(13,1))],
        ]
        window_mp4 = sg.Window('MP4', layout2, size =(300,200), element_justification= 'center', icon='img\\mp4icon.ico')
        button,values = window_mp4.Read()
        try:
            if values == sg.WINDOW_CLOSED:
                window_mp4.hide()

            if button == 'Baixar':
                link = values ['-LINK-']
                Head.download_mp4(link)
                Warning.popup_success()
                window_mp4.hide()
        
        except RegexMatchError:           #Tratamento de excessão para caso ocorra um erro inesperado.
            Warning.popup_error()
            window_mp4.hide()
        
        except VideoUnavailable:          #Tratamento de excessão para caso o vídeo selecionado não esteja disponível.
            Warning.videounavailable()
            window_mp4.hide()
        
        except ExtractError:              #Tratamento de excessão para caso ocorra um erro de extração.
            Warning.extract()        
            window_mp4.hide()
        

    def janela_playlist(self) -> None:   #Método utilizado para exibir a interface do download de playlist em MP4 e executar as opções.
        sg.theme('DarkBlue4')
        layout3 =[
            [sg.Text('────── ♪  PLAYLIST  ♪ ──────', font=('Consolas', 12))],
            [sg.Text('')],
            [sg.Text('𝐈𝐍𝐒𝐈𝐑𝐀 𝐎 𝐋𝐈𝐍𝐊 𝐃𝐀 𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓')],
            [sg.Input(key='-LINK-')],
            [sg.Text('')],
            [sg.Button('Baixar', size=(13,1))],
        ]
        
        window_playlist = sg.Window('PLAYLIST', layout3, size =(300,200), element_justification= 'center',icon='img\\playlisticon.ico')
        button,values = window_playlist.Read()
        try:
            if values == sg.WINDOW_CLOSED:
                window_playlist.hide()

            if button == 'Baixar':
                link = values ['-LINK-']
                Head.download_playlist(link)
                Warning.popup_success()
                window_playlist.hide()

        except RegexMatchError:           #Tratamento de excessão para caso ocorra um erro inesperado.
            Warning.popup_error()
            window_playlist.hide()
        
        except VideoUnavailable:          #Tratamento de excessão para caso o vídeo selecionado não esteja disponível.
            Warning.videounavailable()
            window_playlist.hide()
        
        except ExtractError:              #Tratamento de excessão para caso ocorra um erro de extração.
            Warning.extract()        
            window_playlist.hide()
        
App = Main()
App.start()