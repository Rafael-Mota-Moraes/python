# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# {'Pergunta': 'Quanto é 2+2?', 'Opções': ['1', '3', '4', '5'], 'Resposta': '4'}

acertos = 0


for pergunta in perguntas:
    print(pergunta.get('Pergunta'))
    
    for opcao in pergunta.get('Opções'):
        print(opcao)

    opcao_usuario = input('Digite sua resposta: ')

    if opcao_usuario not in pergunta.get('Opções'):
        print('Selecione uma opção válida!')
        break

    resposta = pergunta.get('Resposta')

    if opcao_usuario == resposta:
        acertos += 1
        print('Certa resposta!')
    else:
        print('Errou!')

    print(f'Você acertou {acertos} de {len(perguntas)}')
