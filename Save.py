#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

def saveTXT(basename, text):
    with open('ST_'+basename+'.txt', 'w') as file:
        file.write(basename+'\n')
        file.writelines(text)

def saveCSV(data: dict):
    """
    data
    key1: ['line1', 'line2', 'line3', ...,]
    key2: ['line1', 'line2', 'line3', ...,]
    ...
    keyn: ['line1', 'line2', 'line3', ...,]
    line can be 'value' or 'value1 value2 ... valuen'
    """
    with open('ST_ouput.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['key', 'value'])
        for key, value in data.items():
            spamwriter.writerows([key] + v.split() for v in value)


if __name__ == '__main__':
    pass
