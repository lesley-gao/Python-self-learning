# Read the data file
import json

from pyecharts.charts import Map
from pyecharts.options import *

f = open("../../assets/covid-19.txt", "r", encoding="UTF-8")
data = f.read()  # Read all data

# Close the file
f.close()

# Retrieve data for Henan province
# Convert the JSON string to a Python dictionary
data_dict = json.loads(data)  # Base data dictionary

# Extract data for cities in Henan province from the dictionary
cities_data = data_dict["areaTree"][0]["children"][3]["children"]

# Prepare tuples of data and add them to a list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"  # Add "市" to the city names, to make sure they align with the city names in the dataset
    city_confirm = city_data["total"]["confirm"]  # Number of confirmed cases
    data_list.append((city_name, city_confirm))
print(data_list)

# Manually add data for Jiyuan City
# (Jiyuan City is not included in the original data, so the confirmed cases are searched online and added manually)
data_list.append(("济源市", 5))

# Create a map object
map = Map()

# Add data
map.add("Number of confirmed cases in Henan Province", data_list, "河南")

# Set global configurations, customize segmented visual mapping
map.set_global_opts(
    title_opts=TitleOpts(title="COVID-19 Map of Henan Province",pos_top = "10%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,        # Whether to display
        is_piecewise=True,   # Whether to use segmented visualization
        pieces=[
            {"min": 1, "max": 99, "label": "1~99 cases", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100~999 cases", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000~4999 cases", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000~9999 cases", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000~99999 cases", "color": "#CC3333"},
            {"min": 100000, "label": "100000+ cases", "color": "#990033"},
        ]
    )
)

# Render the map
map.render("COVID-19_Map_Henan_Province.html")
