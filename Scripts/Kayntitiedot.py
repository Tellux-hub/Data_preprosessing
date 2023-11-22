import pandas as pd

# kaynnit = {"TPKID": ["10", "15", "15","15","15", "12", "12"], "JNRO":["3", "1", "1", None, "1", "2", "2"], "TPKOODI": [None, "ZXD05", "NHJ10", "WX320", "TNX32", "MCA20", "ZXD05"], "TPLAJI": ["A", "P","O", "1", "V", "G", None]}
kaynnit = pd.read_csv("Z:\\input\\Aineisto\\kayntitiedot\\Kaynnit.csv", sep=";")
# drop unwanted datacolumn
kaynnit.drop(["SSIIRAIKA"], axis=1, inplace=True)
# print(df.head(10))

# save cropped dataframe for further experiments
# kaynnit.to_csv("Z:\\input\\Aineisto\\kayntitiedot\\Kaynnit_karsittu.csv", sep = ";", index = False)

# replace None as 0, others 1 between columns 2:46
# df2 = (df.isnull()).astype("int") #muuttaa kaikki sarakkeet
df2 = kaynnit.iloc[:, 1:47].isnull().astype("int")
# print(df2.head(10))
df3 = kaynnit["TPKID"]
# print(df3)
result = pd.merge(df3, df2, left_index=True, right_index=True)
# df3 = df[0:1].join(df2) # value error, columns overlap
print(result.head(10))

# write to .csv
result.to_csv("Z:\\input\\Aineisto\\kayntitiedot\\Kaynnit_poikkeamat.csv", index=False)
# result.to_csv("Z:\\input\\Aineisto\\kayntitiedot\\Kaynnit_poikkeamat_final_TEST.csv", index = False)
print("Valmis")
