import time
import pyautogui
import os
import subprocess
from util import *

app = Application().start("C:\Program Files (x86)\Gravic\Remark Office OMR\RooU.exe")

arquivos_questoes = {
    20: "Modelo20",
    25: "Modelo25",
    30: "Modelo30",
    35: "Modelo35",
    40: "Modelo40",
}

turnos = ["Madrugada", "Matutino", "Vespertino"]


def clica_no_gabarito():
    localiza_img_com_clique_duplo("img_remark/clica_pasta_gabarito")


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
        n_questoes_da_pasta = int(pasta[0:2])

        print(f"Secionando a pasta: {pasta}")

        time.sleep(1)
        # Clicar em pasta
        localiza_img_com_clique("img_remark/clicar_em_pasta")

        time.sleep(0.5)
        print(f"Selecionando o modelo: {n_questoes_da_pasta}")
        # Pesquisa modelo correspondente

        localiza_img_com_clique("img_remark/pesquisa_modelo")
        pyautogui.write(f"{arquivos_questoes[n_questoes_da_pasta]}")
        time.sleep(1)

        pyautogui.press("down")
        time.sleep(0.5)

        pyautogui.press("down")
        time.sleep(0.5)

        pyautogui.press("up")
        time.sleep(0.5)

        pyautogui.press("enter")

        localiza_img_com_clique("img_remark/clicar_em_ler")

        time.sleep(2)

        clicar_se_imagem_aparecer(
            "img_remark/clicar_em_ler_img_azul", "img_remark/clicar_em_ler_img"
        )

        clicar_se_imagem_aparecer(
            "img_remark/clicar_em_proximo", "img_remark/clicar_em_proximo2"
        )

        localiza_img_com_clique("img_remark/clicar_seta_para_baixo")

        time.sleep(1)

        localiza_img_com_clique("img_remark/clicar_em_documentos")

        time.sleep(0.5)
        localiza_img_com_clique_duplo("img_remark/clicar_na_pasta_de_provas")

        time.sleep(0.5)

        localiza_img_com_clique_duplo("img_remark/clicar_digitalizadas")

        time.sleep(0.5)

        nome_da_pasta_antiga.append(pasta)

        altera_nome_da_pasta(turno, pasta, True)

        print(pasta)
        if turno == turnos[0]:
            print(f"Clicar em: {turno}")
            localiza_img_com_clique_duplo("img_remark/clicar_em_madrugada")

        elif turno == turnos[1]:
            print(f"Clicar em: {turno}")
            localiza_img_com_clique_duplo("img_remark/clicar_em_matutino")

        elif turno == turnos[2]:
            print(f"Clicar em: {turno}")
            localiza_img_com_clique_duplo("img_remark/clicar_em_vespertino")

        clica_no_gabarito()

        localiza_img_com_clique("img_remark/clicar_adicionar_tudo")

        localiza_img_com_clique("img_remark/clicar_ler_gabaritos")

        time.sleep(4)

        localiza_img_com_clique_com_mais_precisao(
            "img_remark/clicar_em_avaliacao_avancada"
        )

        localiza_img_com_clique("img_remark/clicar_gabarito_de_resposta")

        localiza_img_com_clique("img_remark/importa_repostas")

        localiza_img_com_clique("img_remark/clicar_linha_de_conjunto")

        localiza_img_com_clique("img_remark/clicar_em_importar_chave")

        time.sleep(1)
        localiza_img_com_clique("img_remark/clicar_em_avaliar")

        localiza_img_com_clique("img_remark/nao_salva_gabarito")

        time.sleep(0.5)

        localiza_img_com_clique_com_mais_precisao("img_remark/clicar_em_dados")

        localiza_img_com_clique("img_remark/clicar_em_exportar_dados")

        localiza_img_com_clique("img_remark/clicar_nome_do_arquivo")
        time.sleep(0.5)

        # Coloca o código da prova como nome

        arquivo_notas_txt = f"OK - {nome_da_pasta_antiga[0]}"
        pyautogui.write(arquivo_notas_txt)

        localiza_img_com_clique("img_remark/clicar_seta_para_baixo")

        time.sleep(0.5)

        localiza_img_com_clique("img_remark/clicar_em_documentos")

        time.sleep(0.5)

        localiza_img_com_clique_duplo("img_remark/clicar_na_pasta_de_provas")

        time.sleep(0.5)
        localiza_img_com_clique_duplo("img_remark/clicar_em_corrigidas")

        localiza_img_com_clique("img_remark/clicar_em_avancado")

        localiza_img_com_clique("img_remark/desmarcar_todo")

        localiza_img_com_clique("img_remark/clicar_em_carregar")

        if n_questoes_da_pasta == 20:
            localiza_img_com_clique_duplo("img_remark/sel_arq_id_e_nota")
        elif n_questoes_da_pasta == 25:
            localiza_img_com_clique_duplo("img_remark/25_sel_arq_id_e_nota_25")
        elif n_questoes_da_pasta == 30:
            localiza_img_com_clique_duplo("img_remark/30_sel_arq_id_e_nota_30")
        elif n_questoes_da_pasta == 35:
            localiza_img_com_clique_duplo("img_remark/35_sel_arq_id_e_nota_35")
        else:
            print("Nenhum arquivo encontrado!")

        localiza_img_com_clique("img_remark/clicar_em_ok")

        if turno == turnos[0]:
            print(f"Clicar em: {turno}")
            localiza_img_com_clique_duplo("img_remark/clicar_em_madrugada")

        elif turno == turnos[1]:
            print(f"Clicar em: {turno}")
            localiza_img_com_clique_duplo("img_remark/clicar_em_matutino")

        elif turno == turnos[2]:
            print(f"Clicar em: {turno}")
            localiza_img_com_clique_duplo("img_remark/clicar_em_vespertino")

        localiza_img_com_clique("img_remark/clicar_em_ok_para_salvar")

        time.sleep(0.5)

        localiza_img_com_clique("img_remark/fechar_quick_starts")

        time.sleep(1)

        localiza_img_com_clique_com_mais_precisao("img_remark/fechar_modelo")

        localiza_img_com_clique("img_remark/nao_salva_modelo")

        maximizar_ou_minimizar(titulo_remark, False)

        arquivo_notas = rf"C:/Users/douglas.lopes/Documents/Provas_para_lancamentos/Corrigidas/{turno}/{arquivo_notas_txt}"
        subprocess.Popen(["start", "notepad.exe", arquivo_notas], shell=True)

        time.sleep(2)

        pyautogui.hotkey("ctrl", "h")

        time.sleep(1)

        localiza_img_com_clique("notepad/substituir_tudo")

        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "s")

        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "w")

        time.sleep(0.5)

        maximizar_ou_minimizar(titulo_remark, True)

        print(nome_da_pasta_antiga[0])
        altera_nome_da_pasta(turno, pasta, False)

        nome_da_pasta_antiga.pop(0)
