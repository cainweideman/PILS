from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from itertools import repeat
import seaborn as sns
import pickle


def get_data():
    # Open the MFCC dict
    infile = open("mean_gtzan_mfcc_dict.pickle", 'rb')
    mfcc_dict = pickle.load(infile)
    infile.close()

    # Add the values of the dictionary to a list
    mfccs = []
    for i in mfcc_dict:
        mfccs.append(mfcc_dict[i])

    # Make the list of labels
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

    # Kernel types: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed‘
    svm = SVC(kernel="poly")
    svm.fit(x_train, y_train)
    predictions = svm.predict(x_test)

    # KNN classifier, uncomment these and comment the svm lines above to use it.
    #neigh = KNeighborsClassifier(n_neighbors=10)
    #neigh.fit(x_train, y_train)
    #predictions = neigh.predict(x_test)

    print(accuracy_score(y_test, predictions))

    # Make and plot a confusion matrix
    matrix = confusion_matrix(y_test, predictions)
    ax = sns.heatmap(matrix, annot=True, cmap='Blues')

    ax.set_title('GTZAN SVM Linear\n\n')
    ax.set_xlabel('\nPredicted Genre')
    ax.set_ylabel('Actual Genre ')

    ax.xaxis.set_ticklabels(['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock'])
    ax.yaxis.set_ticklabels(['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock'])

    plt.show()


main()