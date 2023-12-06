with open("cod_prova.txt", "r") as cod_prova_file:
    lines = cod_prova_file.readlines()

with open("gabarito_cod.txt", "r") as gabarito_cod_file:
    gabarito_lines = gabarito_cod_file.readlines()

new_lines = []
new_gabarito_lines = []

for linha, linha_gabarito in zip(lines, gabarito_lines):
    codigo_prova_questoes = linha_gabarito.split(",")[0]
    prova_questoes = int(linha_gabarito.split(",")[1])

    codigo_prova = linha.split(",")[0]
    codigo_turma = linha.split(",")[1:]

    if prova_questoes != 20:
        new_lines.append(linha)
        new_gabarito_lines.append(linha_gabarito)

with open("cod_prova.txt", "w") as cod_prova_file:
    cod_prova_file.writelines(new_lines)
