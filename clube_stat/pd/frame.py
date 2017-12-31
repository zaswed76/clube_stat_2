
import pandas as pd

data = {"clubs": ["les", "troya", "akadem"],
        "visitors": [5, 7, 9], "load": [8, 9, 11]}
index = ['one', 'twO', 'three']
df = pd.DataFrame(data, columns=["clubs", "visitors", "load", "comp"])
df["comp"] = [50, 40, 34]
r = df[df["load"]> 8]
# print(df)
print(r)

