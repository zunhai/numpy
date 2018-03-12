import numpy as np

import matplotlib.pyplot as plt



# file = open("fangziData.txt");
file = open("chusheng.txt");
data = file.read();

dataArr = data.split("\n");
# print(dataArr);   
year,boy,girl = [],[],[];
for item in dataArr:
    print(item);
    data = item.split(" ");
    print(data);
    if len(data) == 4:
        year.append(int(data[1]))
        boy.append(int(data[2]))
        girl.append(int(data[3]))
print(year);
print(boy);
print(girl);

plt.plot(year,boy);
plt.plot(year,girl);


plt.show();
