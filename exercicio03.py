for i in range(1, 6):
    nome = input(f"Digite o nome do {i}º aluno: ")

    prova01 = float(input("Digite a nota da prova 1: "))
    prova02 = float(input("Digite a nota da prova 2: "))
    prova03 = float(input("Digite a nota da prova 3: "))

    media = (prova01 + prova02 + prova03) / 3

    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

    print("-----------------------")