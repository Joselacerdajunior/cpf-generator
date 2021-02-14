from random import randint

while True:
    # Gerar numero aleatório
    cpf = str(randint(10000000000, 99999999999))

    cpfList = []
    cpfList_result_01 = []
    cpfList_result_02 = []
    sumL1 = 0
    sumL2 = 0
    dig_01 = 0
    dig_02 = 0
    finalCPF = ''
    formatedCpfList = []
    formatedFinalCPF = ''

    if len(cpf) != 11 or not cpf.isnumeric():
        print('ERROR! Quantidade ou tipo de caracter inválido!')
    else:
        # cria uma lista com os números
        cpfList = list(cpf)
        # remover os dois ultimos digitos da lista
        cpfList.pop()
        cpfList.pop()

        # inicio do digito 01
        for x, y in enumerate(range(10, 1, -1)):
            multiplicacao = int(cpfList[x]) * y
            cpfList_result_01.append(multiplicacao)

        for x in cpfList_result_01:
            sumL1 += x

        x = 11 - (sumL1 % 11)
        dig_01 = 0 if (x>9) else x
        cpfList.append(str(dig_01))

        # inicio do digito 02
        for x, y in enumerate(range(11, 1, -1)):
            multiplicacao = int(cpfList[x]) * y
            cpfList_result_02.append(multiplicacao)

        for x in cpfList_result_02:
            sumL2 += x

        x = 11 - (sumL2 % 11)
        dig_02 = x
        cpfList.append(str(dig_02))

        # adicionar formatos ao cpf
        formatedCpfList = cpfList.copy()
        formatedCpfList.insert(3, '.')
        formatedCpfList.insert(7, '.')
        formatedCpfList.insert(11, '-')
        formatedFinalCPF = ''.join(formatedCpfList)

        # transformar lista em string separados por uma caracter vazio
        finalCPF = ''.join(cpfList)

        if finalCPF == cpf:
            print(f'\nO CPF {formatedFinalCPF} é válido!')
            restart = input('Pressione ENTER para gerar novo CPF ...')