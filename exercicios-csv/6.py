import csv

dados = [
    ['nome','nota1','nota2','nota3'],
    ['Ana',7.5,8.0,9.0],
    ['Beto',5.0,6.0,4.5],
    ['Carla',9.0,9.5,10.0],
    ['Diego',6.0,7.0,5.5],
]

with open('exercicios-csv/notas.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

#A)
'''
with open('exercicios-csv/notas.csv', 'r', encoding='utf-8') as arquivo:
    turma = csv.DictReader(arquivo)
    for a in turma:
        print(a['nome'], a['nota1'], a['nota2'], a['nota3'])

'''
#B)

with open('exercicios-csv/notas.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for a in leitor:
        a['nota1'] = float(a['nota1'])
        a['nota2'] = float(a['nota2'])
        a['nota3'] = float(a['nota3'])
        media = (a['nota1'] + a['nota2'] + a['nota3']) / 3
        if media >= 6:
            print(f'{a['nome']} - Média: {media:.2f} - Aprovado')
        else:
            print(f'{a['nome']} - Média: {media:.2f} - Reprovado')