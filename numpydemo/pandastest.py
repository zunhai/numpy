import pandas
import numpy as np
import matplotlib.pyplot as plt
import requests




surl="http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt"

content = pandas.read_table(surl,sep=" ")

print(content)
contents=content.set_index("year")
contents["boys"].plot(color='b')
contents["girls"].plot(color='r')

plt.legend(loc="best")
# contents.plot()
plt.show()
