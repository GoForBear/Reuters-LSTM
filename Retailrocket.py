import numpy as np
import pandas as pd
import tensorflow as tf
from jpype import *
import os.path
import datetime

train = []
trainChild = []
jarpath = os.path.join(os.path.abspath('.'), 'resource/IdeaProjects.jar')#第二个参数是jar包的路径
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" %(jarpath))#启动jvm
rootDir = "D://天池大赛//hy_round1_train_20200102"
JDClass = JClass("ReadCsv")
jprint = java.lang.System.out.println
a = JDClass.getDirFile(rootDir)
start = datetime.datetime.now()
index = -1
for data in a:
    if int(data[0]) != index:
        index = int(data[0])
        if len(trainChild) >= 1:
            train.append(trainChild)
            trainChild = []
    temp = np.zeros((4,1))
    temp[0]  = float(data[1])
    temp[1] = float(data[2])
    temp[2] = float(data[3])
    temp[3] = float(data[4])
    trainChild.append(temp)
end = datetime.datetime.now()
print (end-start)
shutdownJVM()#最后关闭jvm
print(train[0])

