from my_io_utils import enter_limpar_tela, mostrar_texto, obter_numero
from play_number_features import filtrar, gerar_vetor, localizar_posicoes, mapear
from play_numbers_utils import bye


def main():
    opcoes = menu()
    numeros = []

    opcao = obter_numero(opcoes)

    while opcao != 0:
        if opcao == 1:
            numeros = gerar_vetor()
        elif opcao == 2:
            mostrar_texto(f"Existem {len(numeros)} itens.")
        elif opcao == 3:
            mostrar_texto(numeros)
        elif opcao == 4:
            localizar_posicoes(numeros)
        elif opcao == 5:
            mostrar_texto("Antes: ")
            mostrar_texto(numeros)
            n = obter_numero('N: ')
            numeros = mapear(numeros, lambda i: i * n)
            mostrar_texto("Depois: ")
            mostrar_texto(numeros)
        elif opcao == 6:
            mostrar_texto("Antes: ")
            mostrar_texto(numeros)
            n = obter_numero('N: ')
            numeros = mapear(numeros, lambda i: i + n)
            mostrar_texto("Depois: ")
            mostrar_texto(numeros)
        elif opcao == 7:
            mostrar_texto("Antes: ")
            mostrar_texto(numeros)
            numeros = mapear(numeros, lambda i: i * 2 if i % 2 == 0 else i)
            mostrar_texto("Depois: ")
            mostrar_texto(numeros)
        elif opcao == 8:
            mostrar_texto("Antes: ")
            mostrar_texto(numeros)
            mostrar_texto("Filtrados: ")
            mostrar_texto(filtrar(numeros, lambda i: i % 2 == 0))
        elif opcao == 9:
            mostrar_texto("Antes: ")
            mostrar_texto(numeros)
            mostrar_texto("Filtrados: ")
            mostrar_texto(filtrar(numeros, lambda i: i % 2 != 0))

        enter_limpar_tela()
        opcao = obter_numero(opcoes)

    bye()


def menu():
    menu_options = "***** Play Numbers *****"
    menu_options += "\n-----------------------"
    menu_options += "\n1 - Gerar Números"
    menu_options += "\n2 - Mostrar Qtd Números gerados"
    menu_options += "\n3 - Mostrar números"
    menu_options += "\n4 - Buscar número"
    menu_options += "\n5 - Multiplicar números por N"
    menu_options += "\n6 - Somar N aos números"
    menu_options += "\n7 - Dobrar números pares"
    menu_options += "\n8 - Mostrar pares"
    menu_options += "\n9 - Mostrar ímpares"
    menu_options += "\n0 - Sair"
    menu_options += "\n\n>> "

    return menu_options


def dobra_pares(valor):
    if valor % 2 == 0:
        return valor * 2

    return valor


def fabrica_somadora(valor):
    def filha(numero):
        return numero + valor

    return filha


def fabrica_multiplicadora(valor):
    def filha(numero):
        return numero * valor

    return filha


main()
