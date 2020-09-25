from Motion_detection_through_webcam import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource

df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height = 400, width = 1500, title="Motion Tracking Plot")
p.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips = [("Start:" ,"@Start_String"), ("End: " ,"@End_String")])
p.add_tools(hover)

q = p.quad(left = "Start", right = "End", bottom = 0, top = 1, color = 'indigo', source=cds)

output_file("Graph.html")
show(p)