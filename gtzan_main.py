from matplotlib import pyplot as plt
from sklearn.svm import SVC
import pickle
from itertools import repeat
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import collections
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns


def get_data():
    # MFCC dict
    infile = open("sum_gtzan_mfcc_dict.pickle", 'rb')
    mfcc_dict = pickle.load(infile)
    infile.close()
    #for i in mfcc_dict:
        #print(np.array(mfcc_dict[i]).shape)
    #first = list(mfcc_dict.values())[0]
    #print(first)
    mfccs = []
    for i in mfcc_dict:
        mfccs.append(mfcc_dict[i])

    #mfccs = np.array(mfccs)
    #nsamples, nx, ny = mfccs.shape
    #mfccs = mfccs.reshape((nsamples, nx * ny))
    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    label_list = []
    for i in labels:
        label_list.extend(repeat(i, 100))

    counter = collections.Counter(label_list)
    #for k, v in dict(counter).items():
        #print(k, v)
    return label_list, mfccs


def main():
    # Getting our training input/labels
    labels, mfccs = get_data()

    # Splitting the data in train/test (80/20)
    x_train, x_test, y_train, y_test = train_test_split(mfccs, labels, test_size=0.20, random_state=69)

    # Kernel types: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed‘
    svm = SVC(kernel="linear")
    svm.fit(x_train, y_train)
    predictions = svm.predict(x_test)

    #neigh = KNeighborsClassifier(n_neighbors=50)
    #neigh.fit(x_train, y_train)
    #predictions = neigh.predict(x_test)

    print(accuracy_score(y_test, predictions))
    matrix = confusion_matrix(y_test, predictions)
    ax = sns.heatmap(matrix, annot=True, cmap='Blues')

    ax.set_title('GTZAN SVM Linear\n\n')
    ax.set_xlabel('\nPredicted Genre')
    ax.set_ylabel('Actual Genre ')

    ## Ticket labels - List must be in alphabetical order
    ax.xaxis.set_ticklabels(['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock'])
    ax.yaxis.set_ticklabels(['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock'])

    ## Display the visualization of the Confusion Matrix.
    plt.show()
    #print(scores)


main()