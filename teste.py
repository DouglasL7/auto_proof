from util import *

localiza_img_com_clique_com_mais_precisao("browser/pesquisar_arquivo_prova")
pyautogui.write(
    rf"C:/Users/douglas.lopes/Documents/Provas_para_lancamentos/Corrigidas/Matutino"
)

pyautogui.press("enter")


localiza_img_com_clique_com_mais_precisao("browser/pesquisa_arquivo_txt_na_pagina")

pyautogui.write("teste.txt")

pyautogui.press("enter")
