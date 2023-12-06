import time
import pyautogui
from pywinauto.application import Application
from util import *

pyautogui.FAILSAFE = True

# app = Application().start(
#     "C:/Users/douglas.lopes/Desktop/sqldeveloper/sqldeveloper.exe"
# )

localiza_img_com_clique_duplo("sql_developer/clicar_no_prime")


def escreve_query():
    localiza_img_com_clique("sql_developer/clicar_na_query")
    with open("sql.txt", "r") as sql:
        conteudo = sql.read()
        pyautogui.press("shift")
        pyautogui.write(conteudo)
        pyautogui.keyUp("shift")


def apagar_query():
    localiza_img_com_clique("sql_developer/clicar_query_conteudo")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    print("Conteúdo apagado")


arquivos_questoes = {
    20: "A20 - 20 Quest",
    25: "B25 - 25 Quest",
    30: "C30 - 30 Quest",
    35: "D35 - 35 Quest",
    40: "E40 - 40 Quest",
}


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


# Caminho para a imagem que você deseja verificar
caminho_imagem = "img/word_clicar_ok_aviso.png"


# Abre cod_prova.txt e processa cada linha
with open("cod_prova.txt", "r") as cod_prova:
    # Lê todas as linhas de gabarito_cod.txt antes do loop principal
    with open("gabarito_cod.txt", "r") as gabarito_cod:
        linhas_gabarito_cod = gabarito_cod.readlines()

    for linha, linha_gabarito in zip(cod_prova, linhas_gabarito_cod):
        # Cola query
        escreve_query()

        # Seleciona o campo da query
        pyautogui.click(button="right", duration=1)

        # Formata a query
        localiza_img_com_clique("sql_developer/formatar_query")

        codigo_prova = linha.split(",")[0]

        codigo_turma = linha.split(",")[1:]

        # Adiciona o código da prova na consulta
        localiza_img_com_clique_duplo("sql_developer/clicar_no_codigo_prova")
        pyautogui.write(codigo_prova.upper())

        time.sleep(1)
        # Adiciona as turmas
        localiza_img_com_clique_duplo("sql_developer/clicar_na_turma")

        # Adiciona % a cada valor
        codigo_turma_conditions = " OR ".join(
            [f"TURMA_BASE LIKE '{valor.strip()} 23/2%'" for valor in codigo_turma]
        ).upper()

        # Adiciona OR entre cada valor de TURMA_BASE LIKE se houver mais de um código de turma
        if len(codigo_turma) > 1:
            pyautogui.write(f"{codigo_turma_conditions}")
        else:
            pyautogui.write(codigo_turma_conditions)
        time.sleep(1)

        # Clica rodar query
        localiza_img_com_clique("sql_developer/clicar_rodar_query")

        # Apaga a query
        apagar_query()

        # Clica em confirmado
        localiza_img_com_clique("sql_developer/clicar_situacao_contrato")
        pyautogui.click(button="right", duration=1)

        # Clica em exportar
        localiza_img_com_clique("sql_developer/clicar_exportar")

        # Clica em formato
        localiza_img_com_clique("sql_developer/clicar_em_insert")

        # Procura excel 2003
        pyautogui.doubleClick(982, 496, duration=1)

        # Seleciona excel 2003
        pyautogui.click(920, 497, duration=1)

        # Altera o nome do arquivo
        localiza_img_com_clique_duplo("sql_developer/alterar_exportar")
        pyautogui.write(
            f"Documents\gabaritos_alunos\{codigo_prova}\{codigo_prova}.xlsx"
        )

        time.sleep(1)

        # Clica em próximo
        localiza_img_com_clique("sql_developer/clicar_em_proximo")

        # Clica em sim para confirmar a criação do diretório
        localiza_img_com_clique("sql_developer/clicar_em_sim")

        # Clica em finalizar
        localiza_img_com_clique("sql_developer/clicar_em_finalizar")

        # Abre o Word
        app = Application().start(
            "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
        )

        # localiza_img_com_clique("sql_developer/clicar_abrir_word")

        # para pegar o gabarito correspondente
        codigo_prova_questoes = linha_gabarito.split(",")[0]
        prova_questoes = int(linha_gabarito.split(",")[1])

        print(f"Código da prova: {codigo_prova_questoes}, Questões: {prova_questoes}")
        # Verifica se a quantidade de questões está no dicionário
        # Adiciona prints para verificar os valores
        print(f"Código da prova no arquivo: {codigo_prova}")
        print(f"Código da prova no gabarito: {codigo_prova_questoes}")
        print(f"Questões no gabarito: {prova_questoes}")

        # Verifica se a quantidade de questões está no dicionário
        if prova_questoes in arquivos_questoes:
            print(f"Questões encontradas no dicionário: {prova_questoes}")

            # Verifica se os códigos da prova são iguais
            if codigo_prova_questoes == codigo_prova:
                print(f"Selecionando arquivo: {arquivos_questoes[prova_questoes]}")

                # Seleciona o arquivo correspondente
                localiza_gabaritos(arquivos_questoes[prova_questoes])
            else:
                print("Códigos da prova não correspondem.")

        # Seleciona as correspondecias
        localiza_img_com_clique("word/clicar_em_coreespondecias")

        # Selecionar Destinatários
        localiza_img_com_clique("word/clicar_em_destinatarios")

        time.sleep(2)

        # Usar uma lista existente
        localiza_img_com_clique("word/clicar_em_lista_existente")

        # Seleciona o caminha no explorador de arquivos
        localiza_img_com_clique("word/clicar_em_minhas_fontes_de_dados")
        pyautogui.write(
            f"C:/Users/douglas.lopes/Documents/gabaritos_alunos/{codigo_prova}"
        )

        # Navega até o caminho
        localiza_img_com_clique("word/navegar_ate_o_dir")

        # Seleciona o arquivo xlsx
        localiza_img_com_clique_duplo("word/clicar_no_xlsx")

        # Clicar em exportar
        localiza_img_com_clique_duplo("word/clicar_exportar")

        # Clicar em mesclar
        localiza_img_com_clique("word/clicar_mesclar")

        time.sleep(1)

        # Clica em Imprimir Documentos
        localiza_img_com_clique("word/clicar_em_documentos_individuais")

        # Clica em OK
        localiza_img_com_clique("word/clicar_em_ok")

        time.sleep(1)

        # Clica no aviso
        # Caminho para a imagem que você deseja verificar
        caminho_imagem = "img/word/clicar_ok_aviso.png"

        # Verifica se a imagem está na tela e pressiona "enter" se encontrada
        # if pyautogui.locateOnScreen(caminho_imagem):
        #     pyautogui.press("enter")
        # else:
        #     print("A imagem não foi encontrada")

        time.sleep(1)

        # Clica em arquivo
        localiza_img_com_clique("word/clicar_em_arquivo")

        # Clica salvar como
        localiza_img_com_clique("word/clicar_em_salvar_como")

        # Clicar em mais opções
        localiza_img_com_clique("word/clicar_em_mais_opcoes")

        # Clica na pesquisa
        pyautogui.click(1021, 254, duration=1)
        pyautogui.write(
            f"C:/Users/douglas.lopes/Documents/gabaritos_alunos/{codigo_prova}"
        )
        pyautogui.click(1089, 258, duration=1)

        # Altera o nome do arquivo
        pyautogui.doubleClick(545, 601, duration=0.5)
        pyautogui.write(codigo_prova)

        # Salva arquivo word
        localiza_img_com_clique("word/clicar_em_salvar")

        # Fecha o word com os alunos
        localiza_img_com_clique("word/clicar_em_fechar")

        # Fecha o word sem os alunos
        localiza_img_com_clique("word/clicar_em_fechar")

        # Clique em não salvar quando fechar o word
        localiza_img_com_clique("word/clicar_em_nao_salvar")

        # Reabre o sql
        localiza_img_com_clique("word/clicar_icone_sqldev")
