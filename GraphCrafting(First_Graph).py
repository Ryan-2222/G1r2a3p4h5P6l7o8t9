import plotly.graph_objects as go
import plotly.offline as pyo
import json
import re

with open("data\config.json") as g:
    config = json.load(g)
    FirstGraphPathHTML = config["FirstGraphPathHTML"]
    FirstGraphPathPNG = config["FirstGraphPathPNG"]
    categories = config["FirstCategories"]

g.close()

categories = [*categories, categories[0]]

with open("data\data.json", "r") as f:
    content = json.load(f)
    MaxRow = content["MaxRow"]
    print(MaxRow)
    MaxColumn = content["MaxColumn"]

for i in range(3, MaxRow+2):
    j = str(i)
    Class = content["Class" + j]
    ClassNo = content["ClassNo" + j]
    data = content["data" + j]
    date = content["year" + j]
    date = re.sub(r'[\\/*?:"<>|]', "_", date)

    print(i)
    print(data)

    fig = go.Figure(
        data=[
            go.Scatterpolar(r=data, theta=categories, fill='toself', name='Marks'),
        ],
        layout=go.Layout(
            title=go.layout.Title(text=Class + ClassNo + " " + 'Form1-6 Math result'),
            polar={'radialaxis': {'visible': True, 'range': [0, 100]}},
            showlegend=True,
        )
    )

    pyo.plot(fig, filename=FirstGraphPathHTML + Class + ClassNo + " " + date + ".html", auto_open=False)
    fig.write_image(FirstGraphPathPNG + Class + ClassNo + " " + date + ".png", format="png")

    print("Finished " + Class + ClassNo)
