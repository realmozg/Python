import shutil, os, datetime, zipfile

oper_date = datetime.datetime.now().strftime("%d.%m.%Y %H-%M-%S")
in_folder = 'C:\\Users\\demom\\OneDrive\\Рабочий стол\\IN\\'
out_folder = 'C:\\Users\\demom\\OneDrive\\Рабочий стол\\OUT\\'
dest_folder = 'C:\\Users\\demom\\OneDrive\\Рабочий стол\\Архив\\Уведомления от ' + str(oper_date) +'\\'
source_folder = dest_folder + 'Исходные файлы\\'
log =  dest_folder + str(oper_date)+'_log.txt'



#Создаём каталоги для обработки уведомлений

try:
    os.makedirs(dest_folder)
except OSError:
    print("Создать каталог по пути %s невозможно, так как он уже был создан" %dest_folder)
else:
    print("Рабочий каталог %s создан." %dest_folder)

try:
    os.makedirs(source_folder)
except OSError:
    print("Создать каталог по пути %s невозможно, так как он уже был создан" %source_folder)
else:
    print("Рабочий каталог %s создан" %source_folder)

# создаём лог файл

os.chdir(dest_folder)

file_log = open(log, "w")
file_log.write('Список файлов: \n\n')

Form5_count = 0
MigCs_count = 0
MedCs_count = 0
UnregCs_count = 0
MedUnregCs_count = 0

file_list = sorted(os.listdir(in_folder))

for filename in file_list:

    if not filename.endswith('.xml'):
        continue
    
    elif filename.startswith('Form5'):
        print('Перемещаю %s в %s'%(filename,source_folder))
        shutil.copy2(in_folder + filename, source_folder + filename)
        Form5_count += 1
    
    elif filename.startswith('MigCs'):
        print('Перемещаю %s в %s'%(filename,source_folder))
        shutil.copy2(in_folder + filename, source_folder + filename)
        MigCs_count += 1 
    
    elif filename.startswith('MedCs'):
        print('Перемещаю %s в %s'%(filename,source_folder))
        shutil.copy2(in_folder + filename, source_folder + filename)
        MedCs_count += 1
    
    elif filename.startswith('UnregCs'):
        print('Перемещаю %s в %s'%(filename,source_folder))
        shutil.copy2(in_folder + filename, source_folder + filename)
        UnregCs_count += 1
    
    elif filename.startswith('MedUnregCs'):
        print('Перемещаю %s в %s'%(filename,source_folder))
        shutil.copy2(in_folder + filename, source_folder + filename)
        MedUnregCs_count += 1
else:
        print ('Файлов больше нет. Создаю архивы')
        
file_log.write('Кол-во Form5: %s\n'%Form5_count)
file_log.write('Кол-во MigCs: %s\n'%MigCs_count)
file_log.write('Кол-во MedCs: %s\n'%MedCs_count)
file_log.write('Кол-во UnregCs: %s\n'%UnregCs_count)
file_log.write('Кол-во MedUnregCs: %s\n'%MedUnregCs_count)


os.chdir(source_folder)

archive_number = 1

def create_zip(archive_number, xml_type, dest_folder = dest_folder, oper_date = oper_date):
    try:
        new_zip = zipfile.ZipFile(dest_folder + str(archive_number) + '. ' + xml_type + '_Kontur_' + str(oper_date) + '.zip', 'w') #создаем архив
        print('Архив %s на диске создан.'%new_zip)
        archive_number += 1
    except:
        print('Ошибка, архив %s не создан'%xml_type)
    return archive_number, new_zip


if Form5_count > 0:
    archive_number, zipform5 = create_zip(archive_number, 'Form5')
else:
    print ('Файлов Form5 нет на диске, архив не будет создан')

if MigCs_count > 0:
    archive_number, zipmigcs = create_zip(archive_number, 'MigCs')
else:
    print ('Файлов MigCs нет на диске, архив не будет создан')

if MedCs_count > 0:
    archive_number, zipmedcs = create_zip(archive_number, 'MedCs')
else:
    print ('Файлов MedCs нет на диске, архив не будет создан')

