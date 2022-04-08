# PILS
MLP project

Developed by:

Cain Weideman

Twan Heeres

Thijs Brekhof

# Code

The following files have been developed for this project:

fma_get_genres.py - run this file in the same folder as tracks.csv to get fma_genre_dict.pickle -> the dictionary with tracks as key and the corresponding genre as value.

gtzan_convert.py - run this file to relocate the data from genres to wav-data, a cleaner and more easy to use directory.

fma_convert.py - run this file to relocate the data from fma_small to mp3-data, a cleaner and more easy to use directory.

mp3_to_mfcc.py - run this file to convert the mp3 data in mp3-data to MFCC's, the output is a dictionary saved in a pickle file

wav_to_mfcc.py - run this file to convert the wav data in wav-data to MFCC's, the output is a dictionary saved in a pickle file 

fma_main.py - main file to run the classifiers on the FMA dataset.

gtzan_main.py - main file to run the classifiers on the GTZAN dataset.

# To recreate this experiment

## To create the FMA data and run the classifier
Clone this repository

Download FMA dataset from https://github.com/mdeff/fma and extract in the folder you cloned this repository. 

Download fma_metadata.zip and extract tracks.csv from this (required to get the genres using fma_get_genres) to the same folder.

run fma_convert.py to relocate the data from fma_small to mp3-data, a cleaner and more easy to use directory.

run mp3_to_mfcc.py to convert mp3 data to MFCCs (default: Saved in mfcc_dict.pickle) In case you cannot/don't want to run this file, the output is also available at https://drive.google.com/drive/u/1/folders/1ovOgYFLUD70kid8qOUmLmJ-TCU7U1oxm for people that have a RUG email account. (Not on github as the filesize is too large.) 

run fma_get_genres.py to get the root genre for each of the songs (default: saved in fma_genre_dict.pickle)

run fma_main.py

## To create the GTZAN data and run the classifier
Clone this repository

Download GTZAN dataset from https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification and extract in the folder you cloned this repository. 

run gtzan_convert.py to relocate the data from genres to wav-data, a cleaner and more easy to use directory.

run wav_to_mfcc.py to convert wav data to MFCCs (default: Saved in gtzan_mfcc_dict.pickle)

run gtzan_main.py (default: set to use the MFFC's)
