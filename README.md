# PILS
MLP project

# Code

The following files have been developed for this project:

fma_get_genres.py - run this file in the same folder as tracks.csv to get fma_genre_dict.pickle -> the dictionary with tracks as key and the corresponding genre as value.
fma_convert.py - run this file to rewrite the data from fma_small to mp3-data, a cleaner and more easy to use data format.
convert_to_wav.py - ?

mp3_to_mfcc.py - run this file to convert the mp3 data in mp3-data to MFCC's, the output is a dictionary saved in a pickle file "mfcc_dict.pickle".
wav_to_mfcc.py - ?

fma_main.py - main file to run the classifiers on the FMA dataset.
gtzan_main.py - main file to run the classifiers on the GTZAN dataset.

# To recreate this experiment

## To create the FMA data and run the classifier
Clone this repository
Download FMA dataset from https://github.com/mdeff/fma and extract in the folder you cloned this repository. 
Download fma_metadata.zip and extract tracks.csv from this (required to get the genres using fma_get_genres) to the same folder.
run fma_convert.py to rewrite the data from fma_small to mp3-data, a cleaner and more easy to use data format.
run mp3_to_mfcc.py to convert mp3 data to MFCCs (default: saved in mfcc_dict.pickle)
run fma_get_genres.py to get the root genre for each of the songs (default: saved in fma_genre_dict.pickle)
run fma_main.py

## To create the GTZAN data and run the classifier
Clone this repository
Download GTZAN dataset from https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification and extract in the folder you cloned this repository. 
step 2
