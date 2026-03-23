import csv

dados = [
    ['nome','nota1','nota2','nota3','media'],
]

with open('exercicios-csv/notas.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for a in leitor:
        a['nota1'] = float(a['nota1'])
        a['nota2'] = float(a['nota2'])
        a['nota3'] = float(a['nota3'])
        media = (a['nota1'] + a['nota2'] + a['nota3']) / 3
        dados.append([a['nome'],a['nota1'], a['nota2'], a['nota3'], media])

with open('exercicios-csv/notas_com_media.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)