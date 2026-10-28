print("Menu: ")
print("1 - par ou impar")
print("2 - compare o número")
print("3 - calcule o dobro")
resposta = "sim"
while resposta == "sim":
    opção = int(input("Escolha uma opção: "))
    match opção:
    case 1:
    print("Par ou impar")
    numero = int(input("Numero: "))
    if numero %2 == 0: 
        print(f"{numero} é par.")
        else:
            print(f"{numero} é impar.")
    case 2:
    print("Compare os números")
    n1 = int(input("1º Número: "))
    n2 = int(input("2º Número: "))
    inf n1 > n2:
    print(f"{n1} é maior que {n2}")
    elif n1 < n2:
        print(f"{n1} é menir que {n2}")
        else:
            print(f"{n1} é igual a {n2}")
            case 3:
            print("Dobro")
            num = int(input("Escolha um número: "))
            dobro = num * 2
            print(f"O dobro de {num} é {dobro}")
            case _:
            print("Opção Inválida")
        resposta = input("Deseja continuar? (sim ou não)")
        if resposta = "sim"
        print("Programa encerrado")
        break