#função para mostrar uma nova linha na cor verde!
def linha(tam = 42):
    return '\033[32m-\033[m' * tam
#função para titulo (cabaçalho)
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#função para ler um número INTEIRO, (tratamento de erros usando excesão)
def laiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO... POR FAVOR DIGITE UM NÚMERO INTEIRO!\033[m1')
            continue
        except KeyboardInterrupt:
            print('\033[33mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n

#Um menu ao qual o usuário escolhera entre a opção 1, 2 ou 3, e oque ele escolher terá um retorno
def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[34m{c}\033[m - \033[33m{item}\033[m')
        c += 1
    print(linha())
    opc = laiaint('\033[36mDigite sua Opção:\033[m')
    return opc


#Um lup infinito para o usuario escolher oque desejar!
#se escolher 3 sairá do programa
while True:
    cabeçalho('\033[32mAlistamento Militar!\033[m')
    resposta = menu(['Alistar', 'Ver Alistados', 'Sair do Sistema'])
    if resposta == 1:
        print('Alistar')
        print(linha())
    elif resposta == 2:
        print('Ver alistados')
        print(linha())
    elif resposta == 3:
        print('Até Logo!!!')
        break
    else:
        print('\033[31mERRO...Digite 1, 2 ou 3!!!\033[m')
        print(linha())
