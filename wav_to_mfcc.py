import scipy.io.wavfile as wav
from python_speech_features import mfcc
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
    count = 0
    for audio_file in file_list:
        #print(audio_file)
        file_path = directory + audio_file
        (rate, sig) = wav.read(file_path)
        mfcc_feat = mfcc(sig, rate)
        mfcc_feat = np.transpose(mfcc_feat)
        #signal, sr = librosa.load(file_path)
        #mfcc_feat = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)
        mfcc_list = []
        for i in mfcc_feat:
            mean = np.mean(i)
            mfcc_list.append(mean)
        #print(len(mfcc_list))

        mfcc_dict[audio_file] = mfcc_list
    with open('big_wav_mfcc_dict.pickle', 'wb') as f:
        pickle.dump(mfcc_dict, f)


main()