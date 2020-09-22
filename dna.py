from cs50 import *
from csv import reader, DictReader
from sys import argv

with open(argv[1], "r") as f:
    spam = reader(f)
    i = 0
    datas = dict()
    for row in spam:
        if i == 0:
            words = row
            words.pop(0)
        else:
            datas[row[0]] = row[1:]
        i += 1

with open(argv[2], "r") as f:
    spam = reader(f)
    for row in spam:
        seq = row[0]

len_seq = len(seq)
keys = []
for word in words:
    i = 0
    cnt = 0
    mx = 0
    len_word = len(word)

    while i < len_seq:
        cnt = 0
        while i < len_seq and word == seq[i:i + len_word]:
            cnt += 1
            if cnt > mx:
                mx = cnt
            i += len_word
        i += 1
    keys.append(str(mx))

found = False
for k, v in datas.items():
    if v == keys:
        found = True
        print(k)
        break

if not found:
    print("No match")
