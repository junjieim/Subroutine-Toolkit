#!/usr/bin/env python
# -*- coding: utf-8 -*-

def saveTXT(basename, text):
    with open('ST_'+basename+'.txt', 'w') as file:
        file.write(basename+'\n')
        file.writelines(text)

def saveCSV(basename: str, text: dict):
    pass
