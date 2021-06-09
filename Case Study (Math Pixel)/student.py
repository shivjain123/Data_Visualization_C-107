import pandas as p
import csv
import plotly.graph_objects as go

df = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/Case Study (Math Pixel)/data.csv")

student_list = df.loc[df["student_id"] == "TRL_xsl"]

mean = student_list.groupby("level")["attempt"].mean()

print(mean)

figure = go.Figure(
    go.Bar(x=mean, y=['level 1', 'level 2', 'level 3', 'level 4'], orientation='h'))

figure.show()
