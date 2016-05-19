#coding=utf-8
import xgboost as xgb
import pandas as pd
import time
import numpy as np
from graphviz import *


dataset = pd.read_csv(r"E:\Desktop\Desktop\data\DigitRecognizer\train.csv") # 注意自己数据路径

train = dataset.iloc[:,1:].values
labels = dataset.iloc[:,:1].values

tests = pd.read_csv(r"E:\Desktop\Desktop\data\DigitRecognizer\test.csv") # 注意自己数据路径
test = tests.iloc[:,:].values

params={
'booster':'gbtree',
'objective': 'multi:softmax',
'num_class':10,
'gamma':0.05,
'max_depth':12,
'eval_metric':'merror',
#'lambda':450,
'subsample':0.4,
'colsample_bytree':0.7,
#'min_child_weight':12,
'silent':0 ,
'eta': 0.005, # 如同学习率
'seed':710,
'nthread':4,# cpu 线程数
}

plst = list(params.items())

#Using 10000 rows for early stopping.
offset = 35000

num_rounds = 8
xgtest = xgb.DMatrix(test)

# 划分训练集与验证集
xgtrain = xgb.DMatrix(train[:offset,:], label=labels[:offset])
xgval = xgb.DMatrix(train[offset:,:], label=labels[offset:])

# return 训练和验证的错误率
watchlist = [(xgtrain, 'train'),(xgval, 'val')]


# training model
model = xgb.train(plst, xgtrain, num_rounds, watchlist,early_stopping_rounds=8)
preds = model.predict(xgval,ntree_limit=model.best_iteration)
#auc = metrics.roc_auc_score(labels[offset:], preds, sample_weight=None) 多分类不支持
# 将预测结果写入文件，方式有很多，自己顺手能实现即可
#np.savetxt('E:\Desktop\submission_xgb_MultiSoftmax.csv',np.c_[range(1,len(test)+1),preds],
#               delimiter=',',header='ImageId,Label',comments='',fmt='%d')



