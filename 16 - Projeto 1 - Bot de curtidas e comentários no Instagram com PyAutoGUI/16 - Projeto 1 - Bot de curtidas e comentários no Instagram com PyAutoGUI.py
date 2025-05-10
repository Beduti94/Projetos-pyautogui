
""" 
Bot de curtidas e comentários no instagram:

Acessar_site()
1- navegar até o site;
2- entrar com meu usuario;
3- entrar com minha senha;
4- clicar em log in; 
5- clicar em not now; 
6- fechar a janela de salvar senha; opcional

Acessar_pagina()
7- pesquisar pela pagina
8- entrar na pagina

dar_like()
9- clicar na postagem mais recente
10- verificar se ja curti ou não a ponstagem
bot_pause()
11- se ja tiver curtido, fazer nada e pauasar o bot por 24h
12- se não tiver curtido, curtir foto
13- se não tiver curtido, comentar foto
bot_pause()
14- Pausar por 24horas
15- após 24 horas, rodar de novo
"""
import pyautogui
import webbrowser
from time import sleep
import time
from datetime import datetime

def main():
    data = datetime.now()
    login = pyautogui.prompt(title="Login do instagram",text="Digite seu telefone, nome de usuario ou email")
    senha = pyautogui.password(title="Login do instagram",text="Digite sua senha",mask='*')
    def logout():
            pyautogui.press('esc')
            sleep(1)
            pyautogui.moveRel(-1026,175,duration=1)
            pyautogui.click(duration=1)
            sleep(1)
            pyautogui.moveRel(0,-115,duration=1)
            pyautogui.click(duration=1)
            bot_pause()
        
    def acessar_site(): 
        sleep(2)
        webbrowser.open("https://www.instagram.com/?flo=true")
        sleep(4)
        pyautogui.hotkey("alt","space","x")
        sleep(1)
        entrar_posi = pyautogui.locateCenterOnScreen("entrar_2.png",confidence=0.8) # Coordenada de referência
        pyautogui.moveTo(entrar_posi[0],entrar_posi[1],duration=0.78)
        pyautogui.moveRel(0,-142,duration=0.5)
        pyautogui.click()
        pyautogui.typewrite(login)
        pyautogui.press('tab')
        pyautogui.typewrite(senha)
        pyautogui.click(entrar_posi[0],entrar_posi[1])
        sleep(6)
        acessar_pagina()

    def acessar_pagina():
        pyautogui.hotkey('ctrl','l')
        pyautogui.typewrite('www.instagram.com/nike',interval=0.1)
        pyautogui.press('enter')
        sleep(4)
        dar_like()

    def dar_like():
        sleep(2)
        seguir_posi = pyautogui.locateCenterOnScreen("seguir.png",confidence=0.8) # Coordenada de referência
        pyautogui.moveTo(seguir_posi[0],seguir_posi[1],duration=2)
        pyautogui.moveRel(-488,1036,duration=1.5)
        pyautogui.click()
        sleep(4)
        no_sound_posi = pyautogui.locateCenterOnScreen("no_sound.png",confidence=0.8) # Coordenada de referência
        pyautogui.moveTo(no_sound_posi[0],no_sound_posi[1])
        pyautogui.moveRel(102,-176)
        x, y = pyautogui.position()
        heart_color = pyautogui.pixel(x,y)

        if heart_color == (255,48,64): # Coração vermelho = ja dei like
            print(f"Já curtiu! - {data.strftime("%d/%m/%Y %H:%M:%S")}")
            sleep(2)            
            logout()

        elif heart_color == (0,0,0): # Coração preto (tema escuro) = não dei like
            pyautogui.click()
            print(f"Você deixou um like!{data.strftime("%d/%m/%Y %H:%M:%S")}")
            sleep(1)
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.typewrite("Cool!",interval=0.5)
            pyautogui.press('tab')
            pyautogui.press('enter')
            print(f"Você deixou um comentário!{data.strftime("%d/%m/%Y %H:%M:%S")}")
            sleep(2)
            logout()

        elif heart_color == (255,255,255): # Coração branco (tema claro) = nao dei like
            pyautogui.click()
            print(f"Você deixou um like!{data.strftime("%d/%m/%Y %H:%M:%S")}")
            sleep(1)
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.typewrite("Cool!")
            pyautogui.press('tab')
            pyautogui.press('enter')
            print(f"Você deixou um comentário!{data.strftime("%d/%m/%Y %H:%M:%S")}")
            sleep(2)
            logout()

    def bot_pause():
        sleep(10)
        pyautogui.hotkey("ctrl","f4")
        acessar_site()

    acessar_site()
main()
