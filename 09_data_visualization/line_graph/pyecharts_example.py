from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts
import json

# 数据处理
# 打开美国和印度数据所在的文件
file_us = open("../../assets/USA.txt", "r", encoding="UTF-8")
file_in = open("../../assets/India.txt", "r", encoding="UTF-8")
#读取文件的全部内容
us_data = file_us.read()
in_data = file_in.read()
#去掉不合JSON规范的开头（将开头的不相关字符换为空）
us_data = us_data.replace("jsonp_1629344292311_69436(","")
in_data = in_data.replace("jsonp_1629350745930_63180(","")

# 去掉不合JSON规范的结尾
us_data = us_data[:-2] #去掉最后的两个字符
in_data = in_data[:-2]

# JSON转Python字典
us_dict = json.loads(us_data)
in_dict = json.loads(in_data)
print(type(us_dict))
print(type(in_dict))
print(us_dict)
print(in_dict)

# 获取trend data
us_trend_data = us_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]

# 获取日期数据，用于X轴，取2020年日期即可
us_x_data= us_trend_data["updateDate"][:314]   # 2020年日期到314下标结束
in_x_data= in_trend_data["updateDate"][:314]   # 2020年日期到269下标结束

# 获取确认数据，用于Y轴，取2020年日期即可
us_y_data = us_trend_data["list"][0]["data"][:314]  # 2020年日期到314下标结束
in_y_data = in_trend_data["list"][0]["data"][:314]  # 2020年日期到269下标结束

# 生成图表
line = Line()      # 构建折线图对象

# 添加 X 轴和 Y 轴数据
line.add_xaxis(us_x_data)  # x轴是公用的，所以使用一个国家的数据即可
line.add_yaxis("USA Covid-19 Confirmed Cases", us_y_data, label_opts=LabelOpts(is_show=False))    #添加美国的y轴数据,
                                                                    # label_opts=LabelOpts(is_show=False)的作用是不将数字显示在图表上
line.add_yaxis("India Covid-19 Confirmed Cases", in_y_data, label_opts=LabelOpts(is_show=False))    #添加印度的y轴数据

# 设置全局配置，包括标题、工具箱
line.set_global_opts(
    title_opts=TitleOpts(title="Comparison of Covid-19 Confirmed Cases", pos_left="center", pos_bottom="0%"),
    toolbox_opts=ToolboxOpts(is_show=True)
)

# 调用render方法，生成图表，输出到HTML文件
line.render()

#关闭文件对象
file_in.close()
file_us.close()