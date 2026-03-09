def vypis(vysledek):
    for i in vysledek:
        print(i, ",")

def delitel(cislo):
    vysledek = []
    for i in range(100):
        if i == 0:
            break
        mini_vysledek = cislo%i
        if mini_vysledek == 0 :
            i.__add__(vysledek)
        else:
            break
    print("Tvoje cislo je delitelne: ", vypis(vysledek))


delitel(58)