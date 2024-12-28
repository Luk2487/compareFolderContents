# main file
# imports
import config
import compare

while True:

    temp = input('config (1)\ncompare (2)\nquit (3)\n>>>')

    if temp == '1':

        temp = input('Folder Handle (1)\nFolder1 (2)\nFolder2 (3)\nBack (4)')

        if temp == '1':

            print('When working with files, if instead of using the folder, use it\'s content (default: False)')
            print('Current Value: ' + str(config.folder_handle))

            temp = input('Set to True (1)\nSet to False (2)\nBack (3)')

            if temp == '1':

                config.folder_handle = True

            elif temp == '2':

                config.folder_handle = False

        elif temp == '2':

            config.folder1 = input('Write the Path to the folder1 (ex: C:/.../.../)\n>>>')

        elif temp == '3':

            config.folder2 = input('Write the Path to the folder2 (ex: C:/.../.../)\n>>>')

    elif temp == '2':

        temp = input('folder content (1)\nBack (2)')

        if temp == '1':

            temp = input('Execute (1)\nChange Folders (2)\nBack (3)')

            if temp == '1':

                print('The Same Files: ', compare.folder_compare(config.folder1, config.folder2)[0])
                print('The Files in Folder1 wich aren\'t in Folder2', compare.folder_compare(config.folder1, config.folder2)[1])
                print('The Files in Folder2 wich aren\'t in Folder1', compare.folder_compare(config.folder1, config.folder2)[2])

                input('>>>')

            elif temp == '2':

                input('Go to Config and then change Folder1 and Folder2\n>>>')

    else:
        break
