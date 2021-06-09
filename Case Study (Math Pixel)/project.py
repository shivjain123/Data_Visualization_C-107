import pandas as p
import plotly_express as px

df = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/Case Study (Math Pixel)/data.csv")

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

figure = px.scatter(mean, x = "student_id", y = "level", size = "attempt", color = "attempt")

figure.show()