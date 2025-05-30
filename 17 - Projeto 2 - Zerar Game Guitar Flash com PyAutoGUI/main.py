import cv2
import numpy as np
import win32gui, win32ui, win32con
from pynput.keyboard import Controller
import time

TECLAS = {'verde': 'a', 'vermelha': 's', 'amarela': 'j', 'azul': 'k', 'laranja': 'l'}
FAIXAS_HSV = {
    'verde': (np.array([55, 200, 100]), np.array([65, 255, 255])),
    'vermelha': (np.array([0, 200, 200]), np.array([5, 255, 255])),
    'amarela': (np.array([28, 200, 200]), np.array([34, 255, 255])),
    # Azul expandido com S e V mínimos mais baixos pra pegar esses tons difíceis
    'azul': (np.array([90, 100, 150]), np.array([110, 255, 255])),
    'laranja': (np.array([10, 200, 200]), np.array([14, 255, 255]))
}
FAIXAS_X = {
    'verde': (125, 235), 'vermelha': (250, 370), 'amarela': (380, 510),
    'azul': (520, 635), 'laranja': (650, 760)
}

def captura_gdi(left, top, width, height):
    hwnd = win32gui.GetDesktopWindow()
    hwindc = win32gui.GetWindowDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()

    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    bmp_str = bmp.GetBitmapBits(True)
    img = np.frombuffer(bmp_str, dtype=np.uint8).reshape((height, width, 4))
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    win32gui.DeleteObject(bmp.GetHandle())
    memdc.DeleteDC(); srcdc.DeleteDC(); win32gui.ReleaseDC(hwnd, hwindc)
    return img

LIMIAR_Y_LOGICO = 35
ALTURA_FAIXA = 10
monitor = {"top": 1100, "left": 1580, "width": 850, "height": 150}
keyboard = Controller()
pressed = {cor: False for cor in TECLAS}
DEBUG = True

def bot_guitarflash():
    print("Bot GDI otimizado ligado! Aperte ESC pra sair.")
    time.sleep(2)

    while True:
        img = captura_gdi(monitor["left"], monitor["top"], monitor["width"], monitor["height"])
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        for cor, (lower, upper) in FAIXAS_HSV.items():
            x1, x2 = FAIXAS_X[cor]
            y1 = max(0, LIMIAR_Y_LOGICO - ALTURA_FAIXA // 2)
            y2 = LIMIAR_Y_LOGICO + ALTURA_FAIXA // 2

            mask = cv2.inRange(hsv, lower, upper)
            mask[:y1, :] = 0
            mask[y2:, :] = 0
            mask[:, :x1] = 0
            mask[:, x2:] = 0

            if cor == 'azul' and DEBUG:
                print(f"Pixels azuis detectados: {np.count_nonzero(mask)}")

            contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            acionou = False

            for cnt in contornos:
                _, y, _, h = cv2.boundingRect(cnt)
                if y + h >= LIMIAR_Y_LOGICO:
                    if not pressed[cor]:
                        keyboard.press(TECLAS[cor])
                        pressed[cor] = True
                    acionou = True
                    break

            if not acionou and pressed[cor]:
                keyboard.release(TECLAS[cor])
                pressed[cor] = False

            if DEBUG:
                cor_bgr = {
                    'verde': (0, 255, 0), 'vermelha': (0, 0, 255),
                    'amarela': (0, 255, 255), 'azul': (255, 0, 0), 'laranja': (0, 140, 255)
                }[cor]
                cv2.rectangle(img, (x1, y1), (x2, y2), cor_bgr, 2)
                for cnt in contornos:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(img, (x, y), (x + w, y + h), cor_bgr, 1)

        if DEBUG:
            cv2.line(img, (0, LIMIAR_Y_LOGICO), (img.shape[1], LIMIAR_Y_LOGICO), (255, 255, 255), 2)
            cv2.imshow("preview", img)
            if cv2.waitKey(1) == 27:
                break

    if DEBUG:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    bot_guitarflash()
