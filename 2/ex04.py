vogal = ['a','e','i','o','u']
consoante =['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','x']

letra = str(input('Informe uma letra ')).lower()

if letra in vogal:
    print('É uma vogal ')

elif letra in consoante:
    print('É uma consoante ')