import pandas as pd

flows = pd.read_csv("flows.csv")

grouped = flows.groupby(
    ["src_ip", "dst_ip", "dst_port"]
).size()

print(grouped.sort_values(ascending=False).head(20))
