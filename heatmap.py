import matplotlib.pyplot as plt
import numpy as np
from itertools import count
from pandas import *
import pickle as pkl
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable

img_folder = "3-format-heatmap"
csv_name = "3-format.csv"
source_path = "TestData"
fig_name = ""

data = []

file_name = source_path + "/"+ csv_name
data = read_csv(file_name)

y = np.array(data)

for item in y:
    item = np.array(item)
    
counter_set_len =[]


plt.rcParams["figure.figsize"] = 10,2
x = np.linspace(0,15)
for i in range (len(y)):
    X = y[i][2:399]
    
    fig, ax = plt.subplots(1, sharex=True)

    im = ax.imshow(X[np.newaxis,:], cmap="jet", aspect="auto")
    ax.set_yticks([])

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)

    fig.colorbar(im,cax=cax)

    fig_path = source_path+ "/" +img_folder+ "/" + fig_name+ "/" + fig_name + str(i+1)+".jpg"
    fig.savefig(fig_path)
    plt.close()

