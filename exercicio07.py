for i in range(1,6):
    nome = input(f"{i}º Nome: ")
    p1 = float(input("Prova 01: "))
    p2 = float(input("Prova 02: "))
    p3 = float(input("Prova 03: "))
    md = (p1+p2+p3)/3
    if md >= 7:
        sit = "ap"
    elif md >= 6:
        sit = "rc"
    else:
        sit = "rp"
    print("\n---Resultado---")
    print(f"Aluno: {1}")
    print(f"Nome: {nome}")
    print(f"Prova 1: {p1}")
    print(f"Prova 2: {p2}")
    print(f"Prova 3: {p3}")
    print(f"Media: {md}")
    print(f"Situação: {sit}")
    print(f"\n")
    