from interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True
    

def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO... Ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            print(linha)
    finally:
        a.close()


def cadastrar(arq, nome='desconheido', validacao=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ouve um erro ao cadastrar...')
    else:
        try:
            a.write(f'Nome:{nome:<25} CPF:{validacao}\n')
        except:
            print('\033[31mErro\033[m')
        else:
            print(f'Novo registro de {nome} Adicionado!')
            a.close()

def cpf(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Digite seu CPF corretamente!') 
            continue
        except:
            if len(num) == 11:
                return n
            else:
                print('Erro...CPF INVALIDO!')
        