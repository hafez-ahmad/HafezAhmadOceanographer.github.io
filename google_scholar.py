# beutifshop
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time 
from bokeh.io import output_file, show
from bokeh.plotting import figure
date=time.strftime("%Y-%m-%d")
url='https://scholar.google.com/citations?user=ToH-NhkAAAAJ&hl=en'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
# find 'Citations"  in 'class="gsc_rsb_std"'
Citations=soup.find('td',class_="gsc_rsb_std").text
print(Citations)
total=[]
# find 'h-index' in 'class="gsc_rsb_std"'
for i in soup.find_all('td',class_="gsc_rsb_std"):
    # take 0,3,5 elements
    total.append(i.text)
print(total)
# select the 0,3,5 elements
all=['TotalCitations','H-index','I10-index']
# select the 0,3,5 elemen
index=[0,3,5]
total=[total[i] for i in index]
df=pd.DataFrame(total,index=all,columns=['value'])
# save to txt file
#df.to_csv(f'google_scholar_{date}.txt',sep='\t')
# make values as integers
df['value']=df['value'].astype(int)
# make bar plot and save to html file
# instantiating the figure object
graph = figure(x_range=df.index.values.tolist(),plot_width=400, plot_height=400,title = 'Google Scholar information: '+date)
# x-axis label with font size
#graph.xaxis.axis_label = 'Indices'
# font 20 and bold
graph.xaxis.axis_label_text_font_size = "20pt"
graph.xaxis.axis_label_text_font_style = "bold"
# xticks font size
graph.xaxis.major_label_text_font_size = "14pt"
graph.xaxis.major_label_text_font_style = "bold"
# save to html file
output_file("E:/python_projects/HafezAhmadOceanographer.github.io/citebar.html")
# add values to the bars
for i, v in enumerate(df['value']):
    graph.text(x=i+0.5, y=v, text=[str(v)], text_color="black", text_font_size="10pt", text_align="left")
# bar plot with df
graph.vbar(x = df.index.values.tolist(),  width=0.9,top = df['value'].values.tolist(),fill_color=['#36AB9D','#B1F9E1','#EB8E79'])
show(graph)