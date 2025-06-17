import json
import pandas as pd
import matplotlib.pyplot as plt

with open('data.json', 'r') as file:
    data = json.load(file)

locations = []
latestEmissions = []
previousEmissions = []

for place in data["value"]:
    locations.append(place["location"])
    latestEmissions.append(place["latestMonthEmissions"])
    previousEmissions.append(place["previousMonthEmissions"])

dataFrame = pd.DataFrame({"Previous Month Emissions": previousEmissions, "Latest Month Emissions" :latestEmissions}, index=locations)

dataFrame.plot.bar()
plt.show()