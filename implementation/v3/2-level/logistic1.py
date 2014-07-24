import logs
import preprocess


new_model = logs.logs_object('TeraSort')

feature_list = new_model.get_RedFeature_list()
interData_list = new_model.get_RedMean_list()
target_list = new_model.get_target_list()


feature_list_train = feature_list[:-50] 
feature_list_test = feature_list[-50:]
target_list_train = target_list[:-50]
target_list_test = target_list[-50:]
interData_list_train = interData_list[:-50]
interData_list_test = interData_list[-50:]


from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(feature_list_train, interData_list_train)


error_rate = new_model.get_error_rate(interData_list_test,LR.predict(feature_list_test))
print error_rate
print LR.predict(feature_list_test)
print interData_list_test
#print "error_rate:"+str(error_rate)

