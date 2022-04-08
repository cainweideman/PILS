import os


def main():
    directory = "genres"

    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            new_path = os.path.join(root, subdirectory)
            file_list = os.listdir(new_path)
            for i in file_list:
                file_path = new_path + '/' + i

                # In order for this to work, create an empty directory in the same folder named "wav-data"
                os.replace(file_path, "wav-data/" + i)


if __name__ == "__main__":
    main()