import csv

dados = [
    ['nome','nota1','nota2']
]

for i in range(0,3):
    a = input("Digite o nome do aluno: ")
    b = input("Digite a primeira nota do aluno: ")
    c = input("Digite a segunda nota do aluno: ")

    dados.append([a,b,c])

with open('exercicios-csv/turma.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

with open('exercicios-csv/turma.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)