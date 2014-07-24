import logs
import preprocess
import numpy as np
import cPickle
new_model = logs.logs_object('TeraSort')

ratio =-300

MapFeature_list = new_model.get_MapFeature_list()

RedFeature_list =new_model.get_RedFeature_list()
MapFeature_list_test = MapFeature_list[ratio:]
RedFeature_list_test = RedFeature_list[ratio:]


target_list = new_model.get_target_list()

target_list_train = target_list[:ratio]
target_list_test = target_list[ratio:]

with open('Map.model','rb') as MP:
	knn = cPickle.load(MP)
with open('Reduce.model','rb') as RD:
	LR = cPickle.load(RD)
with open('Job.model','rb') as JOB:
	knn2 = cPickle.load(JOB)


MapMean_list = knn.predict(MapFeature_list_test)
RedMean_list = LR.predict(RedFeature_list_test)

interData_list = []
for i in range(len(MapMean_list)):
	interData_list.append(np.hstack((MapMean_list[i],RedMean_list[i])))

#print new_model.get_error_rate(new_model.get_MapMean_list()[ratio:],MapMean_list)
#print '\n'
#print new_model.get_error_rate(new_model.get_RedMean_list()[ratio:],RedMean_list)
#print '\n'
error_rate = new_model.get_error_rate(target_list_test,knn2.predict(interData_list))
print error_rate


