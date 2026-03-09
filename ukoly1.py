import csv 
sladkost = []
velikost = []
prumers = 0
prumerv = 0
cesta = r"C:\Users\st025547\Downloads\Banana_Quality-main\Banana_Quality-main\banana_quality.csv"

with open(cesta, "r", encoding="utf-8") as file:
    for radek in csv.DictReader(file):
        if float(radek["Weight"]) >= 1:
            if float(radek["Sweetness"]) >= 3.5:
                sladkost.append(float(radek["Sweetness"]))
                velikost.append(float(radek["Weight"]))
prumers = sum(sladkost) / len(sladkost)
prumerv = sum(velikost) / len(velikost)

print("Velke banany jsou prumerne ", prumers," jednotek sladke a ", prumerv, " kilo tezke.")