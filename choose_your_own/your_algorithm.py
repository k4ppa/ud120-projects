#!/usr/bin/python

import matplotlib.pyplot as plt
from time import time

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()


################################################################################

def create_classifier(classifier, **kwargs):
    classifier = classifier(**kwargs)
    t0 = time()
    classifier.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"
    return classifier


def calculate_accuracy(classifier):
    t0 = time()
    predicted = classifier.predict(features_test)
    print "predicting time:", round(time() - t0, 3), "s"
    accuracy = classifier.score(features_test, labels_test)
    print 'Accuracy: {}'.format(accuracy)
    return accuracy


def show_plot(clf, features_test, labels_test):
    try:
        prettyPicture(clf, features_test, labels_test)
    except NameError:
        pass

### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

clf = create_classifier(KNeighborsClassifier, n_neighbors=22) # best result 0.944
accuracy = calculate_accuracy(clf)
show_plot(clf, features_test, labels_test)

clf = create_classifier(RandomForestClassifier, n_estimators=10, min_samples_split=15, min_samples_leaf=2) # best result 0.936
accuracy = calculate_accuracy(clf)
show_plot(clf, features_test, labels_test)

clf = create_classifier(AdaBoostClassifier, algorithm='SAMME') # best result 0.924
accuracy = calculate_accuracy(clf)
show_plot(clf, features_test, labels_test)


