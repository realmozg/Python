import os
import shutil
import uuid

source_folder = 'C:\\Users\\demom\\Desktop\\Исходные данные\\'
response_folder = 'C:\\Users\\demom\\Desktop\\Ответы\\'
out_folder = 'C:\\Users\\demom\\Desktop\\На отправку\\'



def create_file (folder, prefix, name, gen_id):
    with open(folder + prefix + name + gen_id + '.xml', 'w') as file:
        return file

##
##for i in range(100):
##    gen_id = uuid.uuid4()
##    new_xml = create_file(source_folder, 'Form5_', '0000_202020_', str(gen_id))
##    new_resp_xml = create_file(response_folder, 'response_Form5_', '0000_202020_', str(gen_id))
##    print (new_xml)
##    print (new_resp_xml)

def is_response(source_folder = source_folder, response_folder = response_folder, out_folder = out_folder):
    source_files = os.listdir(source_folder)
    resp_files = os.listdir(response_folder)
    for source_file in source_files:
        for resp_file in resp_files:
            if resp_file == 'response_' + source_file:
                shutil.move(response_folder+resp_file, out_folder+resp_file)
