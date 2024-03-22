from arquivo import *
from interface import *
arq = 'AlistamentoMilitar.txt'
if not arquivoExiste(arq):
    criararquivo(arq)
#Um lup infinito para o usuario escolher oque desejar!
#se escolher 3 sairá do programa
while True:
    cabeçalho('\033[32mAlistamento Militar!\033[m')
    resposta = menu(['Alistar', 'Ver Alistados', 'Sair do Sistema'])
    if resposta == 1:
        nome = str(input('Digite seu NOME: '))
        validacao = cpf('CPF: ')
        if len(validacao) == 11:
            cadastrar(arq, nome, validacao)
        else:
            print('ERRO na numeração do CPF!')
        print(linha())
    elif resposta == 2:
        lerarquivo(arq)
    elif resposta == 3:
        print('Até Logo!!!')
        break
    else:
        print('\033[31mERRO...Digite 1, 2 ou 3!!!\033[m')
        print(linha())
