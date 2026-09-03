rada = input("Zadej číselnou řadu oddělenou mezerami: ")

cisla = list(map(int, rada.split()))

unikatni_cisla = list(set(cisla))

print("Číselná řada bez duplicit:")
print(unikatni_cisla)