if UnregCs_count > 0: 
    archive_number, zipunregcs = create_zip(archive_number, 'UnregCs')
else:
    print ('Файлов UnregCs нет на диске, архив не будет создан')

if MedUnregCs_count > 0:
    archive_number, zipmedunregcs = create_zip(archive_number, 'MedUnregCs')
else:
    print ('Файлов MedUnregCs нет на диске, архив не будет создан')

total_size = 41943040
Form5_size = 0
MigCs_size = 0
MedCs_size = 0
UnregCs_size = 0
MedUnregCs_size = 0

archive_file_list = sorted(os.listdir(source_folder))

for newfile in archive_file_list:
    if newfile.startswith('Form5'):
        Form5_size += os.path.getsize(newfile)
        if Form5_size <= total_size:
            print('Записываю %s, размер файлов: %s'%(newfile, Form5_size))
            zipform5.write(newfile)
        else:
            zipform5.close()
            Form5_size = 0 + os.path.getsize(newfile)
            archive_number, zipform5 = create_zip(archive_number, 'Form5')
            print('Записываю %s, размер файлов: %s'%(newfile, Form5_size))
            zipform5.write(newfile)
    
    elif newfile.startswith('MigCs'):
        MigCs_size += os.path.getsize(newfile)
        if MigCs_size <= total_size:
            print('Записываю %s, размер файлов: %s'%(newfile, MigCs_size))
            zipmigcs.write(newfile)
        else:
            zipmigcs.close()
            MigCs_size = 0 + os.path.getsize(newfile)
            archive_number, zipmigcs = create_zip(archive_number, 'MigCs')
            print('Записываю %s, размер файлов: %s'%(newfile, MigCs_size))
            zipmigcs.write(newfile) #complete 
            
    elif newfile.startswith('MedCs'):
        MedCs_size += os.path.getsize(newfile)
        if MedCs_size <= total_size:
            print('Записываю %s, размер файлов: %s'%(newfile, MedCs_size))
            zipmedcs.write(newfile)
        else:
            zipmedcs.close()
            MedCs_size = 0 + os.path.getsize(newfile)
            archive_number, zipmedcs = create_zip(archive_number, 'MedCs')
            print('Записываю %s, размер файлов: %s'%(newfile, MedCs_size))
            zipmedcs.write(newfile) #complete
            
    elif newfile.startswith('UnregCs'):
        UnregCs_size += os.path.getsize(newfile)
        if UnregCs_size <= total_size:
            print('Записываю %s, размер файлов: %s'%(newfile, UnregCs_size))
            zipunregcs.write(newfile)
        else:
            zipunregcs.close()
            UnregCs_size = 0 + os.path.getsize(newfile)
            archive_number, zipunregcs = create_zip(archive_number, 'UnregCs')
            print('Записываю %s, размер файлов: %s'%(newfile, UnregCs_size))
            zipunregcs.write(newfile) #complete

    elif newfile.startswith('MedUnregCs'):
        MedUnregCs_size += os.path.getsize(newfile)
        if MedUnregCs_size <= total_size:
            print('Записываю %s, размер файлов: %s'%(newfile, MedUnregCs_size))
            zipmmedunregcs.write(newfile)
        else:
            zipmmedunregcs.close()
            MedUnregCs_size = 0 + os.path.getsize(newfile)
            archive_number, zipmmedunregcs = create_zip(archive_number, 'MedUnregCs')
            print('Записываю %s, размер файлов: %s'%(newfile, MedUnregCs))
            zipmmedunregcs.write(newfile)

zipform5.close()
zipmigcs.close()
##zipmedcs.close()
##zipunregcs.close()
##zipmmedunregcs.close()

print('Размер файлов Form5: %s' %Form5_size)
print('Размер файлов MigCs: %s' %MigCs_size)
print('Размер файлов MedCs: %s' %MedCs_size)
print('Размер файлов UnregCs: %s' %UnregCs_size)
print('Размер файлов MedUnregCs: %s' %MedUnregCs_size)
print("Конец. Файлов больше нет")

file_log.close()
