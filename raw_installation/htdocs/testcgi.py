#!C:\Python34\python.exe
print("Content-type: text/html")
print("")
print("<html><head>")
print("")
print("</head><body>")
print("Hello from Python.")
print("</body></html>")

import pandas as pd
import numpy as np

print('asd')
s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print(df)
print("Content-type: text/html")
print("<html><head>")
print("")
print("</head><body>")
print("Hello.")
print("</body></html>")

print(df.to_html())