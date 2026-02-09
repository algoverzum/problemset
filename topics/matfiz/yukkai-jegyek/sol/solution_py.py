#!/usr/bin/env python3
# @check-accepted: *

n = int(input())  # diákok száma
names = []
scores = []
for _ in range(n):
    name, score = input().split()
    names.append(name)
    scores.append(int(score))
fails = sum(1 for x in scores if x < 50)  # bukottak
max_score = max(scores)
min_score = min(scores)
best_index = scores.index(max_score)
worst_index = scores.index(min_score)
best_name = names[best_index]
worst_name = names[worst_index]

sorted_scores = sorted(scores)
passed_students = [names[i] for i in range(n) if scores[i] >= 50]
print(f"Megbuktak: {fails}")
print(f"Legjobb: {best_name} ({max_score})")
print(f"Legrosszabb: {worst_name} ({min_score})")
print("Rendezett pontok:", *sorted_scores)
if passed_students:
    print("Átmentek:", *passed_students)
else:
    print("Átmentek: -")  # ha senki sem ment át
