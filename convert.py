import os
import pickle
from pydub import AudioSegment


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
                    dst = "data/{0}".format(i[:-4])
                    #print(file_path)
                    #print(dst)
                    audSeg = AudioSegment.from_mp3(file_path)
                    audSeg.export(dst, format="wav")

    with open('genre_dict.pickle', 'wb') as f:
        pickle.dump(genre_dict, f)


if __name__ == "__main__":
    main()