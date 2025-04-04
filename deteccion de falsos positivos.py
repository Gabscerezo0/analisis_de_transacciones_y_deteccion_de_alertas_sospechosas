import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

f = pd.read_csv("transaction_data.csv")
print(f.head())
print(f.info())
print(f.describe())

# Análisis de alertas 
print(f['flagged_alert'].value_counts(normalize=True))

# visualizando con un bar chart
f['flagged_alert'].value_counts().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Flagged Alert')
plt.ylabel('Cantidad de Transacciones')
plt.title('Detección de falsos positivos')
plt.show()
#confirmamos que hay mas transacciones marcadas como NO sospechosas

#Para la deteccion de falsos positivos hagamos lo siguiente:
#comparemos el monto de transacciones sospechosas vs. no sospechosas
plt.figure(figsize=(10,6))
sns.boxplot(x=f['flagged_alert'],y=f['amount'],color='salmon')
plt.xlabel('Flagged Alert')
plt.ylabel('Monto de la Transacción')
plt.title('Distribución de Montos en Transacciones Marcadas y No Marcadas')
plt.show()

# Cuántas transacciones de bajo monto fueron marcadas como sospechosas?
transacciones_bajo_monto = f[(f['amount'] < f['amount'].median()) & (f['flagged_alert'] == 1)]
print(f"Cantidad de transacciones sospechosas con monto bajo: {len(transacciones_bajo_monto)}")

# El sistema solo detecta montos altos?
print(f.groupby('flagged_alert')['amount'].describe())

# El monto tiene un impacto en las alertas?
sns.kdeplot(f[f['flagged_alert'] == 0]['amount'], label="No sospechosa", fill=True)
sns.kdeplot(f[f['flagged_alert'] == 1]['amount'], label="Sospechosa", fill=True)
plt.xlabel("Monto de la Transacción")
plt.ylabel("Densidad")
plt.title("Distribución de Montos en Transacciones Marcadas y No Marcadas")
plt.legend()
plt.show()

# Contamos alertas por tipo de transacción
print(f.groupby("transaction_type")["flagged_alert"].mean() * 100)
print(f.groupby("transaction_type")["amount"].mean())
