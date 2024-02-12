import time
import pyautogui
import os
from pywinauto.application import Application
import ctypes


def localiza_img_com_clique(img: str):
    procurar = "sim"
    caminho_img = f"img/{img}.png"

    while procurar == "sim":
        try:
            pega_img = pyautogui.locateCenterOnScreen(caminho_img, confidence=0.7)
            x, y = pega_img  # Desempacota as coordenadas
            pyautogui.moveTo(x, y)
            time.sleep(1)
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
            pyautogui.moveTo(x, y)
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
            pyautogui.moveTo(x, y)
            time.sleep(1)
            pyautogui.doubleClick(x, y)
            procurar = "Achou"
            print(f"Achou a imagem {img}!!!")

        except:
            time.sleep(1)
            print(f"Procurando {img}...")


def localiza_img_com_clique_duplo_mais_precisao(img: str):
    procurar = "sim"
    caminho_img = f"img/{img}.png"

    while procurar == "sim":
        try:
            pega_img = pyautogui.locateCenterOnScreen(caminho_img, confidence=0.9)
            x, y = pega_img  # Desempacota as coordenadas
            pyautogui.moveTo(x, y)
            time.sleep(1)
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
    tempo_limite = 10

    while time.time() - tempo_inicial < tempo_limite:
        try:
            img1 = pyautogui.locateCenterOnScreen(caminho_img1, confidence=0.9)
            if img1:
                x, y = img1
                pyautogui.moveTo(x, y)
                time.sleep(1)
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
                pyautogui.moveTo(x, y)
                time.sleep(1)
                pyautogui.click(x, y)
                return

            time.sleep(0.5)

        except Exception as e:
            print(f"Erro ao tentar localizar img2: {e}")
            time.sleep(1)

    print("Não achou nenhuma das imagens após 10 segundos.")


nome_da_pasta_antiga = []


def altera_nome_da_pasta(turno, pasta, trocar: bool):
    novo_nome = "Selecione essa"

    diretorio_digitalizadas = (
        "C:/Users/douglas.lopes/Documents/Provas_para_lancamentos/Digitalizadas"
    )

    if trocar == True:
        diretorio_atual = os.path.join(diretorio_digitalizadas, turno, pasta)

        diretorio_novo = os.path.join(diretorio_digitalizadas, turno, novo_nome)

        os.rename(diretorio_atual, diretorio_novo)
    else:
        diretorio_atual = os.path.join(diretorio_digitalizadas, turno, novo_nome)
        print(f"Atual:{diretorio_atual}")
        diretorio_novo = os.path.join(
            diretorio_digitalizadas, turno, nome_da_pasta_antiga[0]
        )

        os.rename(diretorio_atual, diretorio_novo)


# Constantes da API do Windows
SW_MINIMIZE = 6
SW_RESTORE = 9
SW_SHOWMAXIMIZED = 3
GW_HWNDNEXT = 2

titulo_remark = "Central de dados do Remark Office OMR"

titulo_navegador = "Leitura Arquivo de Provas - Seleção - DOUGLAS.LOPES - Google Chrome"


def encontrar_janela(titulo):
    return ctypes.windll.user32.FindWindowW(None, titulo)


def minimizar_janela(hwnd):
    ctypes.windll.user32.ShowWindow(hwnd, SW_MINIMIZE)


def maximizar_janela(hwnd):
    ctypes.windll.user32.ShowWindow(hwnd, SW_SHOWMAXIMIZED)


def encontrar_proxima_janela(hwnd):
    return ctypes.windll.user32.GetWindow(hwnd, GW_HWNDNEXT)


def maximizar_ou_minimizar(janela: str, mm: bool):
    titulo = encontrar_janela(janela)

    if mm == True:
        maximizar_janela(titulo)
    else:
        minimizar_janela(titulo)
