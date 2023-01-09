import os
import re

def trim_at_start_and_save(folderPath,fileName,numOfChars):
    if not fileName.startswith('.') and os.path.isfile(os.path.join(folderPath, fileName)):
        new_name = fileName[numOfChars:]
        new_name_path = folderPath + '/' + new_name.strip()
        old_name_path = folderPath + '/' + fileName
        os.rename(old_name_path, new_name_path)

def trim_at_end_and_save(folderPath,fileName,numOfChars):
    if not fileName.startswith('.') and os.path.isfile(os.path.join(folderPath, fileName)):
        cur_name = re.search('(.*)\..*',fileName)
        cur_name = cur_name.group(1)
        extension = re.search('.*\.(.*)',fileName)
        extension = extension.group(1)
        new_name = cur_name[:-numOfChars] + '.' + extension
        new_name_path = folderPath + '/' + new_name.strip()
        old_name_path = folderPath + '/' + fileName
        os.rename(old_name_path, new_name_path)

def append_at_start_with_serialization(folderPath,fileName,serial,str_to_be_appended):
    if not fileName.startswith('.') and os.path.isfile(os.path.join(folderPath, fileName)):
        new_name = str_to_be_appended + str(serial) + '_' + fileName
        new_name_path = folderPath + '/' + new_name.strip()
        old_name_path = folderPath + '/' + fileName
        os.rename(old_name_path, new_name_path)

def append_at_start_without_serialization(folderPath,fileName,str_to_be_appended):
    if not fileName.startswith('.') and os.path.isfile(os.path.join(folderPath, fileName)):
        new_name = str_to_be_appended + '_' + fileName
        new_name_path = folderPath + '/' + new_name.strip()
        old_name_path = folderPath + '/' + fileName
        os.rename(old_name_path, new_name_path)

def append_in_the_end_with_serialization(folderPath,fileName,serial,str_to_be_appended):
    if not fileName.startswith('.') and os.path.isfile(os.path.join(folderPath, fileName)):
        cur_name = re.search('(.*)\..*',fileName)
        cur_name = cur_name.group(1)
        extension = re.search('.*\.(.*)',fileName)
        extension = extension.group(1)
        new_name = cur_name + '_' + str_to_be_appended + str(serial) + '.' + extension
        new_name_path = folderPath + '/' + new_name.strip()
        old_name_path = folderPath + '/' + fileName
        os.rename(old_name_path, new_name_path)

def append_in_the_end_without_serialization(folderPath,fileName,str_to_be_appended):
    if not fileName.startswith('.') and os.path.isfile(os.path.join(folderPath, fileName)):
        cur_name = re.search('(.*)\..*',fileName)
        cur_name = cur_name.group(1)
        extension = re.search('.*\.(.*)',fileName)
        extension = extension.group(1)
        new_name = cur_name + '_' + str_to_be_appended + '.' + extension
        new_name_path = folderPath + '/' + new_name.strip()
        old_name_path = folderPath + '/' + fileName
        os.rename(old_name_path, new_name_path)

rename = True
while rename == True:

    option = input('[1] Trim from start\n[2] Trim at end\n[3] Append at start\n[4] Append at end\n[5] Exit\n\nEnter your selection: ')
    if option in ['1','2','3','4']:
        folder_path = input('Enter the path: ')
        file_list = os.listdir(folder_path)
        folder_exist = os.path.exists(folder_path)
        if ((len(file_list) > 0) and (folder_exist)):
            if option == '1':
                numberOfCharacters = input('How many characters you want to be removed from start: ')
                numberOfCharacters = int(numberOfCharacters)
                for file in file_list:
                    trim_at_start_and_save(folder_path,file,numberOfCharacters)
            rename = True

            if option == '2':
                numberOfCharacters = input('How many characters you want to be removed at end: ')
                numberOfCharacters = int(numberOfCharacters)
                for file in file_list:
                    trim_at_end_and_save(folder_path,file,numberOfCharacters)
                rename = True

            if option == '3':
                append_at_start = True
                while append_at_start == True:
                    append_at_start_option = input('[1] Append string with serialization (ex. str1*,str2*,str3*...)\n[2] Append string without serialization (ex. str*,str*,str*...)\n\nEnter your selection: ')
                    if append_at_start_option == '1':
                        str_to_be_appended = input('Enter the string you want to get appended: ')
                        serial = 1
                        for file in file_list:
                            append_at_start_with_serialization(folder_path,file,serial,str_to_be_appended)
                            serial = serial + 1
                        append_at_start = False
                    elif append_at_start_option == '2':
                        str_to_be_appended = input('Enter the string you want to get appended: ')
                        for file in file_list:
                            append_at_start_without_serialization(folder_path,file,str_to_be_appended)
                        append_at_start = False
                    else:
                        print ('Kindly select right option: ')
                        append_at_start = True
                rename = True

            if option == '4':
                append_in_the_end = True
                while append_in_the_end == True:
                    append_in_the_end_option = input('[1] Append string with serialization (ex. *str1,*str2,*str3...)\n[2] Append string without serialization (ex. *str,*str,*str...)\n\nEnter your selection: ')
                    if append_in_the_end_option == '1':
                        str_to_be_appended = input('Enter the string you want to get appended: ')
                        serial = 1
                        for file in file_list:
                            append_in_the_end_with_serialization(folder_path,file,serial,str_to_be_appended)
                            serial = serial + 1
                        append_in_the_end = False
                    elif append_in_the_end_option == '2':
                        str_to_be_appended = input('Enter the string you want to get appended: ')
                        for file in file_list:
                            append_in_the_end_without_serialization(folder_path,file,str_to_be_appended)
                        append_in_the_end = False
                    else:
                        print ('Kindly select right option: ')
                        append_in_the_end = True
                rename = True

    elif option == '5':
        rename = False

    else:
        print('Kindly select correct option')
        rename = True