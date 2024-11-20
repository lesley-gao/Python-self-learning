from pyecharts.charts import Line

line = Line()

line.add_xaxis(["China","USA","UK"])

line.add_yaxis("GDP", [30, 20, 10])

line.render()