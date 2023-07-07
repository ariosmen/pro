from search.search import download
from order.order import order
import pandas as pd

download()

df = pd.read_csv("./download/padron.csv", low_memory=False)
a = df[
    (df["SEXE"] == "Home")
    & (df["EDAT"] > 50)
    & (df["NAIX_MUNICIPI"] == "BARCELONA")
    & (df["DISTRICTE"] == 5)
]

b = df[
    (df["SEXE"] == "Dona")
    & (df["EDAT"] < 70)
    & (df["NAIX_MUNICIPI"] == "AZUAGA")
]

order(a)
order(b)