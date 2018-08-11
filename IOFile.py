# -*- coding: utf-8 -*-
import codecs
import os
import io
import chardet

def getFromFile(fileDir, mode):

    try:
        aFile = codecs.open("files/"+fileDir, 'r', "utf-8")
        text = aFile.read()
        aFile.close()
    except:
        print("\n###\nФайл не существует или невозможно открыть!\n###\n")
        return 1
    else:
        if mode == 0:
            return text
        elif mode == 1:
            text = text.split('\n')
            for i in range(0, len(text)):
                text[i] = text[i].strip()
            return text
        elif mode == 2:
            text = text.split('\n')
            for i in range(0, len(text)):
                text[i] = text[i].strip()
            for i in range(0, len(text)):
                text[i] = text[i].split(' ')
            return text
            


def clearDir(path):
    list_dir = os.listdir(path)

    for file in list_dir:
        if os.path.isfile(path + "/" + file):
            os.remove(path + "/" + file)
        elif os.path.isdir(path + "/" + file):
            clearDir(path + "/" + file)
    pass