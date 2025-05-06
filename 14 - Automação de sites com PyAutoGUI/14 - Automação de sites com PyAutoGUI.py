"""

1) Navegue até o site https://cursoautomacao.netlify.app/
    >usar o webbrowser

2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
    >Achar o botão "alerta"
    >mover o mouse para o campo de digitação
    >clicar

3) Clique em alerta, para gerar a alerta
    >Usar as coordenadas do botão "alerta" já existentes
    >clicar

4) Feche a alerta
    >achar o botão "ok" da janela que abriu
    >clicar

5) Suba a página totalmente para cima
    >usar o scroll do mouse ou clicar 'home'

6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
    >03 pagedown para chegar na posição
    >mover cursor do mouse até o botão de fazer download do excel
    >clicar
    >mover cursor do mouse até o botão de fazer download do pdf
    >clicar
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
    >usar pyautoguo.alert para mandar a mensagem

"""
import pyautogui
import webbrowser
from time import sleep

def passo1():
    webbrowser.open('https://cursoautomacao.netlify.app/')
    sleep(2)
    passo2()

def passo2():
    pyautogui.hotkey('pagedown')
    sleep(1)
    pyautogui.click(2002,946,duration=1)
    pyautogui.write("Felipe Beduti",interval=0.05)
    sleep(1)
    passo3()

def passo3():
    alerta = pyautogui.locateCenterOnScreen('alerta.png',confidence=0.8)
    pyautogui.click(alerta[0],alerta[1])
    sleep(1)
    passo4()

def passo4():
    ok_button = pyautogui.locateCenterOnScreen('ok.png',confidence=0.8)
    pyautogui.click(ok_button[0],ok_button[1])
    sleep(1)
    passo5()

def passo5():
    pyautogui.hotkey(['home'] * 2)
    sleep(1)
    passo6()
    
def passo6():
    # 462,534
    # 783,525
    pyautogui.hotkey('pagedown')
    sleep(1)
    pyautogui.hotkey('pagedown')
    sleep(1)
    pyautogui.hotkey('pagedown')
    sleep(1)
    pyautogui.click(462,534,duration=1)
    pyautogui.click(783,525,duration=1)
    sleep(1)
    passo7()
    
def passo7():
    pyautogui.alert(title='Aviso!',text='VOCÊ TERMINOU')
passo1()
