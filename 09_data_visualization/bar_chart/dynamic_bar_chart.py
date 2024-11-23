"""
A dynamic bar chart for GDP visualization
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# Step 1: Read the data from a CSV file
file = open("../../assets/1960-2019 Global GDP.csv", "r", encoding="GB2312")   # Open the file with the specified encoding
data_lines = file.readlines()  # Read all lines into a list

# Close the file after reading to free resources
file.close()

# Remove the first line of the file (header row)
data_lines.pop(0)

# Step 2: Convert data into a dictionary for structured storage
# Format: [Year: [[Country, GDP], [Country, GDP], ...]]
# 1960: [[美国,123], [中国,321], ...... ], 1961: [[美国,123], [中国,321], ...... ]

# define a dict first
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # Extract the year from the first column
    country = line.split(",")[1]  # Extract the country name from the second column
    gdp = float(line.split(",")[2])  # Extract the GDP value from the third column (convert to float)

    # Use a try-except block to handle KeyError when adding data to the dictionary
    try:
        data_dict[year].append([country, gdp])  # If this year exist, append country and gdp to the list
    except KeyError:
        data_dict[year] = []  # If this year doesn't exist, initialize a new list for the year
        data_dict[year].append([country, gdp])  # Add the current [Country, GDP] pair

# print(data_dict[1960])

# Step 3: Initialize a Timeline object with a light theme
timeline = Timeline({"theme": ThemeType.LIGHT})

# Step 4: Process the data year by year and create bar charts
# Sort the years in ascending order
sorted_year_list = sorted(data_dict.keys())  #Displaying the keys in sorted order using sorted() on keys

for year in sorted_year_list:
    # Sort the data for the current year by GDP in descending order
    data_dict[year].sort(key=lambda element: element[1], reverse=True)

    # Extract the top 8 countries by GDP for the current year
    year_data = data_dict[year][0:8]
    x_data = []  # x-axis data: list of countries
    y_data = []  # y-axis data: list of GDP values
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # Add the country name to x-axis data
        y_data.append(country_gdp[1] / 100000000)  # Convert GDP to billions and add to y-axis data

    # Step 5: Create a bar chart for the current year
    bar = Bar()  # Initialize a Bar object
    x_data.reverse()  # Reverse x-axis data to match the display order
    y_data.reverse()  # Reverse y-axis data to match the display order
    bar.add_xaxis(x_data)  # Add the reversed country data to the x-axis
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))  # Add GDP data to the y-axis

    # Reverse the x and y axes to create a horizontal bar chart
    bar.reversal_axis()

    # Set the global options for the chart (e.g., title for each year's chart)
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"Top 8 Countries by GDP({year})")  # Set the title with the current year
    )

    # Add the bar chart to the timeline with the year as a label
    timeline.add(bar, str(year))

# Step 6: Configure the timeline's autoplay settings
timeline.add_schema(
    play_interval=1000,  # Set autoplay interval to 1000ms (1 second)
    is_timeline_show=True,  # Display the timeline at the bottom of the chart
    is_auto_play=True,  # Enable autoplay
    is_loop_play=False  # Disable looping of the autoplay
)

# Step 7: Render the timeline chart to an HTML file
timeline.render("Top 8 Countries by GDP(1960-2019).html")