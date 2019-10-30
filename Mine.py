import pandas as pd

csv_data = pd.read_csv("C:\\Users\\为了熊\Desktop\\工作\\数据挖掘\\xhzw_OUTPUT_0051_19050607.csv")  # 读取训练数据
newD = csv_data.loc[0:20000]
newD.to_csv("demo.csv")