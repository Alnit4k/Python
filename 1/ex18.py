arquivo = float(input('Qual o tamanho do arquivo em MB '))
net = float(input('Qual a velocidade da sua internet MB/s '))
cal = (arquivo/(net/8))

print (f'O seu aquivo vai demorar {cal} segundos para finalizar o download')