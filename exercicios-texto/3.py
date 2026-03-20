from datetime import datetime

a = input("Digite seu texto no seu Diario(shhhhh segredo): ")

agora = datetime.now().strftime('%d/%m/%Y %H:%M')

with open('exercicios-texto/diario.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(f'| Anotação em {agora} ')
    arquivo.write(f'{a} \n')
