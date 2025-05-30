import pyautogui
import cv2
import numpy as np
import time

print("Move o mouse e veja a cor HSV do pixel abaixo do cursor. Ctrl+C para sair.")

try:
    while True:
        x, y = pyautogui.position()  # pega posição do mouse
        pixel = pyautogui.screenshot(region=(x, y, 1, 1))
        r, g, b = pixel.getpixel((0, 0))
        
        # Converte RGB para HSV usando OpenCV (que usa BGR)
        color_bgr = np.uint8([[[b, g, r]]])
        hsv = cv2.cvtColor(color_bgr, cv2.COLOR_BGR2HSV)[0][0]

        print(f"Pos({x},{y}) - HSV: {hsv}")
        time.sleep(0.1)  # 10 vezes por segundo, pra não floodar

except KeyboardInterrupt:
    print("\nParado pelo usuário.")
