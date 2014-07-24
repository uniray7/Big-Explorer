import logs
import numpy as np
import cPickle

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor



class WhatIf_Engine:
	def __init__(self,MapFeature_list,RedFeature_list,MapMean_list,RedMean_list,MapDev_list,RedDev_list,Target_list):
		self.MapFeature_list = MapFeature_list
		self.RedFeature_list = RedFeature_list
		self.MapMean_list = MapMean_list
		self.RedMean_list = RedMean_list
		self.MapDev_list = MapDev_list
		self.RedDev_list = RedDev_list
		self.Target_list = Target_list

	def Build_MapMean_Model(self):
		knn_MapMean = KNeighborsRegressor()
		knn_MapMean.fit(self.MapFeature_list,self.MapMean_list)
		self.Dump_Model('Model/MapMean.model',knn_MapMean)

	def Build_MapDev_Model(self):
		knn_MapDev = KNeighborsRegressor()
		knn_MapDev.fit(self.MapFeature_list,self.MapDev_list)
		self.Dump_Model('Model/MapDev.model',knn_MapDev)


	def Build_RedMean_Model(self):
		DTR_RedMean = DecisionTreeRegressor()
		DTR_RedMean.fit(self.RedFeature_list,self.RedMean_list)
		self.Dump_Model('Model/ReduceMean.model',DTR_RedMean)


	def Build_RedDev_Model(self):
		DTR_RedDev = DecisionTreeRegressor()
		DTR_RedDev.fit(self.RedFeature_list,self.RedDev_list)
		self.Dump_Model('Model/ReduceDev.model',DTR_RedDev)


	def Concate_Task_Feature(self):
		interData_list = []
		for i in range(len(self.MapMean_list)):
			wave = (float(self.MapFeature_list[i][-1])*1024)/(8*float(self.MapFeature_list[i][1])*float(self.MapFeature_list[i][2]))
			interData_list.append(np.hstack(((self.MapMean_list[i])*int(wave),self.RedMean_list[i])))
		return interData_list


	def Build_Final_Model(self):
		interData_list = self.Concate_Task_Feature()
		from sklearn import linear_model
		knn_Final = linear_model.LinearRegression()
		
		knn_Final.fit(interData_list,self.Target_list)
		print 'finish'
		self.Dump_Model('Model/Job.model',knn_Final)
		

#		import sys
#		sys.path.append('/home/trend-hadoop/expr/implementation/libsvm-3.18/python')
#		from svm import *
#		from svmutil import *
#		x_dict_list = []
#		for x_array in interData_list:
#			i = 1
#			x_dict = dict()
#			for x_feature in x_array:
#				x_dict.update({i:float(x_feature)})
#				i = i+1
#			x_dict_list.append(x_dict)
#		
#		problem = svm_problem(self.Target_list,x_dict_list)
#
#		param = svm_parameter()
##		param.svm_type=3
#		param.kernel_type=1
#		param.degree=2
#		param.cost=10
#		param.epsilon=100
#		model = svm_train(problem,param)	
#
#		svm_save_model('Final_svm.model',model)

	def Dump_Model(self,path,model):
		with open(path,'wb') as model_outstream:
			cPickle.dump(model,model_outstream)








#new_model = logs.logs_object('TeraSort')

#ratio1 = -200

#MapFeature_list = np.array(new_model.get_MapFeature_list()[:ratio1])
#RedFeature_list =np.array(new_model.get_RedFeature_list()[:ratio1])
#MapMean_list = np.array(new_model.get_MapMean_list()[:ratio1])
#RedMean_list = np.array(new_model.get_RedMean_list()[:ratio1])

#MapDev_list = np.array(new_model.get_MapDev_list()[:ratio1])
#RedDev_list = np.array(new_model.get_RedDev_list()[:ratio1])

#Target_list = np.array(new_model.get_target_list()[:ratio1])

#engine = WhatIf_Engine(MapFeature_list,RedFeature_list,MapMean_list,RedMean_list,MapDev_list,RedDev_list,Target_list)
#engine.Build_MapMean_Model()
#engine.Build_MapDev_Model()
#engine.Build_RedMean_Model()
#engine.Build_RedDev_Model()
#engine.Build_Final_Model()
