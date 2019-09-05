import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

Bangalore = pd.read_csv('Bangalore.csv',skiprows=1,header=None)
Bangalore.columns = ['skill','Count','Bangalore_Ranking']
t5 = Bangalore.sort_values('Bangalore_Ranking', ascending=False).head(5)
t5.columns = ['skill','Count','Bangalore_Ranking']
t5.drop(t5.columns[[1]], axis=1, inplace=True)
print('Top 5 Skills required for Data Scientist in Bangalore') 
print(t5.skill)
Chennai = pd.read_csv('Chennai.csv',skiprows=1,header=None)
Chennai.columns = ['skill','Count','Chennai_Ranking']
t5c = Chennai.sort_values('Chennai_Ranking', ascending=False).head(5)
t5c.columns = ['skill','Count','Chennai_Ranking']
t5c.drop(t5c.columns[[1]], axis=1, inplace=True)
print('Top 5 Skills required for Data Scientist in Chennai') 
print(t5c.skill)
result1 = pd.merge(Bangalore, Chennai, how='left', on=['skill'])
result1.drop(result1.columns[[1,3]], axis=1, inplace=True)
Delhi = pd.read_csv('Delhi.csv',skiprows=1,header=None)
Delhi.columns = ['skill','Count','Delhi_Ranking']
t5d = Delhi.sort_values('Delhi_Ranking', ascending=False).head(5)
t5d.columns = ['skill','Count','Delhi_Ranking']
t5d.drop(t5d.columns[[1]], axis=1, inplace=True)
print('Top 5 Skills required for Data Scientist in Delhi') 
print(t5d.skill)
Pune = pd.read_csv('Pune.csv',skiprows=1,header=None)
Pune.columns = ['skill','Count','Pune_Ranking']
t5p = Pune.sort_values('Pune_Ranking', ascending=False).head(5)
t5p.columns = ['skill','Count','Pune_Ranking']
t5p.drop(t5p.columns[[1]], axis=1, inplace=True)
print('Top 5 Skills required for Data Scientist in Pune') 
print(t5p.skill)
result2 = pd.merge(Pune, Delhi, how='left', on=['skill'])
result2.drop(result2.columns[[1,3]], axis=1, inplace=True)
result3 = pd.merge(result2, result1, how='left', on=['skill'])
Hyderabad = pd.read_csv('Hyderabad.csv',skiprows=1,header=None)
Hyderabad.columns = ['skill','Count','Hyderabad_Ranking']
t5h = Hyderabad.sort_values('Hyderabad_Ranking', ascending=False).head(5)
t5h.columns = ['skill','Count','Hyderabad_Ranking']
t5h.drop(t5h.columns[[1]], axis=1, inplace=True)
print('Top 5 Skills required for Data Scientist in Hyderabad') 
print(t5h.skill)
result = pd.merge(Hyderabad, result3, how='left', on=['skill'])
result.drop(result.columns[[1]], axis=1, inplace=True)
#print(result)
#result.to_csv('five_cities.csv',index=False)
frames = [Bangalore.skill, Hyderabad.skill, Pune.skill, Delhi.skill, Chennai.skill]
trycloud = pd.concat(frames)
a = trycloud.tolist()
#print(a)
counts = Counter(a)
print(counts)
wordcloud = WordCloud()
wordcloud.generate(' '.join(a))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

