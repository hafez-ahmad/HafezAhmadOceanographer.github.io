
import time 
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

print('imported')
date = time.strftime("%Y-%m-%d")

from bokeh.plotting import figure, show

# Dataframe with Google Scholar information
data = ['TotalCitations', 'H-index', 'I10-index']
counts = [205, 2, 3]

# Create a figure
p = figure(x_range=data, height=350, title="Citations up to "+ date, toolbar_location=None, tools="")

# Plot the vertical bars
p.vbar(x=data, top=counts, width=0.9, color=['#36AB9D', '#B1F9E1', '#EB8E79'])
# Save to an HTML file
output_file("D:/python_projects/HafezAhmadOceanographer.github.io/citebar.html")
# Customize the plot
p.xgrid.grid_line_color = None
p.y_range.start = 0

# Show the plot
show(p)

