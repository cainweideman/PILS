from sklearn.svm import SVC
import pickle
from itertools import repeat
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier


def get_data():
    # MFCC dict
    infile = open("big_wav_mfcc_dict.pickle", 'rb')
    mfcc_dict = pickle.load(infile)
    infile.close()
    mfccs = []
    for i in mfcc_dict:
        mfccs.append(mfcc_dict[i])

    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    label_list = []
    for i in labels:
        label_list.extend(repeat(i, 100))

    return label_list, mfccs

def main():
    # Getting our training input/labels
    labels, mfccs = get_data()

    # Splitting the data in train/test (80/20)
    x_train, x_test, y_train, y_test = train_test_split(mfccs, labels, test_size=0.20, random_state=69)

    # Kernel types: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed
    #svm = SVC(kernel="poly")
    #svm.fit(x_train, y_train)
    #scores = cross_val_score(svm, x_test, y_test, cv=5)
    #predictions = svm.predict(x_test)

    neigh = KNeighborsClassifier(n_neighbors=10)
    neigh.fit(x_train, y_train)
    predictions = neigh.predict(x_test)
    print(accuracy_score(y_test, predictions))
    #print(scores)


main()