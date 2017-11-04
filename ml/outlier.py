import pickle

import numpy as np
from sklearn import svm
from sklearn.ensemble import IsolationForest


def train_model(datapoints, user_id):
    num_samples = 200
    outliers_frac = .25
    clusters_seperation = [0, 1, 2]

    classifier = IsolationForest(
        max_samples=num_samples,
        contamination=outliers_fraction
    )

    classifier.fit(datapoints)

    pickle.dump(classifier, open("outlier_models/%s_model.sklearn" % (user_id,), "rb"))

def predict(datapoint, user_id):
    classifier = pickle.load(open("outlier_models/%s_model.sklearn" % (user_id,), "r"))
    return classifier.predict(datapoint)
