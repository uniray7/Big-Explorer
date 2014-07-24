import json
import commands
import preprocess
import numpy as np
import logs




new_model = logs.logs_object('TeraSort')


target_list = np.array(new_model.get_target_list())

feature_list = np.array(new_model.get_AllFeature_list())
interData_list = np.array(new_model.get_RedMean_list())


import pylab as pl
from sklearn.feature_selection import SelectPercentile, f_regression
from sklearn import svm 


pl.figure(1)
pl.clf()

selector = SelectPercentile(f_regression,percentile=100)
selector.fit(feature_list,interData_list)

scores = -np.log10(selector.pvalues_)
scores /= scores.max()


print selector.transform(feature_list)[0]
print feature_list[0]

X_indices = np.arange(feature_list.shape[-1])

pl.bar(X_indices - .45, scores, width=.2,label=r'Univariate score ($-Log(p_{value})$)', color='g')
clf = svm.SVC(kernel='linear')
clf.fit(feature_list, interData_list)
svm_weights = (clf.coef_ ** 2).sum(axis=0)
svm_weights /= svm_weights.max()
pl.bar(X_indices - .25, svm_weights, width=.2, label='SVM weight', color='r')
clf_selected = svm.SVC(kernel='linear')
clf_selected.fit(selector.transform(feature_list), interData_list)


svm_weights_selected = (clf_selected.coef_ ** 2).sum(axis=0)
svm_weights_selected /= svm_weights_selected.max()
pl.bar(X_indices[selector.get_support()] - .05, svm_weights_selected, width=.2,label='SVM weights after selection', color='b')


pl.title("Comparing feature selection")
pl.xlabel('Feature number')
pl.ylabel('execution time')
pl.yticks(())
pl.axis('tight') 
pl.legend(loc='upper right') 
pl.show()   
