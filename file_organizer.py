import os
import shutil
import glob

def organize_files(source_dir):
    files = os.listdir(source_dir)

    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):
            file_extension = os.path.splitext(file)[1][1:]
            destination_dir = os.path.join(source_dir, file_extension)
            os.makedirs(destination_dir, exist_ok=True)

            shutil.move(os.path.join(source_dir, file), os.path.join(destination_dir, file))

if __name__ =="__main__":
    source_directory = input("Enter source directory: ")
    organize_files(source_directory)
    print("Organization complete")