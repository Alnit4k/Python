#4 notas = 4 inputs
#10 alunos diferentes = 10 usuarios diferentes
#calcular a media aritimetca de cada
#colocar a medica de cada aluno numa lista 
#imprimir o nome de alunos com media maior == a 7

alunos = []
media =[]

#Adicionar mais 10 inputs e range 10 para ficar conforme o exercicio solicita
for i in range(2):
    user=input('Digite o nome do {}° aluno: ' .format(i+1))
    alunos.append(user)
    nota1 = int(input('Digite a 1° nota do {}° aluno: ' .format(i+1)))
    nota2 = int(input('Digite a 2°  nota do {}° aluno: ' .format(i+1)))
    final = (nota1+nota2)/2
    media.append(final)
   
#contador de notas  
acima = 0 

#incrementa quantas vezes tiver uma nota acima de 7 na lista "media"
for nota in media:
    if nota > 7:
        acima += 1
    

print(acima)
print(alunos)
print(media)