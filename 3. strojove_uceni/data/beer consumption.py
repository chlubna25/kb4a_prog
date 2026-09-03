import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

x = []
y = []

with open(r"E:\programko\kb4a_prog\3. strojove_uceni\data\alcohol-consumption.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        beer_2020 = float(row["2020_projection"])
        beer_2025 = float(row["2025_projection"])
        total = float(row["total_consumption"])

        if beer_2025 > 10:
            label = 2
        elif beer_2025 > 5:
            label = 1
        else:
            label = 0

        x.append([total, beer_2020])
        y.append(label)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

neural_network = MLPClassifier(
    hidden_layer_sizes=(16, 10),
    activation="relu",
    max_iter=1000,
    random_state=42
)

neural_network.fit(x_train, y_train)

y_pred = neural_network.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"přesnost: {accuracy * 100:.2f}%")

print("matice záměn:")
print(confusion_matrix(y_test, y_pred))