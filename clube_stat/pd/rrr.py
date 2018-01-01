
import arrow
dt = '2017-12-30 09:35:12'
def f(lst):
    res = []
    for i in lst:
        res.append(arrow.get(i).time().strftime("%H:%M"))
    return res
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts.plot()
# plt.show()