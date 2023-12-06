import time
import pyautogui
from pywinauto.application import Application


def localiza_img_com_clique(img: str):
    procurar = "sim"
    caminho_img = f"img/{img}.png"

    while procurar == "sim":
        try:
            pega_img = pyautogui.locateCenterOnScreen(caminho_img, confidence=0.7)
            x, y = pega_img  # Desempacota as coordenadas
            pyautogui.click(x, y)
            procurar = "Achou"
            print(f"Achou a imagem {img}!!!")

        except:
            time.sleep(1)
            print(f"Procurando {img}...")


def localiza_img_com_clique_duplo(img: str):
    procurar = "sim"
    caminho_img = f"img/{img}.png"

    while procurar == "sim":
        try:
            pega_img = pyautogui.locateCenterOnScreen(caminho_img, confidence=0.8)
            x, y = pega_img  # Desempacota as coordenadas
            pyautogui.doubleClick(x, y)
            procurar = "Achou"
            print(f"Achou a imagem {img}!!!")

        except:
            time.sleep(1)
            print(f"Procurando {img}...")
