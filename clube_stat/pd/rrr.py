

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# data_state_names = pd.read_csv('StateNames.csv') # https://www.kaggle.com/kaggle/us-baby-names
# data = data_state_names.query('Name=="Eric" and State=="NY"').sort_values(by='Count',ascending=False).sort_values(by='Year',ascending=False).head(5)

# data = pd.DataFrame({"load": [5, 6, 12], "times": [5, 6, 12]})

import matplotlib.pyplot as plt

load = [5, 6, 12]
load2 = [2, 2, 5]
times = [1, 3, 6]
# width = 0.8
# ax = plt.bar(times, load)
# ax2 = plt.bar(times, load2)
#
# # plt.xticks([1,2, 3,4,5, 6])
# plt.title('Клуб Лесной')
# plt.show()

class Graph:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.mpl_fig = plt.figure()
        self.ax = self.mpl_fig.add_subplot(111)
        plt.title(self.kwargs.get("title", ""))
        plt.rcParams['figure.facecolor'] = 'black'
        self.plots = {}
        self.index_name = 0


    def set_plot(self, x_seq, y_seq, **kwargs):
        try:
            name = kwargs["name"]
        except KeyError:
            name = self.index_name
            self.index_name += 1
        self.plots[name] = self.ax.bar(x_seq, y_seq, color=kwargs.get("color"))

    def show(self):
        plt.show()

    def save(self, path):
        plt.savefig(path)

    def set_legend(self, bg=None, color_matching=False):
        plots = []
        names = []
        colors = []
        for n, p in self.plots.items():
            plots.append(p[0])
            names.append(n)
            colors.append(p[0].get_facecolor())
        legend = plt.legend([x for x in plots], names, shadow=True)
        frame = legend.get_frame()
        if bg is not None:
            frame.set_facecolor(bg)
        if color_matching:
            for color, text in zip(colors, legend.get_texts()):
                text.set_color(color)


    def set_bg(self, color="lightgrey"):
        self.ax.set_facecolor(color)


gr = Graph(title="les")
gr.set_plot(times, load, name="visitors")
gr.set_plot(times, load2, color="#E3D969", name="schools")
gr.set_legend(bg="#C8C8C8", color_matching=False)
gr.set_bg("#D2D2D2")
gr.show()

# gr.save("dddd.png")

