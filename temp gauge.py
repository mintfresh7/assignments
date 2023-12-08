# Author : Abigail Leppo
# Class : ITN160
# Class Section : 201
# Date : 12/05/2023
# Assignment : Project 3: Temp Gauge

from guizero import App, Slider, Text, Waffle

from guizero import App, Slider, Waffle, Text

def update_temperature(value):
    if value == 0:
        message.value = "Engine Off"
        waffle.bg = "black"
    elif 1 <= value <= 194:
        message.value = "Engine Warming/Cooling"
        waffle.bg = "blue"
    elif 195 <= value <= 220:
        message.value = "Engine Temp Normal"
        waffle.bg = "green"
    else:
        message.value = "Engine Overheated"
        waffle.bg = "red"

app = App("Engine Temperature Gauge")

slider = Slider(app, start=0, end=300, command=update_temperature,)
waffle = Waffle(app, width=50, height=50)
message = Text(app, "Engine Off", align="bottom")

app.display()