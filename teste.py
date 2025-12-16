print(' ---- MadLibs ---- ')

lista = ['1) Digite um adjetivo para um lugar: ', '2) Digite um adjetivo para uma pessoa: ', '3) Digite um substantivo: ']


for pergunta in lista:
    resposta1 = input(pergunta).lower().strip().replace(" ", "")
    if resposta == '' or resposta == '' or resposta == '':
        print('voce ganhou')
    else: 
        print('Voce perdeu')

    