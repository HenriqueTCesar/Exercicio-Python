print('<------------------------>')
print('<-------Calculadora------>')
print('<------------------------>')

'''Entradas de dados'''
op = int (input('\nEscolha uma operação: \n\nAdição[1] \nSubtração[2] \nMultiplicação[3] \nDivisão[4] \nExpoente[5] \nOperação: '))
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))


'''Processamento e Saídas'''

match op:
    case 1:
        r = n1 + n2
        print(f'A soma de {n1} com {n2} é: {r:.2f}')
    case 2:
        r = n1 - n2
        print(f'A subtração de {n1} com {n2} é: {r}')
    case 3:
            r = n1 * n2
            print(f'A multiplicação de {n1} com {n2} é: {r}')
    case 4:
        if n2!=0:
            r = n1 / n2
            print(f'A divisão de {n1} com {n2} é: {r:.2f}')
        else:
            print('Divisão por ZERO!')
    case 5:
        r = n1 ** n2
        print(f'A potência de {n1} com {n2} é: {r}')
    case _:
        print('Operação inválida')
