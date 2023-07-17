import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd

def Generate_heatmap(heatmap_input_array, graph_max, graph_font, graph_title, graph_x_axis_label, graph_y_axis_label):

    df_cm = pd.DataFrame(heatmap_input_array, columns = [i for i in graph_x_axis_label])

    plt.rcParams["font.family"] = graph_font
    plt.title(graph_title)
    ax = sns.heatmap(df_cm, vmin = 0, vmax = graph_max, linewidth=0.5)
    plt.draw()
    ax.set_yticklabels(graph_y_axis_label, rotation = 0)
    plt.show()
    return()