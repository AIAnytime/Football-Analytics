import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar

data = pd.read_csv("/home/sonu/Downloads/fol/radars.csv")


data['Player'] = data['Player'].str.split('\\',expand=True)[0]

data.Player.unique()

data = data[(data['Player']=='Bruno Fernandes') | (data['Player']=='İlkay Gündoğan')].reset_index()

data = data.drop(['index','Rk','Nation','Pos','Squad','Age','Born','90s','FK','PK','PKatt','Matches'],axis=1)

params = list(data.columns)
params = params[1:]

#add ranges to list of tuple pairs
ranges = []
a_values = []
b_values = []

for x in params:
    a = min(data[params][x])
    a = a - (a*.25)
    
    b = max(data[params][x])
    b = b + (b*.25)
    
    ranges.append((a,b))
    
for x in range(len(data['Player'])):
    if data['Player'][x] == 'Bruno Fernandes':
        a_values = data.iloc[x].values.tolist()
    if data['Player'][x] == 'İlkay Gündoğan':
        b_values = data.iloc[x].values.tolist()
        
a_values = a_values[1:]
b_values = b_values[1:]

values = [a_values,b_values]



## title
title = dict(
    title_name='Bruno Fernandes',
    title_color='#F0FFF0',
    subtitle_name='Manchester United',
    subtitle_color='#D43E2A',
    title_name_2='İlkay Gündoğan',
    title_color_2='#F0FFF0',
    subtitle_name_2='Manchester City',
    subtitle_color_2='#C7E0EC',
    title_fontsize=20,
    subtitle_fontsize=18,
)

## endnote 
endnote = "Visualization made by: Sonu. All units are in per90"

radar = Radar(background_color="#121212", patch_color="#28252C", label_color="#F2A365",
              range_color="#F0FFF0")

## plot radar              
fig, ax = radar.plot_radar(ranges=ranges, params=params, values=values, 
                           radar_color=['#D43E2A', '#C7E0EC'], 
                           title=title, endnote=endnote,
                           alphas=[.75,.6], compare=True)