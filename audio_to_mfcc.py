import librosa
import librosa.display

import os
import warnings
import pickle


def main():
    infile = open("mfcc_dict.pickle", 'rb')
    old_mfcc_dict = pickle.load(infile)
    infile.close()
    warnings.filterwarnings('ignore')

    mfcc_dict = {}
    directory = "mp3-data/"
    file_list = os.listdir(directory)
    count = 0
    for audio_file in file_list:
        if audio_file not in old_mfcc_dict:
            print(audio_file)
            file_path = directory + audio_file
            signal, sr = librosa.load(file_path)
            mfcc = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)

            mfcc_dict[audio_file] = mfcc
            count += 1
            print(count)
    with open('new_mfcc_dict.pickle', 'wb') as f:
        pickle.dump(mfcc_dict, f)


main()
