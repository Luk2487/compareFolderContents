# core module with useful and upgraded funcs
# imports
import os
import config

# funcs
"""theinput is the folder inside wich you'll search, return a list,
folder_handler must be either True (instead of append folder to the list, append it's content, handle inceptions)
or False to append the folder"""


def better_listdir(theinput, thelist):

    temp = os.listdir(theinput)

    if config.folder_handle:

        for each in temp:

            if os.path.isfile(theinput+'/'+each):

                thelist.append(each)
            else:

                better_listdir(theinput+'/'+each, thelist, True)

        return thelist

    else:
        for each in temp:

            thelist.append(each)

        return thelist
