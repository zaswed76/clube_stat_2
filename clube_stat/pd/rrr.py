

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# data_state_names = pd.read_csv('StateNames.csv') # https://www.kaggle.com/kaggle/us-baby-names
# data = data_state_names.query('Name=="Eric" and State=="NY"').sort_values(by='Count',ascending=False).sort_values(by='Year',ascending=False).head(5)

# data = pd.DataFrame({"load": [5, 6, 12], "times": [5, 6, 12]})

import matplotlib.pyplot as plt

load = [5, 6, 12]
times = [1, 3, 6]
width = 0.5
plt.bar(times, load,  width, color="red")
plt.xticks([1,2, 3,4,5, 6])
plt.show()