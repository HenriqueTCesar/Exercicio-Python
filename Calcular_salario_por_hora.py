print('--------------------------')
print('*-* Calculo do salário *-*')
print('--------------------------')

#entrada de dados
horas_trabalhadas float(input('Quantas horas você trabalhou?': ))
valor_por_hora = float(input('Digite o valor por hora: '))

#processamento
salario = horas_trabalhadas + valor_por_hora

#saida de dados
print(f"O salário total é: R${salario:.2f}")
