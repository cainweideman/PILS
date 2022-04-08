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
            # Use to make the mean dictionary, comment lines 30,31 and 34 to use
            #mean = np.mean(i)
            #mfcc_list.append(mean)

            # Use to make the sum dictionary, comment lines 26, 27 and 34 to use
            #sum = np.sum(i)
            #mfcc_list.append(sum)

            # Use to make the MFCC dictionary, comment lines 26, 27, 30 and 31 to use
            mfcc_list.append(i)

        mfcc_dict[audio_file] = mfcc_list

    with open('gtzan_mfcc_dict.pickle', 'wb') as f:
        pickle.dump(mfcc_dict, f)


main()