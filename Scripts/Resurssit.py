import pandas as pd

# resurssit = {"TPKID": ["10", "15", "15","15","15", "12", "12"], "RRYHMA":["32", "56", "89", "77", None, "890", "876"], "RESKDI": [ None, "0973 3457", "3456 5789", None,"7689 4567", "5647 3456", "2341 4536"], "RESKPL": [1, 2, 2, 1 , 3 , 1 , 1], "RESHINTA": ["56€", "120€", "980€", "5€", "89€", "567€", None]}
df = pd.read_csv(
    "Z:\\input\\Aineisto\\resurssit\\Resurssit.csv", sep=";", encoding="latin1"
)
df.replace({"NULL": None}, regex=True, inplace=True)
# print(df.head(10))

# Count resurssilkm of id:s and count of particles "Y_RESKPL", count None values of columns "RRYHMA", "RESKDI", "RESHINTA"
# ,add columns "RLKM", "P_RYHMA", "P_RESKDI", "P_RESHINTA" to database

last_tpkid = ""
tpkids = df["TPKID"].unique()

for id in tpkids:
    # print(id)
    temp_df = df.loc[df["TPKID"] == id]

    # count len unique "TPKID", add sum to column "RLKM"
    count_id = len(temp_df["TPKID"])
    # print(f"Resursseja [{count_id}] id-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "RLKM"] = count_id

    # count RESKPL values by "TPKID"
    count_reskpl = temp_df["RESKPL"].sum()
    # print(f"Tuotekappaleita [{count_id}] id-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "Y_RESKPL"] = count_reskpl

    # count None values in "RRYHMA", add sum to column "P_RRYHMA"
    count_nryhma = temp_df["RRYHMA"].isnull().sum()
    # print(f"Poikkeamia [{count_nryhma}] rryhma-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_RYHMA"] = count_nryhma

    # count None values in "RESKDI", add sum to column "P_RESKDI"
    count_nreskdi = temp_df["RESKDI"].isnull().sum()
    # print(f"Poikkeamia [{count_nreskdi}] reskdi-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_RESKDI"] = count_nreskdi

    # count None values in "RESKPL", add sum to column "P_RESKPL"
    count_nreskpl = temp_df["RESKPL"].isnull().sum()
    # print(f"Poikkeamia [{count_nreskdi}] reskdi-muuttujassa [{id}]")    # sum(result["P_RESKPL"]), sum(result["P_RYHMA"]
    df.loc[df["TPKID"] == id, "P_RESKPL"] = count_nreskpl

    # count None values in "RESHINTA", add sum to column "P_RESHINTA"
    count_nreshinta = temp_df["RESHINTA"].isnull().sum()
    # print(f"Poikkeamia [{count_nreshinta}] reshinta-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_RESHINTA"] = count_nreshinta

# print(df.head(10))

df_muokattu = df.drop(["RESKPL", "RRYHMA", "RESKDI", "RESHINTA"], axis=1)
# print(df_muokattu)

result = df_muokattu.drop_duplicates()
# print(result.head(10))

result.to_csv("Z:\\input\\Aineisto\\resurssit\\Resurssit_poikkeamat.csv", index=False)
print("Valmis")
