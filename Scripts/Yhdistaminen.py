import pandas as pd

# Read files
kaynnit = pd.read_csv(
    "Z:\\input\\Aineisto\\kayntitiedot\\Kaynnit_poikkeamat.csv", sep=","
)
# print(kaynnit.columns)
kaynnit.set_index("TPKID", inplace=True)

toimenpide = pd.read_csv(
    "Z:\\input\\Aineisto\\toimenpiteet\\Toimenpiteet_poikkeamat.csv", sep=","
)
toimenpide.set_index("TPKID", inplace=True)

henkilosto = pd.read_csv(
    "Z:\\input\\Aineisto\\henkilosto\\Pseudohenkilosto_poikkeamat_2.csv", sep=";"
)
henkilosto.set_index("TPKID", inplace=True)

resurssit = pd.read_csv(
    "Z:\\input\\Aineisto\\resurssit\\Resurssit_poikkeamat.csv",
    sep=",",
    encoding="latin1",
)
resurssit.set_index("TPKID", inplace=True)
# print(df)


# find duplicates
doubles = resurssit[resurssit.index.duplicated(keep=False)]
print(doubles)


# join dataframes
df = (
    kaynnit.join(toimenpide, how="outer")
    .join(henkilosto, how="outer")
    .join(resurssit, how="outer")
)
print(df.head(10))


# fill NaN as 1 to indicate data omission
result = df.fillna(1)


# write to .csv
result.to_csv(
    "Z:\\input\\Aineisto\\kayntitiedot\\Kayntitiedot_poikkeamat_yhd_FINAL_eiNaN.csv",
    sep=";",
    index=True,
)
