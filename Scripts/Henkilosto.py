import pandas as pd

df = pd.DataFrame(
    {
        "TPKID": ["15", "15", "15", "15", "15", "12", "12"],
        "HNIMI": ["Nimi1", "Nimi2", "Nimi3", None, "Nimi5", "Nimi1", "Nimi3"],
        "HRYHMA": ["5", None, "4", "5", "6", None, None],
        "PAVUST": ["P", "A", "P", "A", None, "P", "P"],
    }
)
# you can also use .csv file
# df = pd.read_csv("input\\Pseudo_personnel_data.csv", sep=",")
print(df.head(10))

# Count henkilostolkm of id:s, count None values of columns "HNIMI", "HRYHMA", "PAVUST"
# ,add columns "HLKM", "P_NIMI", "P_RYHM", "P_AVUST" to database

last_tmpkid = ""
tpkids = df["TPKID"].unique()

for id in tpkids:
    # print(id)
    temp_df = df.loc[df["TPKID"] == id]

    # count len unique "TPKID", add sum to column "HLKM"
    count_id = len(temp_df["TPKID"])
    # print(f"Henkilostoa [{count_id}] id-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "HLKM"] = count_id

    # count None values in "HNIMI", add sum to column "P_NIMI"
    count_nnimi = temp_df["HNIMI"].isnull().sum()
    # print(f"Poikkeamia [{count_nnimi}] nimi-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_NIMI"] = count_nnimi
    # count None values in "HRYHMA", add sum to column "P_RYHM"
    count_nryhm = temp_df["HRYHMA"].isnull().sum()
    # print(f"Poikkeamia [{count_nryhm}] ryhmä-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_RYHM"] = count_nryhm
    # count None values in "PAVUST", add sum to column "P_AVUST"
    count_navust = temp_df["PAVUST"].isnull().sum()
    # print(f"Poikkeamia [{count_navust}] pavust-muuttujassa [{id}]")
    df.loc[df["TPKID"] == id, "P_AVUST"] = count_navust
print(df.head(10))

df_muokattu = df.drop(["HNIMI", "HRYHMA", "PAVUST"], axis=1)
# print(df_muokattu.head(10))

result = df_muokattu.drop_duplicates()
print(result.head(10))

result.to_csv(
    "output\\Personnel_data_omissions.csv",
    sep=";",
    index=False,
)
