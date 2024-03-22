ensemble = {'maça','pera','uva','caqui','jaca','ameixa','jambo'}
for fruit in ensemble:
    print(fruit)
    ensemble.add(input("Digite uma fruta"))
    for fruit in ensemble:
        print(fruit)