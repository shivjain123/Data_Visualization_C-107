import pandas as p
import csv
import plotly.graph_objects as go

with open("D:/(4) WhiteHatJr. Codes/Third Module/Case Study (Math Pixel)/data.csv", newline = "") as f:
    reader = list(csv.reader(f))
    reader.pop(0)
    level_list = []
    attempt_list = []
    for i in range(0, len(reader)):
        if (reader[i][0] == "TRL_xsl"):
            level = reader[i][1]
            level_list.append(level)
            attempt = reader[i][2]
            attempt_list.append(attempt)

#print(level_list)

mode_data_range = {"Level 1": 0, "Level 2": 0, "Level 3" : 0, "Level 4" : 0}

df = p.DataFrame([attempt_list, level_list])

print(df)