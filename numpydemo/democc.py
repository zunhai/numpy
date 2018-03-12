import os
import io
import numpy as np
import matplotlib.pyplot as plt
# dtype=np.float
# a=[]
# np.savetxt("fangziData.txt",a)
# a =numpy.loadtxt("fangziData.txt", delimiter=',')  
# with open('fangziData.txt', 'r') as f:  
#     data = f.readlines()  #txt中所有字符串读入data  
    
#     for line in data:  
#         data = line.split("\n") 
             
#     print(data) 

file = open("fangziData.txt","r")  
list_arr = file.readlines()  
  
lists = []  
  
for index,x in enumerate(list_arr):  
    x = x.strip()  
    x = x.strip('[]')  
    x = x.split(",")  
    lists.append(x)


# a = a.astype(int)  
print (lists)  
plt.plot();
plt.plot();


plt.show();


file.close() 
# x , y= [],[];
# print(dataArr)
# for item in dataArr:
#     # a = item.
#     a = item.split(",");
#     if a[0] != "":
#         x.append(int(a[0]));
#         y.append(int(a[1]));
# #将数据绘制到界面上
# plt.scatter(x , y);
