import shutil
import os
import datetime
import zipfile
import subprocess
import sys

oper_date = datetime.datetime.now().strftime("%d.%m.%Y %H-%M-%S")
in_folder = "C:\\Users\\demom\\OneDrive\\Рабочий стол\\IN\\"
out_folder = "C:\\Users\\demom\\OneDrive\\Рабочий стол\\OUT\\"
inbound_folder = "\\\\192.168.100.200\\Kontur\\inbound\\"
outbound_folder = "\\\\192.168.100.200\\Kontur\\outbound\\"
dest_folder = "C:\\Users\\demom\\OneDrive\\Рабочий стол\\Архив\\Уведомления от " + str(oper_date) + "\\"
source_folder = dest_folder + "Исходные файлы\\"
log =  dest_folder + str(oper_date) + "_log.txt"


try:
    os.makedirs(dest_folder)
except OSError:
    print("Создать каталог по пути %s невозможно, так как он уже был создан\n" %os.path.dirname(dest_folder))
else:
    print("Рабочий каталог %s создан.\n" %os.path.dirname(dest_folder))

try:
    os.makedirs(source_folder)
except OSError:
    print("Создать каталог по пути %s невозможно, так как он уже был создан\n" %os.path.dirname(source_folder))
else:
    print("Рабочий каталог %s создан\n" %os.path.dirname(source_folder))


# def check_folder (folder):
#     if os.path.exists(folder):
#         print("Каталог %s существует"%folder)
#         return 0
#     else:
#         print("Не могу найти путь до каталога %s. Выполняю попытку подключения."%folder)
# ##        subprocess.call ('cmd /c "net use n: \\192.168.1.1\share /server-name/administrator password"') # реализовать подключение по net use
#         return 1



#тестирование аварийного завершения.
# check = check_folder (r'D:\torrent')


# if check == 0:
#     print ("Каталог существует")
# else:
#     print ("Такого каталога нет, завершаю работу")
#     sys.exit()

print('Перемещаю файлы: \n')



# Form5_count = 0
# MigCs_count = 0
# MedCs_count = 0
# UnregCs_count = 0
# MedUnregCs_count = 0

# os.chdir(in_folder)
# file_list = os.listdir(in_folder)


# for filename in file_list:

#     if not filename.endswith('.xml'):
#         continue
    
#     elif filename.startswith('Form5'):
#         print('Перемещаю %s в %s'%(filename,source_folder))
#         shutil.copy2(in_folder + filename, source_folder + filename)
#         Form5_count += 1
    
#     elif filename.startswith('MigCs'):
#         print('Перемещаю %s в %s'%(filename,source_folder))
#         shutil.copy2(in_folder + filename, source_folder + filename)
#         MigCs_count += 1 
    
#     elif filename.startswith('MedCs'):
#         print('Перемещаю %s в %s'%(filename,source_folder))
#         shutil.copy2(in_folder + filename, source_folder + filename)
#         MedCs_count += 1
    
#     elif filename.startswith('UnregCs'):
#         print('Перемещаю %s в %s'%(filename,source_folder))
#         shutil.copy2(in_folder + filename, source_folder + filename)
#         UnregCs_count += 1
    
#     elif filename.startswith('MedUnregCs'):
#         print('Перемещаю %s в %s'%(filename,source_folder))
#         shutil.copy2(in_folder + filename, source_folder + filename)
#         MedUnregCs_count += 1
# else:
#         print ('Файлов больше нет. Создаю архивы\n')


os.chdir(in_folder)
file_list = os.listdir(in_folder)

hotel_count = 0
med_count = 0


for filename in file_list:

    if not filename.endswith('.xml'):
        continue
    
    elif filename.startswith('Form5') or filename.startswith('MigCs') or filename.startswith('UnregCs'):
        print('Перемещаю %s в %s'%(filename, source_folder))
        shutil.copy2(in_folder + filename, source_folder + filename)
        hotel_count += 1
    
    elif filename.startswith('MedCs') or filename.startswith('MedUnregCs'):
        print('Перемещаю %s в %s'%(filename,source_folder))
        shutil.copy2(in_folder + filename, source_folder + filename)
        med_count += 1 
    else:
        print ("Файлов в каталоге нет.")
