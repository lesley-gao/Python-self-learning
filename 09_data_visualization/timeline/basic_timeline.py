from pyecharts.charts import Timeline, Bar
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["China", "USA", "UK"])
bar1.add_yaxis("GDP", [30, 30, 20], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["China", "USA", "UK"])
bar2.add_yaxis("GDP", [50, 50, 50], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["China", "USA", "UK"])
bar3.add_yaxis("GDP", [70, 60, 60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# Create a timeline object, and set the theme
timeline = Timeline({"theme":ThemeType.LIGHT})

# Add bar chart objects to the timeline
timeline.add(bar1, "Point 1")
timeline.add(bar2, "Point 2")
timeline.add(bar3, "Point 3")

# Set the autoplay configuration
timeline.add_schema(
    play_interval=1000,      # Time interval for autoplay
    is_timeline_show=True,   # Whether to display the timeline during autoplay
    is_auto_play=True,       # Whether to enable autoplay
    is_loop_play=True        # Whether to enable looping autoplay
)

# Render the chart using the timeline object, not the bar objects
timeline.render("basic_timeline.html")

