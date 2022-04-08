from sklearn.svm import SVC
import pickle
from sklearn.model_selection import train_test_split
import collections
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def get_data():
    # MFCC dict
    infile = open("mfcc_dict.pickle", 'rb')
    mfcc_dict = pickle.load(infile)
    infile.close()
    mfcc_dict = collections.OrderedDict(sorted(mfcc_dict.items()))
    mfccs = []
    issue_tracks = ["098565.mp3", "098567.mp3", "098569.mp3", "099134.mp3", "108925.mp3", "133297.mp3"]
    for track in issue_tracks:
        try:
            mfcc_dict.pop(track)
        except KeyError:
            pass
    # adding mfccs to list so the classifier can use them as input data
    for i in mfcc_dict:
        mfccs.append(mfcc_dict[i])

    # Padding with zeroes and summing/getting mean when wanted
    padded_mfcc = []
    temp_l = []
    for i in mfccs:
        # If padding is required (when using the MFCC's themselves as input, uncomment the following if/elif clause
        # if i.shape[1] == 1292:
        #     i = np.pad(i, [(0, 0), (0, 1)], mode="constant")
        # elif i.shape[1] == 1291:
        #     i = np.pad(i, [(0, 0), (0, 2)], mode="constant")

        for ii in i:
            # For regular MFCC's uncomment next line and comment other ones
            # temp_l.append(ii)

            # For mean of MFCC's
            # temp_l.append(np.mean(ii))

            # For sum of MFCC's
            temp_l.append(np.sum(ii))
            if len(temp_l) == 13:
                padded_mfcc.append(temp_l)
                temp_l = []

    mfccs = padded_mfcc
    # Reshaping mfccs to format that the SVM classifier can recognise -
    # only necessary when using regular MFCC's, not for mean/sum
    # nsamples, nx, ny = mfccs.shape
    # mfccs = mfccs.reshape((nsamples, nx * ny))

    # Genre dict
    infile = open("fma_genre_dict.pickle", 'rb')
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

    # SVM
    # Kernel types: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed
    svm = SVC(kernel="linear")
    svm.fit(x_train, y_train)
    predictions = svm.predict(x_test)

    # KNN
    # neigh = KNeighborsClassifier(n_neighbors=10)
    # neigh.fit(x_train, y_train)
    # predictions = neigh.predict(x_test)

    # Printing accuracy
    print(accuracy_score(y_test, predictions))


main()
