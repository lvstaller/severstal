from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных
dataset = pd.read_excel("Задание 2.xlsx")

# Удаления строк с пустыми значениями
dataset.dropna(inplace=True)

print(dataset)
# Сохранение в файл "out.xlsx" коэффициентов корреляции
dataset.corr().to_excel("out.xlsx")

# Разделение параметров X от Y
data_y = dataset[["Y"]]
data_x = dataset.drop(["Y"], axis=1)


# Объявление моделей
models = [
    LinearRegression(),  # метод наименьших квадратов
    RandomForestRegressor(n_estimators=100, max_features="sqrt"),  # случайный лес
    KNeighborsRegressor(),  # метод ближайших соседей
    SVR(kernel="linear"),  # метод опорных векторов с линейным ядром
    LogisticRegression(),  # логистическая регрессия
]

Xtrn, Xtest, Ytrn, Ytest = train_test_split(data_x, data_y, test_size=0.1)
# создаем временные структуры
TestModels = pd.DataFrame()
tmp = {}
# для каждой модели из списка
for model in models:
    # получаем имя модели
    m = str(model)
    tmp["Model"] = m[: m.index("(")]
    # для каждого столбцам результирующего набора
    # обучаем модель
    model.fit(Xtrn, Ytrn)
    # вычисляем коэффициент детерминации
    tmp["R2_Y"] = model.score(Xtest, Ytest)
    # записываем данные и итоговый DataFrame
    TestModels = TestModels.append([tmp])
# делаем индекс по названию модели
TestModels.set_index("Model", inplace=True)
fig, axes = plt.subplots(ncols=1, figsize=(15, 10))
TestModels.plot(ax=axes, kind="bar", title="R_Y")
plt.show()
