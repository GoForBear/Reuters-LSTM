import  sklearn
import pandas as pd
from sklearn import  tree
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler


csv_data = pd.read_csv("demo.csv")
i = 0
label = []
data = []
print("开始处理数据")
for i in range(csv_data.shape[0]):
    temp = []
    for j in range(csv_data.shape[1]):
        if j <2 :
            continue
        elif j == 6:
            label.append(csv_data.loc[i][j])
        elif j< 28:
            temp.append(csv_data.loc[i][j])
        else:
            continue
    data.append(temp)
# print("处理数据完毕")
print("开始切分数据集")
X_train = data[0:int(20000*0.8)]
y_train = label[0:int(20000*0.8)]
X_test = data[int(20000*0.8):]
y_test = label[int(20000*0.8):]
print("开始分类")
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
predict = clf.predict(X_test)
print('Accuracy of tree Classifier:', clf.score(X_test, y_test))






# print(data[2])
# print(label[2])