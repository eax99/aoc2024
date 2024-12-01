# advent of code 2024, problem 1, solution by eax99
import fileinput
leftlist, rightlist = ([], [])
for line in fileinput.input():
    line = line.rstrip()
    parts = list(map(int, line.split()))
    leftlist.append(parts[0])
    rightlist.append(parts[1])
pairs_in_ascending_order = zip(sorted(leftlist), sorted(rightlist))
absolute_distance = lambda tup: abs(tup[0] - tup[1])
total_distance = sum(map(absolute_distance, pairs_in_ascending_order))
print("part 1:", total_distance)

right_list_times_appearing = {}
for n in rightlist:
    right_list_times_appearing[n] = right_list_times_appearing.get(n, 0) + 1
similarity_score = 0
for n in leftlist:
    similarity_score += n * right_list_times_appearing.get(n, 0)
print("part 2:", similarity_score)
