print('-'*40)
print(' '*10,'LOJAS SUPER BARATÃO')
print('-'*40)

soma_produtos = 0
contador_produto = 0
comparador_valor = 0
contador_execucao = 0

while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = int(input('Preço: R$'))
    if contador_execucao == 0:
        comparador_valor = valor
        comparador_produto = produto
        contador_execucao = contador_execucao + 1

    soma_produtos = soma_produtos + valor

    if valor >= 1000:
        contador_produto = contador_produto + 1

    if valor < comparador_valor:
        comparador_valor = valor
        comparador_produto = produto

    usuario = ' '
    while usuario not in 'SsNn':
        usuario = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]

    if usuario in 'nN':
        print('-'*20,' FIM DO PROGRAMA ', '-'*20)
        break

print(f'O total da compra foi R${soma_produtos:.2f}')
print(f'Temos {contador_produto} produto custando mais de R$1.000,00')
print(f'O produto mais barato foi {comparador_produto} que custa R${comparador_valor:.2f}')