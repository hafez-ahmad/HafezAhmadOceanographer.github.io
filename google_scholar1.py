import pandas as pd
import time 
from bokeh.plotting import figure, output_file, show
date=time.strftime("%Y-%m-%d")
# Dataframe with Google Scholar information
data = {'TotalCitations': [178], 'H-index': [2], 'I10-index': [3]}
df = pd.DataFrame(data)

# Make bar plot and save to an HTML file
# Instantiating the figure object
graph = figure(x_range=df.columns.tolist(), plot_width=400, plot_height=400, title = 'Google Scholar information: '+date)

# x-axis label with font size and style
graph.xaxis.axis_label_text_font_size = "20pt"
graph.xaxis.axis_label_text_font_style = "bold"

# xticks font size and style
graph.xaxis.major_label_text_font_size = "14pt"
graph.xaxis.major_label_text_font_style = "bold"

# Save to an HTML file
output_file("E:/python_projects/HafezAhmadOceanographer.github.io/citebar.html")

# Add values to the bars
for i, v in enumerate(df.iloc[0]):
    graph.text(x=i + 0.5, y=v, text=[str(v)], text_color="black", text_font_size="10pt", text_align="center")

# Bar plot with df
graph.vbar(x=df.columns.tolist(), width=0.9, top=df.iloc[0].values.tolist(), fill_color=['#36AB9D', '#B1F9E1', '#EB8E79'])

show(graph)
