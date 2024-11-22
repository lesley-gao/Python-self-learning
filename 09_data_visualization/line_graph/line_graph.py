from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, LabelOpts
import json

# Data processing
# Open the files containing data for the USA and India
file_us = open("../../assets/USA.txt", "r", encoding="UTF-8")
file_in = open("../../assets/India.txt", "r", encoding="UTF-8")
file_jp = open("../../assets/Japan.txt", "r", encoding="UTF-8")

# Read the entire content of the files
us_data = file_us.read()
in_data = file_in.read()
jp_data = file_jp.read()

# Remove the non-JSON-compliant prefix (replace unrelated characters at the beginning with an empty string)
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")

# Remove the non-JSON-compliant suffix
us_data = us_data[:-2]  # Remove the last two characters
in_data = in_data[:-2]
jp_data = jp_data[:-2]

# Convert JSON to Python dictionary
us_dict = json.loads(us_data)
in_dict = json.loads(in_data)
jp_dict = json.loads(jp_data)
print(us_dict)
print(in_dict)
print(jp_data)

# Retrieve trend data
us_trend_data = us_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]

# Retrieve date data for the X-axis, using dates from 2020
us_x_data = us_trend_data["updateDate"][:314]   # Dates up to index 314 for the year 2020
in_x_data = in_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]

# Retrieve confirmation data for the Y-axis, using data from 2020
us_y_data = us_trend_data["list"][0]["data"][:314]  # Data up to index 314 for the year 2020
in_y_data = in_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]

# Generate chart
line = Line()      # Create a line chart object

# Add X-axis and Y-axis data
line.add_xaxis(us_x_data)  # X-axis is shared, so we use data from one country
line.add_yaxis("GDP of USA", us_y_data, label_opts=LabelOpts(is_show=False))    # Add Y-axis data for the USA
                                                                    # label_opts=LabelOpts(is_show=False) hides numbers on the chart
line.add_yaxis("GDP OF India", in_y_data, label_opts=LabelOpts(is_show=False))  # Add Y-axis data for India
line.add_yaxis("GDP OF Japan", jp_y_data, label_opts=LabelOpts(is_show=False))  # Add Y-axis data for Japan

# Set global options, including title and toolbox
line.set_global_opts(
    title_opts=TitleOpts(title="Comparison of GDP", pos_left="center", pos_bottom="0%"),
    toolbox_opts=ToolboxOpts(is_show=True)
)

# Call the render method to generate the chart and output it to an HTML file
line.render("GDP.html")    # If only line.render() is used, the HTML file name is not specified

# Close the file objects
file_in.close()
file_us.close()
file_jp.close()