import logs
import preprocess
import numpy as np
new_model = logs.logs_object('TeraSort')


feature_list = preprocess.PreProcess(new_model.get_RedFeature_list())

MapMean_list = new_model.get_MapMean_list()
RedMean_list = new_model.get_RedMean_list()
target_list = new_model.get_target_list()


feature_list_train = feature_list[:-10] 
feature_list_test = feature_list[-10:]
MapMean_list_train = MapMean_list[:-10]
RedMean_list_train = RedMean_list[:-10]
target_list_train = target_list[:-10]
target_list_test = target_list[-10:]

interData_list = []
for i in range(len(MapMean_list)):
	interData_list.append(np.hstack((MapMean_list[i],RedMean_list[i])))


interData_list_train = interData_list[:-10]
interData_list_test = interData_list[-10:]

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor()
knn.fit(interData_list_train, target_list_train)

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(interData_list_train, target_list_train)

error_rate = new_model.get_error_rate(target_list_test,knn.predict(interData_list_test))
print error_rate

error_rate = new_model.get_error_rate(target_list_test,LR.predict(interData_list_test))
print error_rate


#print "error_rate:"+str(error_rate)


