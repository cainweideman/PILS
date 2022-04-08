import librosa
import librosa.display
import os
import warnings
import pickle


def main():
    warnings.filterwarnings('ignore')

    mfcc_dict = {}
    # In order to make this script work, you will have to create an empty directory named "mp3-data"
    directory = "mp3-data/"
    file_list = os.listdir(directory)
    # Creating a count to see how fast the conversion is going
    count = 0
    for audio_file in file_list:
        print(audio_file)
        file_path = directory + audio_file
        signal, sr = librosa.load(file_path)
        mfcc = librosa.feature.mfcc(signal, n_mfcc=13, sr=sr)
        mfcc_dict[audio_file] = mfcc
        count += 1
        print(count)

    # Writing the resulting dict to a pickle file
    with open('mfcc_dict.pickle', 'wb') as f:
        pickle.dump(mfcc_dict, f)


main()
