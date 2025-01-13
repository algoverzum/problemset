#!/usr/bin/env python3
# @check-wrong-answer: examples all


n = int(input())
words = input().split()
words.sort(key=len)
print(words[0])
