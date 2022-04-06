import scipy.io.wavfile as wav
from python_speech_features import mfcc
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import librosa

import os
import warnings
import pickle
import numpy as np


def main():

    warnings.filterwarnings('ignore')

    mfcc_dict = {}
    directory = "wav-data/"
    file_list = os.listdir(directory)
    for audio_file in file_list:
        file_path = directory + audio_file

        signal, sr = librosa.load(file_path)
        mfcc_feat = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)

        mfcc_list = []
        for i in mfcc_feat:
            #mean = np.mean(i)
            #mfcc_list.append(mean)
            sum = np.sum(i)
            mfcc_list.append(sum)

        mfcc_dict[audio_file] = mfcc_list

    with open('sum_gtzan_mfcc_dict.pickle', 'wb') as f:
        pickle.dump(mfcc_dict, f)


main()