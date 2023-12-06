import pandas as pd

henkilosto = pd.DataFrame(
    {
        "TMPKID": ["10", "10", "15", "15", "12", "12", "12"],
        "HNIMI": [
            "Matti Majanen",
            "Elina Elonen",
            "Into Iloinen",
            "Matti Majanen",
            "Elina Elonen",
            "Iina Innokas",
            "Matti Majanen",
        ],
        "HRYHMA": ["5", "4", None, "5", "4", "6", "5"],
        "PAVUST": ["P", "A", "O", "A", "P", "G", None],
    }
)

# you can also use .csv file
# henkilosto = pd.read_csv("input\\Personnel_data.csv", sep=";", encoding="latin1", dtype="str")
print(henkilosto)

# factorize by "HNIMI", replace "HNIMI" by sequential number
henkilosto["pseudonro"] = pd.factorize(henkilosto["HNIMI"])[0] + 1
label = "Nimi"
henkilosto["pseudonimijanro"] = label + henkilosto["pseudonro"].astype(str)
henkilosto["HNIMI"] = henkilosto["pseudonimijanro"]
muuttujat = henkilosto.drop(["pseudonro", "pseudonimijanro"], axis=1)
# print(muuttujat.head(10))

muuttujat.to_csv(
    "output\\Pseudo_personnel_data.csv.csv",
    sep=";",
    encoding="utf-8",
    index=False,
)
print("Valmis")
