import numpy as np


dataArr = np.array([[1,100] , [45 , 123] ,  [143, 23] , [116 , 8]])
labels = ["爱情片","爱情片","动作片","动作片"]

#k临近算法 iknn
# testData 测试数据 
#  dataSet训练数据 样本数据
# labels 分类标签
# K KNN算法中 算法参数 ,选择距离最小的 K个点

def kNNClassify(testData , dataSet , labels , k):

    dataHang = dataSet.shape[0]
    # 在x方向上 重复 testData 共 1 次
    # 在y方向上 重复 testData 共 dataHang 次
    # 将一个测试数据 重复 4行 1 列  跟样本集一样的矩阵结构
    xiangLiangJuzhen = np.tile(testData , (dataHang , 1)) - dataSet

    xiangLiangJuzhenPingfang = xiangLiangJuzhen ** 2

    XYqiuhe = xiangLiangJuzhenPingfang.sum(axis = 1)

    distance = XYqiuhe **0.5

    sortDistance = distance.argsort()

    distance.sort(axis=0)

    leibieCount = {}

    for i in range(k):
        xiabiao = sortDistance[i]
        leibie = labels[xiabiao]


        leibieCount[leibie] = leibieCount.get(leibie , 0) + 1

    print(leibieCount)

#动作类型
testMovie = [101 , 22]

result = kNNClassify(testMovie ,dataArr , labels , 3)

print(result)



