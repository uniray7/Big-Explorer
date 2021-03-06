import logs
import preprocess
import numpy as np
import cPickle

from sklearn import cross_validation

new_model = logs.logs_object('TeraSort')

ratio = -300
MapFeature_list = np.array(new_model.get_MapFeature_list()[:ratio])
RedFeature_list =np.array(new_model.get_RedFeature_list()[:ratio])
MapMean_list = np.array(new_model.get_MapMean_list()[:ratio])
RedMean_list = np.array(new_model.get_RedMean_list()[:ratio])
target_list = np.array(new_model.get_target_list()[:ratio])


interData_list = []
for i in range(len(MapMean_list)):
	interData_list.append(np.hstack((MapMean_list[i],RedMean_list[i])))


from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor()
knn.fit(MapFeature_list,MapMean_list)
with open('Map.model','wb') as MP:
	cPickle.dump(knn,MP)
print knn.score(MapFeature_list,MapMean_list)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(RedFeature_list,RedMean_list)
with open('Reduce.model','wb') as RP:
	cPickle.dump(regressor,RP)
print regressor.score(RedFeature_list,RedMean_list)



knn2 = KNeighborsRegressor(p=1)
knn2.fit(interData_list,target_list)
with open('Job.model','wb') as JP:
	cPickle.dump(knn2,JP)
print knn2.score(interData_list,target_list)



