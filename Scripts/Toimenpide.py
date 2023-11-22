import pandas as pd

# toimenpide = {"TPKID": ["10", "15", "15","15","15", "12", "12"], "JNRO":["3", "1", "1", None, "1", "2", "2"], "TPKOODI": [None, "ZXD05", "NHJ10", "WX320", "TNX32", "MCA20", "ZXD05"], "TPLAJI": ["A", "P","O", "1", "V", "G", None]}
toimenpide = pd.read_csv("Z:\\input\\Aineisto\\toimenpiteet\\Toimenpiteet.csv", sep=";")
df = pd.DataFrame(data=toimenpide)
# print(df.head(10))

# Count toimenpidelkm of id:s, count None values of columns "JNRO", "TPKOODI", "TPLAJI"
# ,add columns "TLKM", "P_JNRO", "P_TPKOODI", "P_TPLAJI" to database
last_tmpkid = ""
tpkids = df["TPKID"].unique()

for id in tpkids:
    # print(id)
    temp_df = df.loc[df["TPKID"] == id]

    # count len unique "TPKID", add sum to column "TLKM"
    count_id = len(temp_df["TPKID"])
    # print(f"Toimenpiteita [{count_id}] id-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "TLKM"] = count_id

    # count None values in "JNRO", add sum to column "P_JNRO"
    count_njnro = temp_df["JNRO"].isnull().sum()
    # print(f"Poikkeamia [{count_njnro}] jnro-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_JNRO"] = count_njnro

    # count None values in "TPKOODI", add sum to column "P_TPKOODI"
    count_ntpkoodi = temp_df["TPKOODI"].isnull().sum()
    # print(f"Poikkeamia [{count_ntpkoodi}] tpkoodi-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_TPKOODI"] = count_ntpkoodi

    # count None values in "TPLAJI", add sum to column "P_TPLAJI"
    count_ntplaji = temp_df["TPLAJI"].isnull().sum()
    # print(f"Poikkeamia [{count_ntplaji}] tplaji-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_TPLAJI"] = count_ntplaji
# print(df.head(10))

df_muokattu = df.drop(["JNRO", "TPKOODI", "TPLAJI"], axis=1)
# print(df_muokattu)

result = df_muokattu.drop_duplicates()
print(result.head(10))

result.to_csv(
    "Z:\\input\\Aineisto\\toimenpiteet\\Toimenpiteet_poikkeamat.csv", index=False
)
print("Valmis")
