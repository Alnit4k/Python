con = {'b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z'}
#sets só funcionam com dicionario

frase = input('Digite até 10 caracteres pare serem lidos: ').lower()

frase = frase[:10]
dic= set(frase)

dic.discard(' ')
#Posso usar a função discard para tirar algo que eu não quero na minha lista
entre = con & dic
tamanho = len(entre)

print(entre, tamanho)