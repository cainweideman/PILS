import os
import pickle


def main():

    directory = "fma_small/"

    infile = open("genre_dict.pickle", 'rb')
    genre_dict = pickle.load(infile)
    infile.close()

    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            new_path = os.path.join(root, subdirectory)
            file_list = os.listdir(new_path)
            for i in file_list:
                if i in genre_dict.keys():
                    file_path = new_path + '/' + i
                    os.replace(file_path, "mp3-data/" + i)


if __name__ == "__main__":
    main()