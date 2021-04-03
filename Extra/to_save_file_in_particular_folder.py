import os
import os.path
model_folder = "model"
try:
    os.makedirs(model_folder)
except FileExistsError:
    print("Directory is already exists !")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

file_save = os.path.join(model_folder,"test.txt")

file1 = open(file_save,"w")
file1.write("File created in specified folder....")
file1.close()