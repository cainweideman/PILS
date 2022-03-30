# Authors: Thijs Brekhof, Cain Weideman, Twan Heeres
# In this file we will save all known genres to a pickle (dictionary) file
import pandas as pd
import os
import pickle


def get_our_tracks():
    directory = "fma_small/"

    our_files = []
    for root, subdirectories, files in os.walk(directory):
        # print(files)
        for file in files:
            our_files.append(file[:-4])
    return our_files[2:]


def main():
    # Opening csv file
    df = pd.read_csv("tracks.csv", low_memory=False)
    # Fixing messy data and adding padding
    df = df.rename(columns=df.iloc[0])
    df = df.rename(columns={df.columns[0]: 'track_id'})
    df = df.drop(df.index[0:2])
    df.drop(df.columns.difference(["track_id", "genre_top"]), 1, inplace=True)

    # Padding the track ids
    df['track_id'] = df['track_id'].apply(lambda x: '{0:0>6}'.format(x))
    # Getting all tracks we are using in the fma_small dataset
    tracks = get_our_tracks()

    # Getting genres per track
    genre_dict = {}
    for _, row in df.iterrows():
        if row["track_id"] in tracks:
            genre_dict[row["track_id"]] = row["genre_top"]

    # Writing the dict to a pickle file
    with open('genre_dict.pickle', 'wb') as f:
        pickle.dump(genre_dict, f)


if __name__ == "__main__":
    main()
