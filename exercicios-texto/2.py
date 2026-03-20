while True:
    a = input("Digite os itens na lista de compras(Digite 'sair' para acabar de digitar): ")

    if a == 'sair':
        print('Sua lista de compras: \n')
        with open('exercicios-texto/lista.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                print(linha.strip())
                
        with open('exercicios-texto/lista.txt', 'w', encoding='utf-8') as arquivo:
            pass
        
        break
    else:
        with open('exercicios-texto/lista.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(a)