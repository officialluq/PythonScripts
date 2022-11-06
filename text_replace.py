import sys, os
import re

words_to_delete = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']

f = open(f'{os.getcwd()}/{sys.argv[1]}', 'r')
txt = f.read()
for word in words_to_delete:
    txt = re.sub(rf'(?<![a-zA-Z]){word}(?![a-z-Z])', '', txt)


print(txt)