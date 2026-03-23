import csv

dados = [
    ['nome','nota','turma'],
    ['Ana',8.5,'1A'],
    ['Beto',7.0,'1A'],
    ['Carla',9.2,'1B'],
]

with open('como-fazer/turma.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

with open('como-fazer/turma.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)