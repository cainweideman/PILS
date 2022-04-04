import os
import pickle


def main():

    directory = "genres"

    #infile = open("genre_dict.pickle", 'rb')
    #genre_dict = pickle.load(infile)
    #infile.close()

    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            new_path = os.path.join(root, subdirectory)
            file_list = os.listdir(new_path)
            for i in file_list:
                file_path = new_path + '/' + i
                os.replace(file_path, "wav-data/" + i)


if __name__ == "__main__":
    main()