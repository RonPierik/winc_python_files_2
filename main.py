__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

def clean_cache():
    my_cwd = os.getcwd()
    my_cwd = os.path.join(my_cwd, "files")
    if "data.zip" in os.listdir(my_cwd):
        if "cache" not in os.listdir(my_cwd):
            os.makedirs(os.path.join(my_cwd, "cache"))
            ret_val = True
        else:
            for file in os.scandir(os.path.join(my_cwd, "cache")):
                 os.remove(file.path)
            ret_val = True
    else:
        ret_val = False

    return(ret_val)

def cache_zip(my_zipfile_path, my_cache_path):
    # my_zipfile_path_name = os.path.join(my_zipfile_path , "data.zip")
    with ZipFile(my_zipfile_path, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall(my_cache_path)

def cached_files():
    file_list = []
    cache_path = os.path.join(os.getcwd(), "files")
    cache_path = os.path.join(cache_path, "cache")
    cache_path = os.path.abspath(cache_path)
    for file in os.listdir(cache_path):
        file_path = os.path.join(cache_path, file)
        file_list.append(file_path)
    
    return(file_list)


def find_password(file_list):
    for file in file_list:
        with open(file) as f:
            for line in f:
                if "password: " in line:
                    password = line.replace("password: ", "")
                    password = password.replace("\n", "")
                    break

    return(str(password))

clean_cache()
my_zipfile_path_name = os.path.join(os.getcwd(), "files")
my_cache_path_name = os.path.join(my_zipfile_path_name, "cache")
my_zipfile_path_name = os.path.join(my_zipfile_path_name, "data.zip")
cache_zip(my_zipfile_path_name, my_cache_path_name)
print(find_password(cached_files()))
