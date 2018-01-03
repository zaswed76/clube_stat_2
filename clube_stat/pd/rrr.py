

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# data_state_names = pd.read_csv('StateNames.csv') # https://www.kaggle.com/kaggle/us-baby-names
# data = data_state_names.query('Name=="Eric" and State=="NY"').sort_values(by='Count',ascending=False).sort_values(by='Year',ascending=False).head(5)

# data = pd.DataFrame({"load": [5, 6, 12], "times": [5, 6, 12]})

import matplotlib.pyplot as plt

import matplotlib.lines as lines
class Graph:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.mpl_fig = plt.figure()
        self.ax = self.mpl_fig.add_subplot(111)
        self.ax.set_xlabel(self.kwargs.get("x_label", ""))
        self.ax.set_ylabel(self.kwargs.get("y_label", ""))
        plt.title(self.kwargs.get("title", ""))
        y_lim = kwargs.get("y_lim")
        if y_lim:
            plt.ylim([0, y_lim])
        self.plots = {}
        self.index_name = 0
        line1 = [(0,6), (9,6)]



        (line1_xs, line1_ys) = zip(*line1)
        # self.ax2 = self.mpl_fig.add_subplot(211)
        # self.ax2.add_line(lines.Line2D(line1_xs, line1_ys, linewidth=1, color='red'))
        # lines = plt.plot(0, 6, 10, 6)
        # plt.setp(lines, color='r', linewidth=2.0)
        # plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
        self.ax.add_artist(lines.Line2D(line1_xs, line1_ys,
                                        linewidth=0.5, color='white'))

    def set_xtick_label(self, labels):
        self.ax.set_xticks(range(1, len(labels)+1))
        self.ax.set_xticklabels(labels)

    def set_plot(self, x_seq, y_seq, **kwargs):
        try:
            name = kwargs["name"]
        except KeyError:
            name = self.index_name
            self.index_name += 1
        self.plots[name] = self.ax.bar(x_seq, y_seq,
                                       color=kwargs.get("color"),
                                       width=kwargs.get("width", 0.8))

    def show(self):
        plt.show()

    def save(self, path):
        plt.savefig(path)

    def set_legend(self, bg=None, color_matching=False, alpha=1.0):
        plots = []
        names = []
        colors = []
        for n, p in self.plots.items():
            plots.append(p[0])
            names.append(n)
            colors.append(p[0].get_facecolor())
        legend = plt.legend([x for x in plots], names, shadow=False, fancybox=True)
        frame = legend.get_frame()
        frame.set_alpha(alpha)
        frame.set_linewidth(0.1)
        frame.set_edgecolor('black')
        if bg is not None:
            frame.set_facecolor(bg)
        if color_matching:
            for color, text in zip(colors, legend.get_texts()):
                text.set_color(color)



    def set_bg(self, color="lightgrey"):
        self.ax.set_facecolor(color)

if __name__ == '__main__':
    load = [14, 14, 14, 8, 7, 5, 9]
    load2 = [2, 2, 5, 7, 6, 3, 1]
    load3 = [6, 6, 5, 6, 6, 6, 4]
    times = [1, 2, 3, 4, 5, 6, 7]

    gr = Graph(title="les", y_lim=50, x_label="время", y_label="человек")
    gr.set_plot(times, load, name="visitors")
    gr.set_plot(times, load2, color="#E3D969", name="schools")
    gr.set_plot(times, load3, color="red", name="pro", width=0.05)
    gr.set_xtick_label(times)
    gr.set_legend(bg="#C8C8C8", color_matching=False, alpha=0.5)
    gr.set_bg("#D2D2D2")
    gr.show()



