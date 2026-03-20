with open('exercicios-texto/diario.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    a = 0
    pala = 0
    
    for i in linhas:
        a += 1
        sprit = i.split()
        for p in sprit:
            pala += 1
        
    print(f'Tem {a} linhas e {pala} palavras.')
    
    