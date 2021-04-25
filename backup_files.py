import os
import shutil

print(os.path.exists(r"C:\Users\User\Desktop\ThisPathDoesNotExistWOW"))
print(os.path.exists(r"C:\Users\User\Desktop\PythonProjects"))

path = input("Path for Directory: ")
list_of_files = os.listdir(path)

for files in list_of_files:
    name, ext = os.path.splitext(files)
    ext = ext[1:]

    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + files, path + "/" + ext + "/" + files)
    else:
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + files, path + "/" + ext + "/" + files)

print(os.getcwd())
