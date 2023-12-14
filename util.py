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

    time.sleep(2)

    try:
        while True:
            # Localizar a posição da imagem 1 na tela
            imagem1_pos = pyautogui.locateOnScreen(caminho_img1)

            # Localizar a posição da imagem 2 na tela
            imagem2_pos = pyautogui.locateOnScreen(caminho_img2)

            # Verificar se a imagem 1 foi encontrada
            if imagem1_pos is not None:
                print("Imagem 1 encontrada! Clicando...")
                pyautogui.click(imagem1_pos)
                procurar = "Achou"
                break

            # Verificar se a imagem 2 foi encontrada
            elif imagem2_pos is not None:
                print("Imagem 2 encontrada! Clicando...")
                pyautogui.click(imagem2_pos)
                procurar = "Achou"
                break

            # Aguardar um curto período de tempo antes de verificar novamente
            time.sleep(1)

    except:
        time.sleep(1)
        print(f"Procurando {imagem1 or imagem2}...")
