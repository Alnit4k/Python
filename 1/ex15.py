time = int(input('Quantas horas o funcionario trabalhou? '))
money = int(input('Quanto  é a hora dele? '))

a = time*money
b2 = (a*-0.08)
b= b2+a
c2=(a*-0.05)
c= c2+a
d = a+(b2+c2)

print(f' O salario bruto do trabalhador é R${a}\n O valor de INSS é R${b}\n O valor pago para o sindicato é R${c}\n O valor do salario liquido é R${d}\n')


