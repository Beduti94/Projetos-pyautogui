# win32api → pra simular o clique
import win32api
# win32con → pra pegar constantes do Windows
import win32con
import pyautogui
import keyboard
from time import sleep
# 1765,646 coluna 1
# 1889,625 coluna 2
# 2008,619 coluna 3
# 2141,623 coluna 4
# 0,0,0 RGB PRETO

pyautogui.click(1882,731,duration=1)
preto = (0,0,0)
def clicar(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('esc')== False:
    if pyautogui.pixelMatchesColor(1765,640,preto):
        clicar(1765,640)
    elif pyautogui.pixelMatchesColor(1889,640,preto):
        clicar(1889,640)
    elif pyautogui.pixelMatchesColor(2008,640,preto):
        clicar(2008,640)
    elif pyautogui.pixelMatchesColor(2141,640,preto):
        clicar(2141,640)

