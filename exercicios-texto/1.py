with open('exercicios-texto/frutas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Tomate\n')
    arquivo.write('Wait\n')
    arquivo.write('Maçã\n')
    arquivo.write('Banana\n')
    arquivo.write('Goaba\n')
    
with open('exercicios-texto/frutas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())