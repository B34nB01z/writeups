# Wells-read

![Coding](https://img.shields.io/badge/Coding--orange?style=for-the-badge) ![Points - 100](https://img.shields.io/badge/Points-100-9cf?style=for-the-badge)

```txt
R-Boy finds the time machine, which Zer0 used to travel to another era. Nearby, lies a copy of HG Wells’ The Time Machine. Could this book from the past help R-Boy travel in time? Unfortunately, R-Boy can’t read or understand it, because the space-time continuum has changed some of the words. Help R-Boy to start his time travels!
```

---

Here, we got a `wells.txt`and a `words.txt` in a ZIP archive. After looking through the text, we noticed that some words were wrong and that they always had one mistake in them. Then, I decided to parse the files into all words and use RegEx to find weird words. I put the output of that into a file and made a second script which checked for the actual wrong words.

The first script, `findwrong.py`, filtered out the empty lines/words and for the rest, I removed non-word characters from the beginning or the end. Then, I looked for every word that is not in the `words.txt` and added them to a list. I noticed that there were “some” words that looked like “its--a”, so I checked through the first list of wrong words and split them by non-word characters and checked if they then were in the `words.txt`.

In the second script `getdiff.py`, I decided that a word is wrong when there is a difference of 1 between the word and a word of the same length (words.txt) or if there is one character different when both are lowercase. When one of the previous two conditions matched, I added the result of the first comparison to a string and then wrote that out into a file. After looking at the file, we noticed that the flag was right in the garbage output.

<center><b>{FLG:1_kn0w_3v3ryth1ng_4b0ut_t1m3_tr4v3ls}</b></center>

