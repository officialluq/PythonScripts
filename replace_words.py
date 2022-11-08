import sys, os
import re
words = {'i':'oraz', 'oraz':'i', 'nigdy':'prawie nigdy', 'dlaczego':'czemu'}


i oraz dfkjgbdf
oraz oraz dfkjgbdf

def tokenize(data:str):
    return data.split(" ")

def replace_dict(replacemenet_dictionary: dict[str, str], to_replace: str) -> str:
    data_tok = tokenize(to_replace)

    array = []
    for word in words:
        array.append(rf'(?<![a-zA-Z]){word}(?![a-z-Z])')
    regex = '|'.join(array)
    return re.sub(regex, (lambda matched_group: replacemenet_dictionary[matched_group.group()]), to_replace)


f = open(f'{os.getcwd()}/{sys.argv[1]}', 'r')

txt = f.read()



print(replace_dict(words, txt))
