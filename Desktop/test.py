import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

import matplotlib.pyplot as plt

# Charger les données de ventes (exemple fictif)
data = pd.read_csv('store_sales.csv', parse_dates=['Date'], index_col='Date')
data.head()



# Visualiser les tendances des ventes au fil du temps
plt.figure(figsize=(10, 6))
plt.plot(data['Sales'])
plt.title('Ventes au fil du temps')
plt.xlabel('Date')
plt.ylabel('Ventes')
plt.show()

# Décomposer les séries chronologiques


result = seasonal_decompose(data['Sales'], model='additive', period=12)
result.plot()
plt.show()


# Diviser les données en ensemble d'entraînement et de test
train = data['Sales'][:int(0.8*len(data))]
test = data['Sales'][int(0.8*len(data)):]

# Ajuster le modèle ARIMA
model = ARIMA(train, order=(5, 1, 0))
model_fit = model.fit()

# Faire des prévisions
forecast = model_fit.forecast(steps=len(test))

# Visualiser les prévisions par rapport aux données réelles
plt.figure(figsize=(10, 6))
plt.plot(train, label='Entraînement')
plt.plot(test, label='Test')
plt.plot(test.index, forecast, label='Prévisions', color='red')
plt.title('Prévision des ventes avec ARIMA')
plt.xlabel('Date')
plt.ylabel('Ventes')
plt.legend()
plt.show()


# Calculer les erreurs
mae = mean_absolute_error(test, forecast)
rmse = mean_squared_error(test, forecast, squared=False)

print(f'MAE: {mae}')
print(f'RMSE: {rmse}')




# Prédire les ventes pour les prochains mois
future_forecast = model_fit.forecast(steps=12)

# Visualiser les prévisions futures
plt.figure(figsize=(10, 6))
plt.plot(data['Sales'], label='Historique')
plt.plot(pd.date_range(start=data.index[-1], periods=12, freq='M'), future_forecast, label='Prévisions futures', color='red')
plt.title('Prévisions futures des ventes')
plt.xlabel('Date')
plt.ylabel('Ventes')
plt.legend()
plt.show()


# Analyse exploratoire des données (EDA)




# Visualiser les tendances des ventes au fil du temps
plt.figure(figsize=(10, 6))
plt.plot(data['Sales'])
plt.title('Ventes au fil du temps')
plt.xlabel('Date')
plt.ylabel('Ventes')
plt.show()

