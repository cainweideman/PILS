from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import pickle
from sklearn.model_selection import train_test_split
import collections
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import (NeighborhoodComponentsAnalysis, KNeighborsClassifier)
from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.pipeline import Pipeline
import random
import sys


def get_data():
    # MFCC dict
    infile = open("mfcc_dict.pickle", 'rb')
    mfcc_dict = pickle.load(infile)
    infile.close()
    mfcc_dict = collections.OrderedDict(sorted(mfcc_dict.items()))
    mfccs = []
    issue_tracks = ["098565.mp3", "098567.mp3", "098569.mp3"]
    for track in issue_tracks:
        mfcc_dict.pop(track)
    # adding mfccs to list so the classifier can use them as input data
    for i in mfcc_dict:
        mfccs.append(mfcc_dict[i])

    # Padding with zeroes
    padded_mfcc = []
    for i in mfccs:
        if i.shape[1] == 1292:
            i = np.pad(i, [(0, 0), (0, 1)], mode="constant")
        elif i.shape[1] == 1291:
            i = np.pad(i, [(0, 0), (0, 2)], mode="constant")
        padded_mfcc.append(i)
    # Reshaping mfccs to format that the SVM classifier can recognise
    mfccs = np.array(padded_mfcc)

    nsamples, nx, ny = mfccs.shape
    mfccs = mfccs.reshape((nsamples, nx * ny))

    # Genre dict
    infile = open("genre_dict.pickle", 'rb')
    genre_dict = pickle.load(infile)
    infile.close()
    # Removing keys from genre dict that aren't in mfcc dict (useless keys)
    remove_l = []
    for i in genre_dict:
        if "{0}.mp3".format(i) not in mfcc_dict:
            remove_l.append(i)
    for i in remove_l:
        genre_dict.pop(i)
    # Rewriting the genres to numbers (0-7) so the classifier can read them
    label_l = ["Hip-Hop", "Pop", "Folk", "International", "Instrumental", "Experimental", "Rock", "Electronic"]
    labels = []
    for i in genre_dict:
        labels.append(label_l.index(genre_dict[i]))

    # The next part is to see the distribution of genres.
    # g_dict = {}
    # for i in genre_dict.values():
    #
    #     if i not in g_dict:
    #         g_dict[i] = 1
    #     else:
    #         g_dict[i] += 1
    #
    # print(dict(sorted(g_dict.items(), key=lambda x: x[1], reverse=True)))

    return labels, mfccs


def main():
    # Getting our training input/labels
    labels, mfccs = get_data()

    # Splitting the data in train/test (80/20)
    x_train, x_test, y_train, y_test = train_test_split(mfccs, labels, test_size=0.20, random_state=69)

    # Kernel types: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed
    #svclassifier = SVC(kernel="poly")
    svm = OneVsRestClassifier(SVC(kernel='poly'), n_jobs=-1)
    clf = svm.fit(x_train, y_train)
    scores = cross_val_score(clf, x_test, y_test, cv=5)
    print(scores)
    #svclassifier.fit(x_train, y_train)

    #predictions = svclassifier.predict(x_test)


    # Gaussian Naive Bayes
    #gnb = GaussianNB()
    #gnb.fit(x_train, y_train)
    #predictions = gnb.predict(x_test)

    # KNN
    #nca = NeighborhoodComponentsAnalysis(random_state=42)
    #knn = KNeighborsClassifier(n_neighbors=1000, n_jobs=-1)
    #nca_pipe = Pipeline([('nca', nca), ('knn', knn)])
    #nca_pipe.fit(x_train, y_train)
    #knn.fit(x_train, y_train)
    #predictions = knn.predict(x_test)
    #print(nca_pipe.score(x_test, y_test))

    #print(accuracy_score(y_test, predictions))


main()
