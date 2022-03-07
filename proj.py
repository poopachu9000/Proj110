import pandas as pd
import plotly.express as px
import csv
import statistics
import plotly.figure_factory as pf
import random
import plotly.graph_objects as go
from collections import Counter

df = pd.read_csv('medium_data.csv')
data = df['claps'].tolist()
pop_mean = statistics.mean(data)
print(pop_mean)
#standard_deviation_temp = statistics.stdev(data)

#print(temp_mean)
#print(standard_deviation_temp)

#fig = pf.create_distplot([data], ['temp'], show_hist = False)
#data_set = []
#for i in range(0,1000):
 #   randomIndex = random.randint(0,len(data))
  #  value = data[randomIndex]
   # data_set.append(value)
#mean1 = statistics.mean(data_set)
#standard_deviation1 = statistics.stdev(data_set)
#print(mean1)
#print(standard_deviation1)

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = pf.create_distplot([df], ['claps'], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.01], mode = 'lines',name = 'mean'))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print(mean)

setup()