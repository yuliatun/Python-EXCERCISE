# AUTOMATE FILE IN FILE EXPLORER

import os, shutil
path = "C:/Users/yuliatun/Documents/DATA ANALIS/Python/folder/"
file_name = os.listdir(path)

folder_name = ['csv files', 'image files', 'text files']

for loop in range(0,3):

    if not os.path.exists(path + folder_name[loop]):
        print(path + folder_name[loop])
    os.makedirs((path + folder_name[loop]))


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg"  in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".png"  in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        print("There are file in this path were not moved")