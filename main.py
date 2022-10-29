import json
import random
from pprint import pprint

words = []
start_end = {}
starts = {}
used = set()
curr_word = ""

with open("words.txt", "r", encoding="utf-8") as f:
    words = list(filter(lambda word: word.count(" ") == 1, f.read().split("\n")))
    curr_word = random.choice(words)


def make_start_end():
    out = {}
    for word in words:
        temp = word.split(" ")
        out[word] = [temp[0], temp[-1]]
    with open("startend.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=4, ensure_ascii=False)


def make_graph():
    out = {}
    with open("startend.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for k, v in data.items():
            key = v[0]
            if key in out:
                out[key].append(k)
            else:
                out[key] = [k]
    with open("starts.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=4, ensure_ascii=False)


# make_start_end()
with open("startend.json", "r", encoding="utf-8") as f:
    start_end = json.load(f)
# make_graph()
with open("starts.json", "r", encoding="utf-8") as f:
    starts = json.load(f)

print("Start")
while True:
    used.add(curr_word)
    # ans = input(curr_word + "\n")

    # if ans == "":
    #     print("AI wins")
    #     break
    # if ans not in words:
    #     print("Not in word list")
    #     continue
    # if start_end[ans][0] != start_end[curr_word][1]:
    #     print("Invalid ans")
    #     continue
    # if ans in used:
    #     print("Used word")
    #     continue

    # curr_word = ans
    # used.add(curr_word)
    print(curr_word)
    curr_end = start_end[curr_word][1]
    if curr_end not in starts:
        print("Player wins")
        break

    choices = list(filter(lambda word: word not in used, starts[curr_end]))
    if len(choices) == 0:
        print("Player wins")
        break

    choice_lens = [0 for _ in choices]
    for i, word in enumerate(choices):
        word_end = start_end[word][1]
        if word_end not in starts:
            continue
        if word in used:
            continue
        choice_lens[i] = len(starts[word_end])

    curr_word = choices[min(range(len(choice_lens)), key=choice_lens.__getitem__)]
