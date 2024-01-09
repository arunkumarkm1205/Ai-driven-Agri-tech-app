import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Rain_Forecast.csv")
data = data.set_index(data.Date)
data.drop(columns = ["Date"], inplace = True)

train = data.iloc[200:]

from statsmodels.tsa.statespace.sarimax import SARIMAX

forecast_model=SARIMAX(train,order=(1,1,1),seasonal_order=(1,1,1,12)) 
forecast_model=forecast_model.fit()
