import pandas as pa
daily_status={'day':['mon','tus','wed'],
              'sleping':[12,6,8],
              'ex':[56,33,55],
              'working':[6,8,4]}
ds=pa.DataFrame(daily_status)
print(ds)
import matplotlib.pyplot as py
from matplotlib import style
print(style.available)
style.use('fivethirtyeight')
ds['ex'].plot()
py.show()