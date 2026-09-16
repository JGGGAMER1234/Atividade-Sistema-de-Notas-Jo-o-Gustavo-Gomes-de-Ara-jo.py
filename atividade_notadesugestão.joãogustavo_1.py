# Lista para armazenar até 50 notas
notas = [None for i in range(50)]
notas_id = 0


# Função que apresenta o menu principal
def print_menu():
    print("Aplicação de controle de notas!")
    print("1 - Inserir nota")
    print("2 - Apresentar média das notas")
    print("3 - Apresentar maior e menor notas")
    print("4 - Apresentar todas as notas")
    print("5 - Sair")


# Função que insere nova nota
def insert_nota(nova_nota):
    global notas_id

    notas[notas_id] = nova_nota
    notas_id += 1


# Função que apresenta a nota mínima
def min_nota(array):
    return min(array)


# Função que apresenta a nota máxima
def max_nota(array):
    return max(array)


while True:
    print_menu()
    opt = input()

    match opt:

        case "1":
            nota = float(input("Digite a nota: "))
            insert_nota(nota)

        case "2":
            media = sum(notas[:notas_id]) / notas_id
            print("Média:", media)

        case "3":
            notas_validas = notas[:notas_id]

            print("Menor nota:", min_nota(notas_validas))
            print("Maior nota:", max_nota(notas_validas))

        case "4":
            print("Notas:", notas[:notas_id])

        case "5":
            break


print("saindo...")
