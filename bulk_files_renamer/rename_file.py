import os

folder_path = input('Enter the path: ')
#/Users/rockesh/Documents/songs
file_list = os.listdir(folder_path)
folder_exist = os.path.exists(folder_path)

def trim_at_start_and_save(folderPath,fileName,numOfChars):
    if not fileName.startswith('.') and os.path.isfile(os.path.join(folderPath, fileName)):
        new_name = fileName[numOfChars:]
        new_name_path = folderPath + '/' + new_name.strip()
        old_name_path = folderPath + '/' + fileName
        os.rename(old_name_path, new_name_path)
        #print(old_name_path)
        #print(new_name_path)


if ((len(file_list) > 0) and (folder_exist)):
    option = input('[1] Trim from start\n[2] Trim at end\n[3] Append at start\n[4] Append at end\n\nEnter your selection: ')
    if option == '1':
        numberOfCharacters = input('How many characters you want to be removed from start: ')
        numberOfCharacters = int(numberOfCharacters)
        # print(file_list)
        # print('----------\n----------\n----------')
        for file in file_list:
            #print(file)
            # print(type(file))
            # print(numberOfCharacters)
            # print(type(numberOfCharacters))
            trim_at_start_and_save(folder_path,file,numberOfCharacters)
    else:
        print('Work in progress... Wait for the next release')