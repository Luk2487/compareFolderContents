# module to compare the content of folders / files by metadata, name...
# imports
import core


def folder_compare(input1, input2):

    list1 = core.better_listdir(input1, [])
    list2 = core.better_listdir(input2, [])
    same = []
    diff1 = []
    diff2 = []
    issame = False

    for each in list1:

        for each2 in list2:

            if each == each2 and not issame:

                same.append(each)
                issame = True
                break

        if not issame:
            diff1.append(each)

        issame = False

    for each in list2:

        for each2 in list1:

            if each == each2 and not issame:
                issame = True
                break

        if not issame:
            diff2.append(each)

        issame = False

    return [same, diff1, diff2]
