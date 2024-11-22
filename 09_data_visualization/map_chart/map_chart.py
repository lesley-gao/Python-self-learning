"""
A national COVID-19 visualization map
"""

import json
from pyecharts.charts import Map
from pyecharts.options import *

# Read the data file
f = open("../../assets/covid-19.txt", "r", encoding="UTF-8")
data = f.read()  # Read all data

# Close the file
f.close()

# Retrieve data for each province
# Convert the JSON string to a Python dictionary
data_dict = json.loads(data)  # Base data dictionary

# Extract the data for provinces from the dictionary
province_data_list = data_dict["areaTree"][0]["children"]

# Assemble the name and confirmed cases for each province into a list
# Pack all the data for each province into the list
special_provinces = {
    "北京": "市", "天津": "市", "上海": "市", "重庆": "市",  # Municipalities directly under the central government
    "香港": "特别行政区", "澳门": "特别行政区",  # Special Administrative Regions
    "新疆": "维吾尔自治区", "西藏": "自治区", "内蒙古": "自治区",  # Autonomous Regions
    "广西": "壮族自治区", "宁夏": "回族自治区"  # Other autonomous regions
}  # Handle special province names

data_list = []  # List to store province data for plotting
for province_data in province_data_list:
    province_name = province_data["name"]  # Retrieve the province name
    province_confirm = province_data["total"]["confirm"]  # Retrieve the number of confirmed cases

    # Check if the province is in the special_provinces dictionary
    if province_name in special_provinces:
        # Append the special suffix (e.g., "市", "特别行政区", or "自治区") to the province name
        province_name = province_name + special_provinces[province_name]
    else:
        # For standard provinces, append "省" to the name
        province_name = province_name + "省"

    # Add the province name and confirmed cases as a tuple to the data list
    data_list.append((province_name, province_confirm))


# Create a map object
map = Map()

# Add data
map.add("Number of confirmed cases in each province", data_list, "china")

# Set global configurations, customize segmented visual mapping
map.set_global_opts(
    title_opts=TitleOpts(title="National COVID-19 Map"),
    visualmap_opts=VisualMapOpts(
        is_show=True,        # Whether to show the visual map
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
map.render("National COVID-19 Map.html")
