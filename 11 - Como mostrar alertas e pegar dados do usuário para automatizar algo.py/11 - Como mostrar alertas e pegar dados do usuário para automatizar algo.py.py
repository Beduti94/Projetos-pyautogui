import pyautogui
import pyperclip
from time import sleep
# pegar email
# pegar senha
# abrir bloco de notas
# colar email
# colar a senha

def pegar_dados():
    email = pyautogui.prompt(title="Login",text="Digite seu email")
    senha = pyautogui.password(title="Password",text="Digite sua senha",mask="*")
    return [email,senha]

def colar_dados(email,senha):
    pyautogui.hotkey("win","r")
    pyautogui.write('notepad',interval=0.25)
    pyautogui.press('enter')
    pyperclip.copy(email)   
    pyautogui.hotkey("ctrl","v")
    pyautogui.press('enter')
    sleep(1)
    pyperclip.copy(senha)
    pyautogui.hotkey("ctrl","v")

email, senha = pegar_dados()
colar_dados(email,senha)
