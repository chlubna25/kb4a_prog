import csv
import matplotlib.pyplot as plt
cesta = r"2. prace_se_soubory\data\teploty.csv"

with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    roky= []
    teploty_rano= []
    for radek in reader:
        if radek ["TIME"] == "AVG":
            print(radek["YEAR"], radek ["TEMPERATURE"])
            teplota = float(radek["TEMPERATURE"])
            teploty_rano.append(teplota)
            rok = int(radek["YEAR"])
            roky.append(rok)
    
    prumer = sum(teploty_rano) /len(teploty_rano)
    print(f"Průměrné ranní teploty jsou {round(prumer, 2)} Celsius")

    plt.bar(roky,teploty_rano)
    plt.title("prumerne ranni teploty v čr")
    plt.xlabel("Rok")
    plt.ylabel("teploty [C]")
    plt.show()