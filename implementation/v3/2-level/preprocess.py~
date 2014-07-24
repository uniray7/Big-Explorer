import logs
import numpy as np
from sklearn import preprocessing

raw_logs_object = logs.logs_object('TeraSort')

feature_list = raw_logs_object.get_RedFeature_list()


def PreProcess(feature_list):
	return preprocessing.scale(feature_list)


