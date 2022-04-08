import os


def main():
    directory = "fma_small"

    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            new_path = os.path.join(root, subdirectory)
            file_list = os.listdir(new_path)
            for i in file_list:
                file_path = new_path + '/' + i

                # In order for this to work, create an empty directory in the same folder named "mp3-data"
                os.replace(file_path, "mp3-data/" + i)


if __name__ == "__main__":
    main()
