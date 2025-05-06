# ​Link para praticar quebrar captcha ReCAPTCHA demo (google.com)​

import pyautogui
from time import sleep
# print(pyautogui.locateOnScreen('photo.png'))
# # outsput: Box(left=2372, top=1027, width=33, height=38)
# print(pyautogui.locateCenterOnScreen('photo.png'))
# # output: Point(x=2388, y=680)

def captcha_check():
    pyautogui.hotkey('win','r')
    pyautogui.write('opera')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write('www.google.com/recaptcha/api2/demo')
    pyautogui.press('enter')
    sleep(2)
    # pyautogui.locateOnScreen('captcha.png')
    captcha = pyautogui.locateCenterOnScreen('captcha.png')
    pyautogui.click(captcha)
    sleep(2)
    # pyautogui.locateOnScreen('enviar.png')
    enviar = pyautogui.locateCenterOnScreen('enviar.png',confidence=0.8)
    pyautogui.click(enviar)
    print('terminou')
captcha_check()


# versão deepseek:
"""
import pyautogui
from time import sleep

def captcha_check():
    # Abre o navegador
    pyautogui.hotkey('win', 'r')
    pyautogui.write('opera')
    pyautogui.press('enter')
    sleep(5)  # Tempo maior para o navegador abrir
    
    # Navega para o site
    pyautogui.write('https://www.google.com/recaptcha/api2/demo')
    pyautogui.press('enter')
    sleep(10)  # Tempo maior para a página carregar
    
    try:
        # Localiza e clica no captcha
        captcha_pos = pyautogui.locateCenterOnScreen('captcha.png', confidence=0.8)
        if captcha_pos:
            pyautogui.click(captcha_pos)
            print("Captcha clicado")
            sleep(5)  # Espera o captcha carregar
            
            # Alternativa 1: Localizar o botão enviar
            try:
                enviar_pos = pyautogui.locateCenterOnScreen('enviar.png', confidence=0.8)
                if enviar_pos:
                    pyautogui.click(enviar_pos)
                    print("Botão enviar clicado")
                else:
                    print("Botão enviar não encontrado - tentando Enter")
                    pyautogui.press('enter')  # Alternativa com Enter
            except:
                print("Erro ao localizar botão enviar - tentando Enter")
                pyautogui.press('enter')
        else:
            print("Captcha não encontrado")
    except Exception as e:
        print(f"Erro: {e}")
    
    print('Processo finalizado')

captcha_check()
"""