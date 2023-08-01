import pandas as pd

period_1 = "2023.01.01 - 2023.03.01"
period_2 = "2023.04.01 - 2023.06.01"
input_file = "Задача 4.xlsx"


df = pd.read_excel(input_file)
df["Критичная позиция"] = ""
products = df["Продукт"].unique()
data_out = pd.DataFrame()
for product in products:
    data = df.loc[df["Продукт"] == product]
    if data.shape[0] == 1:
        i = data.index
        if data["ВГ"].values < 90:
            df["Критичная позиция"][i] = 1
        else:
            df["Критичная позиция"][i] = 0
    else:
        i1, i2 = data.index
        if (
            data["Период"][i1] == period_1
            and data["Период"][i2] == period_2
            and data["ВГ"][i1] - data["ВГ"][i2] > 5
            and data["ВГ"][i2] < 90
        ):
            df["Критичная позиция"][i1] = 1
            df["Критичная позиция"][i2] = 1
        else:
            df["Критичная позиция"][i1] = 0
            df["Критичная позиция"][i2] = 0

df.to_excel("out.xlsx")
