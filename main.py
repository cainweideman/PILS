from sklearn.svm import SVC
import pickle
from sklearn.model_selection import train_test_split

def main():
    # Kernel types: ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed
    # svclassifier = SVC(kernel="linear")
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    # svclassifier.fit(x, y)
    infile = open("genre_dict.pickle", 'rb')
    genre_dict = pickle.load(infile)
    infile.close()
    # myset = set()
    g_dict = {}
    for i in genre_dict.values():
        # myset.add(genre_dict[i])
        if i not in g_dict:
            g_dict[i] = 1
        else:
            g_dict[i] += 1
    # print(len(myset))
    # print(myset)

    print(dict(sorted(g_dict.items(), key=lambda x: x[1], reverse=True)))


main()
