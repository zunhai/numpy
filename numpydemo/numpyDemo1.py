import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt 

def putinfile(file):
    putin=open(file)
    readfile=putin.readlines()
    datalength=len(readfile)
    traindata=np.zeros((datalength,3))
    labels=[]
    index=0
    for line in readfile:
        line = line.rstrip()
        line = line.split("\t")
        traindata[index,:] = line[0:3]
        if line[-1] == "largeDoses":
            labels.append(1)
        if line[-1] == "smallDoses":
            labels.append(2)
        if line[-1] == "didntLike":
            labels.append(3)
        index += 1
    return traindata, labels

def myplot(traindata,labels):
    font=FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc",size=14)

    fig,axes = plt.subplots(nrows=2,ncols=2,sharex=False,sharey=False,figsize=(13,8))
    colorlist = []
    for i in labels:
        if i == 1:
            colorlist.append("red")
        if i == 2:
            colorlist.append("black")
        if i == 3:
            colorlist.append("orange")

    axes[0][0].scatter(x=traindata[:,0], y=traindata[:,1], color=colorlist, s=12, alpha=0.5)
    axes0_set_title = axes[0][0].set_title(u"每年获得的飞行常客里程数与玩视频游戏所消耗时间占比", FontProperties=font)
    axes0_set_xlabel = axes[0][0].set_xlabel(u"每年获得的飞行常客里程数",FontProperties=font)
    axes0_set_ylabel = axes[0][0].set_ylabel(u"玩视频游戏所消耗时间",FontProperties=font)
    plt.setp(axes0_set_title,size=9, weight="bold", color="red")
    plt.setp(axes0_set_xlabel,size=7, weight="bold", color="black")
    plt.setp(axes0_set_ylabel,size=7, weight="bold", color="black")

    axes[0][1].scatter(x=traindata[:,0],y=traindata[:,2], color=colorlist, s=12, alpha=0.5)
    axes1_set_title = axes[0][1].set_title(u"每年获得的飞行常客里程数与每周消费的冰激淋公升数占比",FontProperties=font)
    axes1_set_xlabel = axes[0][1].set_xlabel(u"每年获得的飞行常客里程数",FontProperties=font)
    axes1_set_ylabel = axes[0][1].set_ylabel(u"每周消费的冰激淋公升数",FontProperties=font)
    plt.setp(axes1_set_title,size=9, weight="bold", color="red")
    plt.setp(axes1_set_xlabel,size=7, weight="bold", color="black")
    plt.setp(axes1_set_ylabel,size=7, weight="bold", color="black")

    axes[1][0].scatter(x = traindata[:,1],y=traindata[:,2], color=colorlist, s=12, alpha=0.5)
    axes2_set_title = axes[1][0].set_title(u"玩视频游戏所消耗时间占比与每周消费的冰激淋公升数",FontProperties=font)
    axes2_set_xlabel = axes[1][0].set_xlabel(u"玩视频游戏所消耗时间",FontProperties=font)
    axes2_set_ylabel = axes[1][0].set_ylabel(u"每周消费的冰激淋公升数",FontProperties=font)
    plt.setp(axes2_set_title,size=9, weight="bold", color="red")
    plt.setp(axes2_set_xlabel,size=7, weight="bold", color="black")
    plt.setp(axes2_set_ylabel,size=7, weight="bold", color="black")

    largeDoses = mlines.Line2D([],[],color="red",marker=".", markersize=6,label="largeDoses")
    smallDoses = mlines.Line2D([],[],color="black",marker=".", markersize=6, label="smallDoses")
    didntLike = mlines.Line2D([],[],color="orange",marker=".", markersize=6, label="didntLike")
    axes[0,0].legend(handles=[largeDoses,smallDoses,didntLike])
    axes[0,1].legend(handles=[largeDoses,smallDoses,didntLike])
    axes[1,0].legend(handles=[largeDoses,smallDoses,didntLike])
    plt.show()
    
def standdata(traindata):
    meandata0 = np.mean(traindata,axis=0)
    stddata0 = np.std(traindata,axis=0)
    length = traindata.shape[0]
    meandata1 = np.tile(meandata0,(length,1))
    stddata1 = np.tile(stddata0,(length,1))
    standdata = (traindata-meandata1)/stddata1
    return standdata, meandata0, stddata0

if __name__ == "__main__":
    file="hailunYuehuiData.txt"
    traindata, labels = putinfile(file)
    myplot(traindata,labels)