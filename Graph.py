import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('five_cities.csv',skiprows=1,header=None)
df.columns = ['skill','Hyderabad_Ranking','Pune_Ranking','Delhi_Ranking','Bangalore_Ranking','Chennai_Ranking']
df['HighScore'] = df[['Hyderabad_Ranking','Pune_Ranking','Delhi_Ranking','Bangalore_Ranking','Chennai_Ranking']].max(axis=1)
t5 = df.sort_values('HighScore', ascending=False).head(10)
print("Overall Top 10 skills required for Data Scientist")
print(t5.skill)
df.plot(x="skill", y=["Hyderabad_Ranking", "Pune_Ranking","Delhi_Ranking","Bangalore_Ranking","Chennai_Ranking"],width=0.8, kind="bar")
plt.show()
