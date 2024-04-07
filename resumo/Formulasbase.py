def mais_menos_vezes_Divisao():
    opcao = input("Somar\nSubtrair\nDividir\nMultiplicar\nO que deseja fazer? ")
    if opcao.lower() == 'somar':
        num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opcao.lower() == 'subtrair':
        num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
        print(f"{num1} - {num2} = {num1 - num2}")
    elif opcao.lower() == 'dividir':
        num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
        print(f"{num1} / {num2} = {num1 / num2}")
    elif opcao.lower() == 'multiplicar':
        num1, num2 = float(input("Digite o primeiro número: ")), float(input("Digite o segundo número: "))
        print(f"{num1} * {num2} = {num1 * num2}")
while True:
    mais_menos_vezes_Divisao()
    reset = input("Quer fazer outra operação? (Sim/Não): ")
    if reset.lower() != 'sim':
        break