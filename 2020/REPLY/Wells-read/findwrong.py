import re
from time import sleep

# parse the wells.txt and remove all non-words and words where special characters are at the beginning/end
wells = []
with open("wells.txt", "r") as f:
    temp = f.read() \
        .replace("\n", " ") \
        .split(" ")

    # regex yey
    begin = re.compile(r"^[\W_]+")
    end = re.compile(r"[\W_]+$")
    for word in temp:
        word = end.sub("", begin.sub("", word))

        # also filter empty stuff
        if len(word.strip()) == 0:
            continue

        wells.append(word)

# get words and make them lowercase
words = []
with open("words.txt", "r") as f:
    words = f.read().split("\n")
    for i in range(len(words)):
        words[i] = words[i].lower()

# go through all the tokens and see if they arent in the dictionary
wrong1 = []
for word in wells:
    word = word.strip()
    if len(word) == 0:
        continue

    if word.lower() not in words:
        wrong1.append(word)

# after that, there may be "words" like "like--a" where they actually are good, but just really, messed up
# this matches those and removes them if they actually are words with messed up spaces
nonword = re.compile(r"[\W]+")
wrong2 = []
for word in wrong1:
    for token in nonword.split(word):
        if token.lower() not in words:
            wrong2.append(token)

with open("wrong.txt", "w") as f:
    s = ""
    for word in wrong2:
        s += word+"\n"
    f.write(s)