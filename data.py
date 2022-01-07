import pandas as pd
import plotly_express as px

cd = pd.read_csv("covidData.csv")
dp = px.scatter(cd, x="date" , y="cases", color="country")
dp.show()