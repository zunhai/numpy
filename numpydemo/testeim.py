import os
import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties 

font = FontProperties(fname=r"./simsun/simsun.ttc", size=14) 

df = pd.DataFrame({"山东省": [3872.18, 5960.42, 6650.02, 7162.2, 7662.1, 8542.44] , 
            "江苏省": [4057.39, 6004.21, 6680.34, 7199.95, 7697.82, 8582.727627]},
            index=["1995年", "1996年", "1997年", "1998年", "1999年", "2000年"])

ax = df.plot(color=["g", "r"],style=["--","-"], title=u"山东江苏GDP(单位:亿元)")

labels = ax.get_xticklabels()+ax.legend().texts+[ax.title]
for label in labels : 
    label.set_fontproperties(font) 

    
plt.show()