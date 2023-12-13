import time
import pyautogui
import os
import re
from pywinauto.application import Application
from util import *

arquivos_questoes = {
    20: "Modelo20",
    25: "Modelo25",
    30: "Modelo30",
    35: "Modelo35",
    40: "Modelo40",
}

turnos = ["Madrugada", "Matutino", "Vespertino"]


def processo_correcao(seleciona_turno):
    print()


for turno in turnos:
    diretorio = f"C:/Users/douglas.lopes/Documents/Provas_para_lancamentos/Digitalizadas/{turno}"

    # Obtenha a lista de pastas no diretório
    pastas = [
        nome
        for nome in os.listdir(diretorio)
        if os.path.isdir(os.path.join(diretorio, nome))
    ]

    # Itere sobre as pastas
    for pasta in pastas:
        numbers = int(pasta[0:2])

        # Clicar em pasta
        localiza_img_com_clique("img_remark/clicar_em_pasta")

        # Pesquisa modelo correspondente
        localiza_img_com_clique("img_remark/pesquisa_modelo")
        pyautogui.write(f"{arquivos_questoes[numbers]}")
        time.sleep(1)

        pyautogui.press("down")
        time.sleep(0.5)

        pyautogui.press("down")
        time.sleep(0.5)

        pyautogui.press("up")
        time.sleep(0.5)

        pyautogui.press("enter")

        localiza_img_com_clique("img_remark/clicar_em_ler")

        localiza_img_com_clique("img_remark/clicar_em_proximo")

        localiza_img_com_clique("img_remark/clicar_em_ler_img")

        localiza_img_com_clique("img_remark/clicar_seta_para_baixo")

        # if turno == turnos[0]:
        #     print(f"{turno}: {arquivos_questoes[numbers]}")
        # elif turno == turnos[1]:
        #     print(f"{turno}: {arquivos_questoes[numbers]}")
        # elif turno == turnos[2]:
        #     print(f"{turno}: {arquivos_questoes[numbers]}")
