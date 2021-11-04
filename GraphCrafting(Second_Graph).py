import plotly.graph_objects as go
import plotly.offline as pyo
import json
import re

with open("data\config.json") as g:
    config = json.load(g)
    SecondGraphPathHTML = config["SecondGraphPathHTML"]
    SecondGraphPathPNG = config["SecondGraphPathPNG"]
    categories = config["SecondCategories"]

g.close()

categories = [*categories, categories[0]]

with open("data\data2.json", "r") as f:
    content = json.load(f)
    MaxRow = content["MaxRow"]
    print(MaxRow)
    MaxColumn = content["MaxColumn"]

for i in range(3, MaxRow+2):
    j = str(i)
    Class = content["Class" + j]
    ClassNo = content["ClassNo" + j]
    data = content["data" + j]
    date = content["date" + j]
    year = content["year" + j]
    date = re.sub(r'[\\/*?:"<>|]', "_", date)
    year = re.sub(r'[\\/*?:"<>|]', "_", year)

    print(i)
    print(data)

    fig = go.Figure(
        data=[
            go.Scatterpolar(r=data, theta=categories, fill='toself', name='Marks'),
        ],
        layout=go.Layout(
            title=go.layout.Title(text=Class + ClassNo + " " + 'Different Types of Questions Report: ' + year),
            polar={'radialaxis': {'visible': True, 'range': [0, 100]}},
            showlegend=True,
        )
    )

    pyo.plot(fig, filename=SecondGraphPathHTML + Class + ClassNo + "&&" + year + date + ".html", auto_open=False)
    fig.write_image(SecondGraphPathPNG + Class + ClassNo + " " + year + "&&" + date + ".png", format="png")

    print("Finished " + Class + ClassNo + "Report: " + year)
