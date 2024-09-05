titulo = 'BANCO CEV'
largura_total = 40

print('='*largura_total)
print(titulo.center(largura_total),'\nCédulas disponíveis: R$50,R$20,R$10,R$1 ')
print('='*largura_total)
saque_usuário = int(input('Que valor você quer sacar ?: R$'))
valor_sacado = 0
resto_sacado = 0
contador_nota_50 = 0
contador_nota_20 = 0
contador_nota_10 = 0
contador_nota_1 = 0
while True:
    while True:
        valor_sacado = valor_sacado + 50
        contador_nota_50 = contador_nota_50 + 1
        if valor_sacado > saque_usuário:
            valor_sacado = valor_sacado - 50
            contador_nota_50 = contador_nota_50 - 1
            break
    while True:
        valor_sacado = valor_sacado + 20
        contador_nota_20 = contador_nota_20 + 1
        if valor_sacado > saque_usuário:
            valor_sacado = valor_sacado - 20
            contador_nota_20 = contador_nota_20 - 1
            break
    while True:
        valor_sacado = valor_sacado + 10
        contador_nota_10 = contador_nota_10 + 1
        if valor_sacado > saque_usuário:
            valor_sacado = valor_sacado - 10
            contador_nota_10 = contador_nota_10 - 1
            break
    while True:
        valor_sacado = valor_sacado + 1
        contador_nota_1 = contador_nota_1 + 1
        if valor_sacado > saque_usuário:
            valor_sacado = valor_sacado - 1
            contador_nota_1 = contador_nota_1 - 1
            break

    if valor_sacado == saque_usuário:
        break

if contador_nota_50 > 0:
    print(f'Total de {contador_nota_50} cédulas de R$50')
if contador_nota_20 > 0:
    print(f'Total de {contador_nota_20} cédulas de R$20')
if contador_nota_10 > 0:
    print(f'Total de {contador_nota_10} cédulas de R$10')
if contador_nota_1 > 0:
    print(f'Total de {contador_nota_1} cédulas de R$1')
print('='*largura_total)
print(f'Total do valor SACADO = {valor_sacado}'.center(largura_total))
print('VOLTE SEMPRE')