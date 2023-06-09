# -*- coding: utf-8 -*-
"""Traiding_google.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11GZnAUU5_GVv1a9ruMM0D_DJ_v5SJKrq
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos=pd.read_csv('GOOG.csv')
datos.head()

datos.shape

plt.figure(figsize=(10,5))
plt.plot(datos['Close'])
plt.xlabel('Años')
plt.ylabel('Precio de cierre')
plt.title("Acciones de Google - Cierre de los años desde el 2014 al 2022")
plt.show

"""**Medias moviles **"""

MVS30 = pd.DataFrame()
MVS30['Close'] = datos['Close'].rolling(window = 30).mean()
MVS30[MVS30.index == 29]

MVS100 = pd.DataFrame()
MVS100['Close'] = datos['Close'].rolling(window = 100).mean()
MVS100[MVS100.index == 99]

plt.figure(figsize=(10,5))
plt.plot(datos['Close'], label='real', color='blue') 
plt.plot(MVS30['Close'], label='MVS30', color='red') 
plt.plot(MVS100['Close'], label='MVS100', color='green') 
plt.xlabel('Años')
plt.ylabel('Precio de cierre')
plt.title("Acciones de Google - Cierre de los años desde el 2014 al 2022")
plt.legend(loc='upper left')
plt.show

data =pd.DataFrame()
data['Presio de Google']=datos['Close']
data['MVS30']=MVS30['Close']
data['MVS100']=MVS100['Close']
data

def señalCV(dataV):
    compra = []
    venta = []
    condicion = 0

    for dia in range(len(data)):
         if data['MVS30'][dia]> data['MVS100'][dia]:
            if condicion != 1:
               compra.append(data['Presio de Google'][dia])
               venta.append(np.nan)
               condicion=1
            else:
               compra.append(np.nan)
               venta.append(np.nan)
         elif data['MVS30'][dia] < data['MVS100'][dia]:
                  if condicion != -1:
                    venta.append(data['Presio de Google'][dia])
                    compra.append(np.nan)
                    condicion=-1
                  else:
                    compra.append(np.nan)
                    venta.append(np.nan)
         else:
                  compra.append(np.nan)
                  venta.append(np.nan)
    return(compra, venta)

señales=señalCV(data)
data['Compra']=señales[0]
data['Venta']=señales[1]
data

plt.figure(figsize=(10,5))
plt.plot(datos['Close'], label='real', color='gray', alpha=0.6) 
plt.plot(MVS30['Close'], label='MVS30', color='orange', alpha=0.6) 
plt.plot(MVS100['Close'], label='MVS100', color='purple', alpha=0.6) 
plt.scatter(data.index, data['Compra'], label='Precio de Compra', marker='^', color='green')
plt.scatter(data.index, data['Venta'], label='Precio de venta', marker='v', color='red')
plt.xlabel('Años')
plt.ylabel('Precio de cierre')
plt.title("Acciones de Google - Cierre de los años desde el 2014 al 2022")
plt.legend(loc='upper left')
plt.show