else:
        print ('Файлов больше нет. Создаю архивы\n')

os.chdir(dest_folder)

file_log = open(log, "w")
file_log.write('Список файлов: \n\n')
file_log.write('Общее количество Form5, MigCs, UnregCs: %s\n'%hotel_count)
file_log.write('Общее количество MedCs, MedUnregCs: %s\n'%med_count)


def create_zip(archive_number, xml_type, dest_folder = dest_folder, oper_date = oper_date):
    try:
        new_zip = zipfile.ZipFile(dest_folder + str(archive_number) + '. ' + xml_type + '_Kontur_' + str(oper_date) + '.zip', 'w') 
        archive_number += 1
    except:
        print('Ошибка, архив %s не создан'%xml_type)
    else:
        print('Архив %s на диске создан.'%new_zip)
        return archive_number, new_zip


os.chdir(source_folder)
archive_number = 1

if hotel_count > 0:
    archive_number, ziphotel = create_zip(archive_number, 'Hotel')
else:
    print ('Файлов Form5, MigCs, UnregCs нет на диске, архив не будет создан')

if med_count > 0:
    archive_number, zipmed = create_zip(archive_number, 'Med')
else:
    print ('Файлов MedCs, MedUnregCs нет на диске, архив не будет создан')


# if Form5_count > 0:
#     archive_number, zipform5 = create_zip(archive_number, 'Form5')
# else:
#     print ('Файлов Form5 нет на диске, архив не будет создан')

# if MigCs_count > 0:
#     archive_number, zipmigcs = create_zip(archive_number, 'MigCs')
# else:
#     print ('Файлов MigCs нет на диске, архив не будет создан')

# if MedCs_count > 0:
#     archive_number, zipmedcs = create_zip(archive_number, 'MedCs')
# else:
#     print ('Файлов MedCs нет на диске, архив не будет создан')

# if UnregCs_count > 0: 
#     archive_number, zipunregcs = create_zip(archive_number, 'UnregCs')
# else:
#     print ('Файлов UnregCs нет на диске, архив не будет создан')

# if MedUnregCs_count > 0:
#     archive_number, zipmedunregcs = create_zip(archive_number, 'MedUnregCs')
# else:
#     print ('Файлов MedUnregCs нет на диске, архив не будет создан')

# total_size = 41943040
# Form5_size = 0
# MigCs_size = 0
# MedCs_size = 0
# UnregCs_size = 0
# MedUnregCs_size = 0

# archive_file_list = sorted(os.listdir(source_folder))

# for newfile in archive_file_list:
#     if newfile.startswith('Form5'):
#         Form5_size += os.path.getsize(newfile)
#         if Form5_size <= total_size:
#             print('Записываю %s, размер файлов: %s'%(newfile, Form5_size))
#             zipform5.write(newfile)
#         else:
#             zipform5.close()
#             Form5_size = 0 
#             Form5_size += os.path.getsize(newfile)
#             archive_number, zipform5 = create_zip(archive_number, 'Form5')
#             print('Записываю %s, размер файлов: %s'%(newfile, Form5_size))
#             zipform5.write(newfile)

#     elif newfile.startswith('MigCs'):
#         MigCs_size += os.path.getsize(newfile)
#         if MigCs_size <= total_size:
#             print('Записываю %s, размер файлов: %s'%(newfile, MigCs_size))
#             zipmigcs.write(newfile)
#         else:
#             zipmigcs.close()
#             MigCs_size = 0 + os.path.getsize(newfile)
#             archive_number, zipmigcs = create_zip(archive_number, 'MigCs')
#             print('Записываю %s, размер файлов: %s'%(newfile, MigCs_size))
#             zipmigcs.write(newfile) #complete 

#     elif newfile.startswith('UnregCs'):
#         UnregCs_size += os.path.getsize(newfile)
#         if UnregCs_size <= total_size:
#             print('Записываю %s, размер файлов: %s'%(newfile, UnregCs_size))
#             zipunregcs.write(newfile)
#         else:
#             zipunregcs.close()
#             UnregCs_size = 0 + os.path.getsize(newfile)
#             archive_number, zipunregcs = create_zip(archive_number, 'UnregCs')
#             print('Записываю %s, размер файлов: %s'%(newfile, UnregCs_size))
#             zipunregcs.write(newfile)

