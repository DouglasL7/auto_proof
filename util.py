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


def localiza_img_com_clique_com_mais_precisao(img: str):
    procurar = "sim"
    caminho_img = f"img/{img}.png"

    while procurar == "sim":
        try:
            pega_img = pyautogui.locateCenterOnScreen(caminho_img, confidence=0.9)
            x, y = pega_img  # Desempacota as coordenadas
            time.sleep(2)
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


def localiza_gabaritos(img: str):
    procurar = "sim"

    while procurar == "sim":
        try:
            pega_img = pyautogui.locateCenterOnScreen(
                "img/word/clicar_em_pesquisa.png", confidence=0.7
            )
            x, y = pega_img  # Desempacota as coordenadas
            pyautogui.click(x, y)
            print(f"Achou a imagem {img}!!!")
            pyautogui.write(img)
            time.sleep(0.5)
            pyautogui.press("enter")
            procurar = "Digitou"

        except:
            time.sleep(1)
            print(f"Procurando {img}...")


def clicar_se_imagem_aparecer(imagem1, imagem2):
    caminho_img1 = f"img/{imagem1}.png"
    caminho_img2 = f"img/{imagem2}.png"

    tempo_inicial = time.time()
    tempo_limite = 5

    while time.time() - tempo_inicial < tempo_limite:
        print(tempo_inicial)
        try:
            img1 = pyautogui.locateCenterOnScreen(caminho_img1, confidence=0.9)
            if img1:
                x, y = img1
                pyautogui.click(x, y)
                return

            time.sleep(0.5)

        except Exception as e:
            print(f"Erro ao tentar localizar img1: {e}")
            time.sleep(1)

        try:
            img2 = pyautogui.locateCenterOnScreen(caminho_img2, confidence=0.9)
            if img2:
                x, y = img2
                pyautogui.click(x, y)
                return

            time.sleep(0.5)

        except Exception as e:
            print(f"Erro ao tentar localizar img2: {e}")
            time.sleep(1)

    print("Não achou nenhuma das imagens após 5 segundos.")
