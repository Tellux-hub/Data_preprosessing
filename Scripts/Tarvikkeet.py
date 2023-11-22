import pandas as pd

# df = {"Nimike": ["10", "15", "15","15","15", "12", "12"], "RRYHMA":["32", "56", "89", "77", None, "890", "876"], "RESKDI": [ None, "0973 3457", "3456 5789", None,"7689 4567", "5647 3456", "2341 4536"], "Antal": [1, 2, 2, 1 , 3 , 1 , 1], "RESHINTA": ["56€", "120€", "980€", "5€", "89€", "567€", None]}
df = pd.read_csv(
    "Z:\\input\\Aineisto\\resurssit\\hoitotarvikkeet\\kulutus.csv",
    encoding="latin1",
    sep=";",
)
# print(df.head(10))

# Count resurssilkm of id:s by "Nimike" and count of particles "Y_RESKPL",
# add columns "RLKM", "Y_RESKPL" to database, drop colums, "TPKID", "operatorstid_start", "operatorstid_slut"

last_id = ""
tpkids = df["Nimike"].unique()

for id in tpkids:
    # print(id)
    temp_df = df.loc[df["Nimike"] == id]

    # count len unique "Nimike", add sum to column "RLKM"
    count_id = len(temp_df["Nimike"])
    # print(f"Resursseja [{count_id}] id-muuttujassa [{id}]")
    df.loc[df["Nimike"] == id, "RLKM"] = count_id

    # count Antal values by "Nimike"
    count_reskpl = temp_df["antal"].sum()
    # print(f"Tuotekappaleita [{count_id}] id-muuttujassa [{id}]")
    df.loc[df["Nimike"] == id, "Y_RESKPL"] = count_reskpl

# print(df.head(10))

df_muokattu = df.drop(["TPKID", "operatorstid_start", "operatorstid_slut"], axis=1)
# print(df_muokattu)

result = df_muokattu.drop_duplicates()
print(result.head(10))

result.to_csv(
    "Z:\\input\\Aineisto\\resurssit\\hoitotarvikkeet\\kulutus_sort.csv", index=False
)
print("Valmis")
