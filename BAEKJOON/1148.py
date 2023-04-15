# 단어 만들기

import sys
from collections import defaultdict

my_dic = []

while True:
    word = sys.stdin.readline().strip()
    if word == '-':
        break
    else:
        my_dic.append(sorted(word))

def check(word, charactors):
    word_idx = 0
    charactors_idx = 0

    while word_idx < len(word) and charactors_idx < len(charactors):
        if word[word_idx] == charactors[charactors_idx]:
            word_idx += 1
            charactors_idx += 1

            if word_idx == len(word):
                return True
        else:
            charactors_idx += 1

    return False

while True:
    charactors = sys.stdin.readline().strip()
    sort_charactors = sorted(charactors)
    if charactors == '#':
        break
    else:
        use_charactor_dic = defaultdict(int)
        for word in my_dic:
            if check(word, sort_charactors):
                for i in set(word):
                    use_charactor_dic[i] += 1
        for i in set(sort_charactors):
            if i not in use_charactor_dic:
                use_charactor_dic[i] = 0
        
        max_cnt = max(use_charactor_dic.values())
        min_cnt = min(use_charactor_dic.values())
        most_cnt_chr = []
        least_cnt_chr = []

        for key, value in use_charactor_dic.items():
            if value == max_cnt:
                most_cnt_chr.append(key)
            if value == min_cnt:
                least_cnt_chr.append(key)

        print(''.join(sorted(least_cnt_chr)), end=' ')
        print(min_cnt, end=' ')
        print(''.join(sorted(most_cnt_chr)), end=' ')
        print(max_cnt)