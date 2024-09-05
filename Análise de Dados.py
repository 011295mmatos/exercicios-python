contador_idade = 0
contador_feminino = 0
contador_masculino = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'FfMm':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        contador_idade = contador_idade + 1
    if sexo in 'mM':
        contador_masculino = contador_masculino + 1
    if idade <=   20 and sexo in 'Ff':
        contador_feminino = contador_feminino + 1

    escolha_usario = ' '
    while escolha_usario not in 'SsNn':
        escolha_usario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if escolha_usario in 'nN':
        break

print(f'Total de pessoas com mais de 18 anos: {contador_idade}\nAo todo temos {contador_masculino} homens cadastrados\nE temos {contador_feminino} mulher com menos de 20 anos')
