# PILS
MLP project
Usage:
Download FMA dataset from https://github.com/mdeff/fma
Download GTZAN dataset from https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification
and extract both in the folder you want to run the scripts.
Download fma_metadata.zip and extract tracks.csv from this (required to get the genres using fma_get_genres) to the same folder

# Code

The following files have been developed for this project:

fma_main.py - main file to run the classifiers on the FMA dataset
gtzan_main.py - main file to run the classifiers on the GTZAN dataset

fma_get_genres - run this file in the same folder as tracks.csv to get fma_genre_dict.pickle -> the dictionary with tracks as key and the corresponding genre as value
