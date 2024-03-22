TipoEncadernacao = input("(Escreva: 'airo' ou 'espiral' ou 'capadura')\nQual o tipo da encadernação? ")
#Process
if TipoEncadernacao == 'airo':
    ValAiro= float(input("Qual a quantidade de folhas? "))
    if ValAiro <= 100:
        print("Preço do airo sairá R$15,00")
    if ValAiro > 100 and ValAiro <= 150:
        print("Preço do airo sairá R$20,00")
    if ValAiro > 100 and ValAiro > 150 and ValAiro <= 250:
        print("Preço do airo sairá R$25,00")