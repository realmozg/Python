import os
import time
from datetime import datetime

all_files = os.walk('C:\\Users\\demom\\Desktop\\hotels\\')
source_list = os.listdir('C:\\Users\\demom\\Desktop\\Исходные данные\\')

##def check_new_resp (source_list = source_list, resp_folder = all_files):
def check_new_resp (resp_folder = all_files):
    response = []
    for folder, subfolder, file in all_files:
        modifydate = datetime.fromtimestamp(os.path.getmtime(folder)).strftime('%Y-%m-%d')
        if modifydate == datetime.now().strftime('%Y-%m-%d'):
            print (folder)
            print (datetime.fromtimestamp(os.path.getmtime(folder)).strftime('%Y-%m-%d %H-%M-%S'))
            print (datetime.fromtimestamp(os.path.getmtime(folder)).strftime('%Y-%m-%d'))
            for resp_file in file:
                path_file = str(folder)+'\\'+resp_file
    ##            print(path_file)
    ##            print(resp_file)
                response.append(path_file)
        else:
            continue
    return response
reponse_files = check_new_resp()
print(reponse_files)

