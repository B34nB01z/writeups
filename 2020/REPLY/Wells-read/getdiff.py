def get_diff(word1: str, word2: str) -> [str]:
    diff = []
    for i in range(len(word1)):
        if not word1[i] == word2[i]:
            diff.append(word1[i])
    return diff


# get words and make them lowercase
words = []
lower = []
with open("words.txt", "r") as f:
    words = f.read().split("\n")
    for i in range(len(words)):
        lower.append(words[i].lower())

wrong = []
with open("wrong.txt", "r") as f:
    wrong = f.read().split("\n")

for word in wrong:
    for l in range(len(lower)):
        if len(word) == len(lower[l]):
            diff1 = get_diff(word, words[l])
            diff2 = get_diff(word.lower(), lower[l])
            if len(diff1) == 1 or len(diff2) == 1:
                print(diff1)
                print(diff2)
                print(word)
                print(words[l])