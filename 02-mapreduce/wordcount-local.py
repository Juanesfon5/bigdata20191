#!/usr/bin/python

import os, subprocess
import sys
import glob

import codecs


inputdir="."

if len(sys.argv) >= 1:
	inputdir = sys.argv[1]

def processdir(dir):

    dirList = glob.glob(dir)
    wordcount={}
    for f in dirList:
        wordcountfile(f,wordcount)
    for w in wordcount:
        print(w,wordcount[w])


def wordcountfile(f, wordcount):
#    file=open(f,'r')
    try:
        file = codecs.open(f, "r", "utf-8")
        for word in file.read().split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        file.close()
    except IOError, UnicodeDecodeError:
        print("skip file utf-8 error",f)            
    return wordcount        

processdir(inputdir)