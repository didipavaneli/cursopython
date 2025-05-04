import sklearn as sk
import pandas as pd

data = {
    "diametro": [15,20,25,30,35,40],
    "preco": [50,60,70,80,90,100]
}

df = pd.DataFrame(data)

modelo = sk.linear_model.LinearRegression()
modelo.fit(df[["diametro"]], df[["preco"]])



while True:
    diametro = int(input("Digite o Diametro da pizza: "))
    preco = round(modelo.predict([[diametro]])[0][0])
    print(f"Uma pizza de {diametro}cm de diametro custa: R${preco},00")