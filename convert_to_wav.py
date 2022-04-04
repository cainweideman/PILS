import os
from pydub import AudioSegment
import subprocess


def main():

    print(os.environ["PATH"].split(os.pathsep))

    directory = "mp3-data/"

    file_list = os.listdir(directory)
    for i in file_list:
        file_path = directory + i
        dst = "wav-data/{0}.wav".format(i[:-4])
        #audSeg = AudioSegment.from_mp3(file_path)
        #audSeg.export(dst, format="wav")
        #subprocess.call(['ffmpeg', '-i', file_path, dst])


if __name__ == "__main__":
    main()