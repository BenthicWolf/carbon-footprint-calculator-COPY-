import json
import pandas as pd
import matplotlib.pyplot as plt

# Read resource data from json
with open('resource_data.json', 'r') as file:
    data = json.load(file)

resourceTypes = []
latestEmissions = []
previousEmissions = []

# Extract info from data
for place in data["value"]:
    resourceTypes.append(place["resourceType"].split("/")[-1])
    latestEmissions.append(place["latestMonthEmissions"])
    previousEmissions.append(place["previousMonthEmissions"])

# Create pandas dataframe to store info
dataFrame = pd.DataFrame({"Previous Month Emissions": previousEmissions, "Latest Month Emissions" :latestEmissions}, index=resourceTypes)

# Display dataframe as a bar chart
dataFrame.plot.bar()
plt.title("Emissions produced by resources")
plt.xlabel("Resource")
plt.ylabel("Emission")
plt.subplots_adjust(bottom=0.1)
plt.show()