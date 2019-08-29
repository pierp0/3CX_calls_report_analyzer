import pandas as pd

df = pd.read_csv('./LogChiamateLastWeek_2905_3ZY0Z7AWhmBB4TynNbe6 (1).csv', header = 5, skipfooter = 2, usecols = ["Tempo della Chimata", "Caller ID", "Destinazione", "Stato", "Squillo", "Conversazione", "Totale", "Motivo"])
#print(df.head(10))

#print(df.sample(3))

print(df[df['Tempo della Chimata'].notnull()])
print(df[df['Tempo della Chimata'].isnull()])


print(df[df['Tempo della Chimata'].notnull()].count())
#print(df[df['Tempo della Chimata'].isnull()].count())