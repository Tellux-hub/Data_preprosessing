import pandas as pd

df = pd.DataFrame(
    {
        "Nimike": ["10", "15", "15", "15", "15", "12", "12"],
        "RRYHMA": ["32", "56", "89", "77", None, "890", "876"],
        "RESKDI": [
            None,
            "0973 3457",
            "3456 5789",
            None,
            "7689 4567",
            "5647 3456",
            "2341 4536",
        ],
        "Antal": [1, 2, 2, 1, 3, 1, 1],
        "RESHINTA": ["56€", "120€", "980€", "5€", "89€", "567€", None],
        "TPKID": ["10", "15", "20", "31", "17", "19", "25"],
        "operatorstid_start": [
            "11:10",
            "11:15",
            "12:15",
            "13:15",
            "14:15",
            "15:12",
            "12:00",
        ],
        "operatorstid_slut": [
            "19:10",
            "13:35",
            "12:45",
            "13:35",
            "14:55",
            "15:52",
            "13:00",
        ],
    }
)
# you can also use .csv file
# df = pd.read_csv("input\\Accessories_data.csv", encoding="latin1", sep=";")
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
    count_reskpl = temp_df["Antal"].sum()
    # print(f"Tuotekappaleita [{count_id}] id-muuttujassa [{id}]")
    df.loc[df["Nimike"] == id, "Y_RESKPL"] = count_reskpl

# print(df.head(10))

# drop unwanted columns
df_muokattu = df.drop(["TPKID", "operatorstid_start", "operatorstid_slut"], axis=1)
# print(df_muokattu)

result = df_muokattu.drop_duplicates()
print(result.head(10))

result.to_csv("output\\Accessories_data_sorted.csv", index=False)
print("Valmis")
