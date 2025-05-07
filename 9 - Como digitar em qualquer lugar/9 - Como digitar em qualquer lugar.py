import pyautogui
import pyperclip
from time import sleep

def texto(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey("ctrl","v")
    

pyautogui.moveTo(1637,309,duration=1)
pyautogui.click()

texto("Automação é demais!")