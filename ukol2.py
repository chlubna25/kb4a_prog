import csv
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

X_roky = []
Y_hodnoty = []

with open(r"C:\Users\st025547\Downloads\kb4a_prog-main\Global_Homicide_Rate_1970_2025.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        X_roky.append([int(row["Year"])]) 
        Y_hodnoty.append(float(row["Global_Avg"]))
scaler = StandardScaler()
X_roky_upravene = scaler.fit_transform(X_roky)
neural_network = MLPRegressor(
    hidden_layer_sizes=(10, 10, 10), 
    activation="relu",
    max_iter=5000, 
    random_state=42
)

neural_network.fit(X_roky_upravene, Y_hodnoty)
hledany_rok = [[2030]] 
hledany_rok_upraveny = scaler.transform(hledany_rok) 
vysledek = neural_network.predict(hledany_rok_upraveny)
print(f"Predikce průměru vražd pro rok {hledany_rok[0][0]}: {vysledek[0]:.2f}")
vsechny_predikce = neural_network.predict(X_roky_upravene)
plt.plot(X_roky, Y_hodnoty, label='Skutečná historická data', color='blue')
plt.plot(X_roky, vsechny_predikce, label='Křivka, kterou síť pochopila', color='red', linestyle='dashed')
plt.title("Závislost průměru vražd na čase")
plt.xlabel("Rok")
plt.ylabel("Globální průměr vražd")
plt.legend()
plt.show()
