

import os
from settings import *

def folderCreate():
    support_folder_list = [dataSource]
    for folderpath in support_folder_list:
        if os.path.exists(folderpath) != True:
            print("file path did not found")
            os.mkdir(folderpath)