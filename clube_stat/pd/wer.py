

import numpy as np
import matplotlib.pyplot as plt

N = 24
men_means = (20, 31, 29, 30, 27, 20, 31, 22, 24, 25, 23, 25, 20, 20, 27, 20, 31, 29, 30, 27, 20, 31, 22, 24)


ind = np.arange(N)  # the x locations for the groups
width = 0.8       # the width of the bars

fig, ax = plt.subplots()
fig.patch.set_facecolor('grey')
rects1 = ax.bar(ind, men_means, width, color='#2464CD')

women_means = [x-10 for x in (20, 31, 29, 30, 27, 20, 31, 22, 24, 25, 23, 25, 20, 20, 27, 20, 31, 29, 30, 27, 20, 31, 22, 24)]

# rects2 = ax.bar(ind + width, women_means, width, color='#F8EF3E')

# add some text for labels, title and axes ticks
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

# ax.legend((rects1[0], rects2[0]), ('visitor', 'school'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
# autolabel(rects2)
# ax.set_facecolor('#E1E1E1')

plt.show()