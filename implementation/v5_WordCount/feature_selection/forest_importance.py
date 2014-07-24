import numpy as np

import sys
sys.path.append("../2-level/")
import logs

from sklearn.ensemble import ExtraTreesRegressor

new_model = logs.logs_object('TeraSort')

feature_list = np.array(new_model.get_RedFeature_list())
interData_list = np.array(new_model.get_RedMean_list())

# Build a forest and compute the feature importances
forest = ExtraTreesRegressor(n_estimators=100,random_state=0)

forest.fit(feature_list,interData_list)
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
		             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(len(indices)):
	    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

	    # Plot the feature importances of the forest
import pylab as pl
pl.figure()
pl.title("Feature importances")
pl.bar(range(len(indices)), importances[indices],
			           color="r", yerr=std[indices], align="center")
pl.xticks(range(10), indices)
pl.xlim([-1, 10])
pl.show()
