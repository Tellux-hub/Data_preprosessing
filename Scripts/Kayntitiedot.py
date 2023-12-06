import pandas as pd

df = pd.DataFrame(
    {
        "TPKID": ["10", "15", "15", "15", "15", "12", "12"],
        "JNRO": ["3", "1", "1", None, "1", "2", "2"],
        "TPKOODI": [None, "ZXD05", "NHJ10", "WX320", "TNX32", "MCA20", "ZXD05"],
        "TPLAJI": ["A", "P", "O", "1", "V", "G", None],
        "SSIIRAIKA": ["20", "43", "33", "78", "56", "45", "33"],
    }
)
# you can also use .csv file
# df = pd.read_csv("input\\surg_appointment_data.csv", sep=",")
print(df.head(10))

# drop unwanted datacolumn
df.drop(["SSIIRAIKA"], axis=1, inplace=True)
# print(df.head(10))

# save cropped dataframe for further experiments
# kaynnit.to_csv("C:\\Select_Directory\\surg_appointment_data_reduced.csv", sep = ";", index = False)

# replace None as 0, others 1 between columns 2:46
# df2 = (df.isnull()).astype("int") #muuttaa kaikki sarakkeet
df2 = df.iloc[:, 1:47].isnull().astype("int")
# print(df2.head(10))
df3 = df["TPKID"]
# print(df3)
result = pd.merge(df3, df2, left_index=True, right_index=True)
# df3 = df[0:1].join(df2) # value error, columns overlap
print(result.head(10))

# write to .csv
result.to_csv("output\\Surg_appointment_data_omissions.csv", index=False)
print("Valmis")
