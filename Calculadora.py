print('<------------------------>')
print('<-------Calculadora------>')
print('<------------------------>')

'''Entradas de dados'''
Menu = int (input('\nEscolha uma operação: \n\nAdição[1] \nSubtração[2] \nMultiplicação[3] \nDivisão[4] \nExpoente[5] \nOperação: '))
if Menu >= 6:
    print('Operação inválida!')
else:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))


'''Processamento e Saídas'''

if Menu == 1:
    print('Resultado: ', n1 + n2)
elif Menu == 2:
    print('Resultado: ', n1 - n2)
elif Menu == 3:
    print('Resultado: ', n1 * n2)
elif Menu == 4:
    print('Resultado: ', n1 / n2)
elif Menu == 5:
    print('Resultado: ', n1 ** n2)
