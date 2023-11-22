import pandas as pd

henkilosto = pd.read_csv(
    "Z:\\input\\Aineisto\\df.csv", sep=";", encoding="latin1", dtype="str"
)
# print(henkilosto.head(10))

# factorize by "HNIMI", replace "HNIMI" by sequential number
henkilosto["pseudonro"] = pd.factorize(henkilosto["HNIMI"])[0] + 1
label = "Nimi"
henkilosto["pseudonimijanro"] = label + henkilosto["pseudonro"].astype(str)
henkilosto["HNIMI"] = henkilosto["pseudonimijanro"]
muuttujat = henkilosto.drop(["pseudonro", "pseudonimijanro"], axis=1)
# print(muuttujat.head(10))

muuttujat.to_csv(
    "Z:\\input\\Aineisto\\henkilosto\\pseudohenkilosto_2.csv",
    sep=";",
    encoding="utf-8",
    index=False,
)
print("Valmis")
