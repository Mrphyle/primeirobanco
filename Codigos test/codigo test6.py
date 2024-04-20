ops = input("\n____________\nSubconjunto\nAuB\nAnB\ncomplemento\nDigite qual conjunto desejá: ")

if ops.lower() == 'subconjunto':
    opsc = int(input("Desejá quantos elementos? "))
    A = set()
    for i in range(opsc):
        save1 = int(input("Digite o elemento que deseja: "))
        A.add(save1)
    subconjunte= len(A)
    print(f"{2**subconjunte}")
elif ops.lower() == 'aub':
    CAbc = input("_____________\nAuB ou AuBuC\nQual união desejá: ")
    if CAbc == 'aub':
        opsc1 = int(input("Desejá quantos elementos no  conunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        B = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        R = A.union(B)
        print(R)
    elif CAbc == 'aubuc':
        opsc1 = int(input("Desejá quantos elementos no  conunto A? "))
        A = set()
        for i in range(opsc1):
            save1 = int(input("Digite o elemento que deseja: "))
            A.add(save1)
        opsc2 = int(input("Desejá quantos elementos no conjunto B? "))
        B = set()
        for i in range(opsc2):
            save2 = int(input("Digite o elemento que deseja: "))
            B.add(save2)
        opsc3 = int(input("Desejá quantos elementos no conjunto C? "))
        C = set()
        for i in range(opsc3):
            save3 = int(input("Digite o elemento que deseja: "))
            C.add(save3)
        R = A.union(B and C)
        print(R)