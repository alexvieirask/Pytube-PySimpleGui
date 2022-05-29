import PySimpleGUI as sg

class Warning(object):          #Classe objeto que representa as janelas que exibem os resultados(sucesso ou erro) do aplicativo.
    @staticmethod 
    def popup_success() -> list:        #Método estático que exibe uma janela informando o êxito da ação executada.
        sg.theme('DarkBlue4')   
        layoutpopup = [
            [sg.popup('Download Concluido com Sucesso',title="Sucesso", icon = "img\\corretoicon.ico")]
            ]            
        return layoutpopup
    
    @staticmethod
    def popup_error() -> list:          #Método estático que exibe uma janela informando a falha da ação executada.
        sg.theme('DarkBlue4')
        layoutpopup = [
            [sg.popup('Ocorreu um Erro inesperado',title = "Erro",icon = "img\\erroricon.ico")]
            ]
        return layoutpopup
    
    @staticmethod
    def videounavailable() -> list:     #Método estático que exibe uma janela informando a indisponibilidade do vídeo selecionado.
        sg.theme('DarkBlue4')
        layoutpopup = [
            [sg.popup('O Video esta indisponível',title = "Erro",icon = "img\\erroricon.ico")]
            ]
        return layoutpopup
    
    @staticmethod
    def videoregionblocked() -> list:   #Método estático que exibe uma janela informando indisponibilidade do vídeo selecionado em sua região.
        sg.theme('DarkBlue4')
        layoutpopup = [
            [sg.popup('Video indisponível na sua região',title = "Erro",icon = "img\\erroricon.ico")]
            ]
        return layoutpopup
    
    @staticmethod
    def extract() -> list:   #Método estático que exibe uma janela informando um erro de extração.
        sg.theme('DarkBlue4')
        layoutpopup = [
            [sg.popup('Ocorreu um erro de extração',title = "Erro",icon = "img\\erroricon.ico")]
            ]
        return layoutpopup

    @staticmethod
    def privatevideo() -> list:   #Método estático que exibe uma janela informando um erro de extração.
        sg.theme('DarkBlue4')
        layoutpopup = [
            [sg.popup('O Video em questão é privado',title = "Erro",icon = "img\\erroricon.ico")]
            ]
        return layoutpopup
        