print('------------------')
print('*-* Exercícios *-*')
print('------------------')

#entrada de dados
nome = input('Aluno: ')
n1 = float(input('N1: '))
n2 = float(input('N2: '))
n3 = float(input('N3: '))

#processamento

media = (n1+n2+n3)/3

# Determina o conceito com base na média

if media >= 9 and media <= 10:
    status = 'aprovado'
    conceito = 'A'
    mensagem = 'Excelente'
elif media >= 8 and media <= 9:
    status = 'aprovado'
    conceito = 'B'
    mensagem = 'Ótimo'
elif media >= 7 and media <= 8:
    status = 'aprovado'
    conceito = 'C'
    mensagem = 'Bom'
elif media >= 6 and media <= 7:
    status = 'aprovado'
    conceito = 'D'
    mensagem = 'Regular'
else:
    status = 'Reprovado'
    conceito = 'E'
    mensagem = 'Ruim'


match conceito:
    case 'A':
        print(f'Nome: {nome}, você está {status}!')
        print(f'Média: {media:.1f} - Conceito: {conceito} \nMensagem: {mensagem}')
    case 'B':
        print(f'Nome: {nome}, você está {status}!')
        print(f'Média: {media:.1f} - Conceito: {conceito} \nMensagem: {mensagem}')
    case 'C':
        print(f'Nome: {nome}, você está {status}!')
        print(f'Média: {media:.1f} - Conceito: {conceito} \nMensagem: {mensagem}')
    case 'D':
        print(f'Nome: {nome}, você está {status}!')
        print(f'Média: {media:.1f} - Conceito: {conceito} \nMensagem: {mensagem}')
    case 'E':
        print(f'Nome: {nome}, você está {status}!')
        print(f'Média: {media:.1f} - Conceito: {conceito} \nMensagem: {mensagem}')





