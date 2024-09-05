condicao = 's' and 'S'
soma_numeros = 0
contador = 0
media = 0
maior_valor = 0
menor_valor = 0

while condicao in 'Ss':
    numero = int(input('Digite um número: '))
    condicao = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    soma_numeros = soma_numeros + numero
    if contador == 0:
        maior_valor = numero
        menor_valor = numero
    else:
        if numero > maior_valor:
            maior_valor = numero
        elif numero < menor_valor:
            menor_valor = numero
    contador = contador + 1

media = soma_numeros / contador

if contador > 1:
    print('\nVocê digitou {} números e a média foi {}'.format(contador, media))
else:
    print('\nVocê digitou {} número e a média é {}'.format(contador, media))

print('O maior valor foi {} e o menor foi {}'.format(maior_valor, menor_valor))
