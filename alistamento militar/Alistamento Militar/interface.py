#função para mostrar uma nova linha na cor verde!
def linha(tam = 42):
    return '\033[32m-\033[m' * tam
#função para titulo (cabaçalho)
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#função para ler um número INTEIRO, (tratamento de erros usando excesão)
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO... POR FAVOR DIGITE UM NÚMERO INTEIRO!\033[m')
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
    opc = leiaint('\033[36mDigite sua Opção:\033[m')
    return opc
