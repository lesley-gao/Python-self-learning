from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

# Create an instance of the Bar chart
bar = Bar()

# Add data for the x-axis
bar.add_xaxis(["China", "USA", "UK"])

# Add data for the y-axis (GDP values)
# The labels for the GDP values will be displayed on the "right" side of the bars
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

# Reverse the x and y axes so that the chart is displayed horizontally
bar.reversal_axis()

# Render the chart to an HTML file
bar.render("basic_bar_chart.html")