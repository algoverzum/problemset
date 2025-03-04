#!/usr/bin/env python3
# @check-accepted: *

def binary_search(word, list):
    l = 0
    r = len(list) - 1
    while l <= r:
        mid = (l + r) // 2
        if list[mid] == word:
            return mid
        elif list[mid] < word:
            l = mid + 1
        else:
            r = mid - 1
    return None

n = int(input())

english_words = []
alien_words = []
for i in range(n):
    ew, aw = input().split()
    english_words.append(ew)
    alien_words.append(aw)
    
m = int(input())
message = []
for i in range(m):
    message.append(input())

for word in message:
    idx = binary_search(word, english_words)
    print(alien_words[idx])
