import time
import pandas as pd
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource, HoverTool, Label, LabelSet, Range1d, Title
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6, Turbo256, Viridis256
from bokeh.layouts import column, row
from bokeh.models.widgets import Div
from bokeh.io import curdoc
import os

print('Script started')
date = time.strftime("%Y-%m-%d")

# You can update these citation metrics manually or implement automatic scraping
data = ['Total Citations', 'h-index', 'i10-index']
counts = [331, 5, 3]

# Create a pandas DataFrame for better data handling
df = pd.DataFrame({
    'metric': data,
    'value': counts,
    'color': ['#1976D2', '#03A9F4', '#00BCD4'],  # Modern blue palette
    'description': [
        'Total number of times your work has been cited by others',
        'h articles with at least h citations each',
        'Number of articles with at least 10 citations'
    ]
})

# Create ColumnDataSource for Bokeh
source = ColumnDataSource(df)

# Create a more visually appealing figure
p = figure(
    x_range=df['metric'].tolist(),
    height=450,
    width=650,
    title="Google Scholar Metrics (as of " + date + ")",
    toolbar_location="right",
    tools="pan,wheel_zoom,box_zoom,reset,save",
    sizing_mode="stretch_width",
    background_fill_color="#f5f5f5",
    border_fill_color="white",
)

# Add gradient visual bar chart with hover effects
vbars = p.vbar(
    x='metric',
    top='value',
    width=0.7,
    source=source,
    line_color="white",
    fill_color='color',
    line_width=2,
    alpha=0.8,
    hover_line_color="darkgrey",
    hover_fill_color="color",
    hover_alpha=1.0,
)

# Add hover tool with custom tooltip
hover = HoverTool(
    renderers=[vbars],
    tooltips=[
        ("Metric", "@metric"),
        ("Value", "@value"),
        ("Description", "@description")
    ],
    mode="mouse"
)
p.add_tools(hover)

# Add value labels on top of bars
labels = LabelSet(
    x='metric',
    y='value',
    text='value',
    text_font_size="12pt",
    text_color="black",
    text_align="center",
    text_baseline="bottom",
    y_offset=10,
    source=source
)
p.add_layout(labels)

# Style the plot
p.title.text_font_size = "16pt"
p.title.text_font_style = "bold"
p.title.align = "center"
p.xaxis.major_label_text_font_size = "12pt"
p.xaxis.major_label_text_font_style = "bold"
p.yaxis.major_label_text_font_size = "12pt"
p.yaxis.axis_label = "Count"
p.yaxis.axis_label_text_font_size = "14pt"
p.yaxis.axis_label_text_font_style = "bold"
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = max(counts) * 1.2  # Add some space above bars
p.outline_line_color = "black"
p.outline_line_width = 1
p.xaxis.major_tick_line_color = None  # Hide x-axis major ticks
p.xaxis.minor_tick_line_color = None  # Hide x-axis minor ticks

# Add subtitle as a separate annotation
subtitle = Label(
    x=0, 
    y=max(counts) * 1.1, 
    text="Data from Google Scholar Profile",
    text_font_size="12pt",
    text_font_style="italic"
)
p.add_layout(subtitle)

# Linear trend for previous years (example data - replace with actual historical data)
# For demonstration, using synthetic data
years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026']  # Replace with actual years
yearly_citations = [1, 3, 29, 46, 69, 68, 81, 132,26]  # Replace with your actual yearly citation counts

# Add a second plot for citation trends
trend_source = ColumnDataSource(data=dict(
    years=years,
    citations=yearly_citations
))

trend_plot = figure(
    height=250,
    width=650,
    title="Citation Growth Over Time",
    x_range=years,
    toolbar_location="right",
    tools="pan,wheel_zoom,box_zoom,reset,save",
    sizing_mode="stretch_width",
    background_fill_color="#f5f5f5",
)

# Line with markers for citation trend
trend_plot.line('years', 'citations', line_width=3, line_color="#00796B", source=trend_source)
trend_plot.circle('years', 'citations', size=10, color="#009688", 
                  line_color="white", line_width=2, source=trend_source,
                  hover_fill_color="#4DB6AC", hover_line_color="white")

# Style the trend plot
trend_plot.title.text_font_size = "14pt"
trend_plot.xaxis.major_label_text_font_size = "10pt"
trend_plot.yaxis.major_label_text_font_size = "10pt"
trend_plot.yaxis.axis_label = "Total Citations"
trend_plot.yaxis.axis_label_text_font_size = "12pt"
trend_plot.xaxis.axis_label = "Year"
trend_plot.xaxis.axis_label_text_font_size = "12pt"
trend_plot.y_range.start = 0
trend_plot.add_tools(HoverTool(
    tooltips=[
        ("Year", "@years"),
        ("Citations", "@citations"),
    ],
    mode="mouse"
))

# Save to an HTML file with responsive design
output_file("C:/Users/hafez/MSU/Research/HafezAhmadOceanographer.github.io/citebar.html")

# Combine plots into a single layout
layout = column(p, trend_plot, sizing_mode="stretch_width")

# Save the layout
save(layout)
print(f"Citation visualization updated on {date}")

# Uncomment this section if you want to display the plot while running the script
# show(layout)

