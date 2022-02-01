import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px

df = pd.read_csv("bright_stars.csv")

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
names = df["Star_name"].to_list()


fig = px.bar(x=names, y=mass)
fig.show()

fig2 = px.bar(x=names, y=radius)
fig2.show()

fig3 = px.bar(x=names, y=dist)
fig3.show()