#     elif newfile.startswith('MedCs'):
#         MedCs_size += os.path.getsize(newfile)
#         if MedCs_size <= total_size:
#             print('Записываю %s, размер файлов: %s'%(newfile, MedCs_size))
#             zipmedcs.write(newfile)
#         else:
#             zipmedcs.close()
#             MedCs_size = 0 + os.path.getsize(newfile)
#             archive_number, zipmedcs = create_zip(archive_number, 'MedCs')
#             print('Записываю %s, размер файлов: %s'%(newfile, MedCs_size))
#             zipmedcs.write(newfile) #complete

#     elif newfile.startswith('MedUnregCs'):
#         MedUnregCs_size += os.path.getsize(newfile)
#         if MedUnregCs_size <= total_size:
#             print('Записываю %s, размер файлов: %s'%(newfile, MedUnregCs_size))
#             zipmmedunregcs.write(newfile)
#         else:
#             zipmmedunregcs.close()
#             MedUnregCs_size = 0 + os.path.getsize(newfile)
#             archive_number, zipmmedunregcs = create_zip(archive_number, 'MedUnregCs')
#             print('Записываю %s, размер файлов: %s'%(newfile, MedUnregCs))
#             zipmmedunregcs.write(newfile)

total_size = 41943040
hotel_size = 0
med_size = 0
archive_file_list = os.listdir(source_folder)

for newfile in archive_file_list:
    if newfile.startswith('Form5') or newfile.startswith('MigCs') or newfile.startswith('UnregCs'):
        hotel_size += os.path.getsize(newfile)
        if os.path.getsize(newfile) > total_size:
            print("Файл превышает допустимый размер контейнера в %s, пропускаю запись файла %s\n"%((total_size//1024//1024), newfile))
            hotel_size = 0
            continue
        elif  hotel_size <= total_size:
            print('Записываю %s в архив'%newfile)
            ziphotel.write(newfile)
        else:
            ziphotel.close()
            hotel_size = 0 
            hotel_size += os.path.getsize(newfile)
            archive_number, ziphotel = create_zip(archive_number, 'Hotel')
            print('Записываю %s в архив'%newfile)
            ziphotel.write(newfile)

    elif newfile.startswith('MedCs') or newfile.startswith('MedUnregCs'):
        med_size += os.path.getsize(newfile)
        if os.path.getsize(newfile) > total_size:
            print("Общий размер файлов был задан не верно, пропускаю запись файла %s\n"%newfile)
            med_size = 0
            continue
        elif med_size <= total_size:
            print('Записываю %s в архив'%newfile)
            zipmed.write(newfile)
        else:
            zipmed.close()
            med_size = 0 
            med_size += os.path.getsize(newfile)
            archive_number, zipmed = create_zip(archive_number, 'Med')
            print('Записываю %s в архив'%newfile)
            zipmed.write(newfile)

try:
    ziphotel.close()
except:
    print ('Невозможно закрыть zip архив Hotels, так как он не был создан.\n')
else:
    print('Последний архив Hotels успешно закрыт')

try:
    zipmed.close()
except:
    print ('Невозможно закрыть zip архив Med, так как он не был создан.\n')
else:
    print('Последний архив Med успешно закрыт')

os.chdir(dest_folder)
list_zip = os.listdir(dest_folder)
print ("Список архивов: \n")
for zip_name in list_zip:
    if zip_name.endswith('.zip'):
        try: 
            info_zip = zipfile.ZipFile(zip_name)
            check_zip = zipfile.ZipFile.testzip(info_zip)
            # zipfile.ZipFile.testzip(zips)
        except ValueError: 
            print("Архив %s битый, копирование будет прекращено"%zip_name)
        else:
            size_zip = os.path.getsize(zip_name)/1024
            file_log.write("Копирую архив %s размером %s КБ в директорию %s\n"%(zip_name, size_zip, inbound_folder))
            print("Копирую архив %s размером %s КБ в директорию %s\n"%(zip_name, size_zip, inbound_folder))
            shutil.copy2(dest_folder + zip_name, inbound_folder + filename)
 
file_log.close()
