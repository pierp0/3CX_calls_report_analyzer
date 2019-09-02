import pandas as pd

df = pd.read_csv('./LogChiamateLastWeek_2905_3ZY0Z7AWhmBB4TynNbe6 (1).csv', delimiter = ',', header=5, engine='python', skipfooter=2, usecols=[
                 "Tempo della Chimata", "Caller ID", "Destinazione", "Stato", "Squillo", "Conversazione", "Totale", "Motivo"])
# print(df.head(10))

# print(df.sample(3))

# print(df[df['Tempo della Chimata'].notnull()])
# rint(df[df['Tempo della Chimata'].isnull()])

# print(df[df['Tempo della Chimata'].isnull()].count())

# Crare report settimanale con:
# Tot chiamate
# print('\nTOTALE CHIAMATE')
# print(df[df['Tempo della Chimata'].notnull()].count())
# Tot risposte  tot perse
# print('\nTOTALE PERSE')
# print(df.Stato == 'Non Risposta')

# print(df.groupby('Stato').count())
print(df)

print(df[df['Stato'] == 'Non Risposta'].count())
print(df[df['Stato'] == 'Risposta'].count())
# print(df.groupby('Stato').count())
# Chiamate risposte da ogni operatore
