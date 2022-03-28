# Authors: Thijs Brekhof, Cain Weideman, Twan Heeres
# The main python file we will use to classift musical genres
import eyed3
import os
import pickle


def main():

    directory = "fma_small/"

    genre_dict = {}

    eyed3.log.setLevel("ERROR")

    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            new_path = os.path.join(root, subdirectory)
            file_list = os.listdir(new_path)
            for i in file_list:
                file_path = new_path + '/' + i
                audio = eyed3.load(file_path)
                if audio.tag.genre:
                    genre_dict[i] = audio.tag.genre.name

    with open('genre_dict.pickle', 'wb') as f:
        pickle.dump(genre_dict, f)


if __name__ == "__main__":
    main()
