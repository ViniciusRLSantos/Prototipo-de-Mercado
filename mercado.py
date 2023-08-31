from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main():
    menu()


def menu():
    print('=======================================')
    print('============ Bem-vind@ ================')
    print('============ Loja Show ================')
    print('=======================================')

    print('Selecione uma opção abaixo')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida')
        menu()


def cadastrar_produto():
    print('Cadastro de Produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos():
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('--------------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados nessa loja.')
    sleep(2)
    menu()


def comprar_produto():
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho')
        print('------------------------------------------------------------')
        print('=================== Produtos Disponíveis ===================')
        for produto in produtos:
            print(produto)
            print('------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                item_existe: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'O produto {produto.nome} agora possui {quantidade + 1} unidades no carrinho.')
                        item_existe = True
                        sleep(2)
                        menu()
                if not item_existe:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {prod.nome} foi adicionado ao carrinho.')
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
    else:
        print('Ainda não existem produtos para vender')
    sleep(2)
    menu()


def visualizar_carrinho():
    if len(carrinho) > 0:
        print('Produtos no carrinho:')
        print('--------------------')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('--------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def fechar_pedido():
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        print('--------------------')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
        sleep(1)
        print(f'Sua fatura é: {formata_float_str_moeda(valor_total)}')
        print('Volte sempre')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho')
    sleep(2)
    menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    menu()
