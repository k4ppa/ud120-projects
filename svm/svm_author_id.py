#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from sklearn.svm import SVC
from tools.email_preprocess import preprocess


def calculate_accuracy(features_train, features_test, labels_train, labels_test, C=1):
    #########################################################
    ### your code goes here ###
    clf = SVC(C=C, kernel='rbf')

    # uncomment to use only the 1% of the data set
    #features_train = features_train[:len(features_train) / 100]
    #labels_train = labels_train[:len(labels_train) / 100]

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"

    t1 = time()
    predicted = clf.predict(features_test)
    print "predicting time:", round(time() - t1, 3), "s"

    accuracy = clf.score(features_test, labels_test)
    print 'Accuracy with C={} is {}'.format(C, accuracy)
    return predicted
    #########################################################


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#calculate_accuracy(features_train, features_test, labels_train, labels_test, C=1)
#calculate_accuracy(features_train, features_test, labels_train, labels_test, C=10)
#calculate_accuracy(features_train, features_test, labels_train, labels_test, C=100)
#calculate_accuracy(features_train, features_test, labels_train, labels_test, C=1000)
predicted = calculate_accuracy(features_train, features_test, labels_train, labels_test, C=10000)

print 'Chris email: {}'.format(list(predicted).count(1))
print 'Sara email: {}'.format(list(predicted).count(0))


