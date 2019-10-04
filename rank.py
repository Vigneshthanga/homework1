#!/usr/bin/python
import statistics
import math
marks = [47, 63, 71, 39, 47, 49, 43, 37, 81, 69, 38, 13, 29, 61, 49, 53, 57, 23, 58, 17, 73, 33, 29]
grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+','C', 'C-', 'D', 'F']
marks.sort()
_sum = 0
print(marks)
for i in range(0, len(marks)):
    _sum += marks[i]
print('sum '+str(_sum))
mean = _sum/len(marks)
print('mean '+str(mean))
sd = statistics.stdev(marks)
print('Standard Deviation '+str(sd))
step = (sd/3)

print('step '+str(step))
mean_index = 5

scores = []

for i in range(len(grade)):
    scores.append(0)

i = mean_index
j = 0
while i < len(grade):
    scores[i] = mean - (step*j)
    j += 1
    i += 1

i = mean_index-1
j = 1
while i >= 0:
    scores[i] = mean + (step*j)
    j += 1
    i -= 1

i = 0
j = 0
idx = 0
flag = False
while (j < len(marks)):
    idx = 0
    flag = False
    i = 0
    while i < len(scores):
        if (marks[j] >= scores[i]):
            flag = True
            if (i != 0):
                print('mark '+ str(marks[j])+' grade '+str(grade[i-1]))
            else:
                print('mark '+ str(marks[j])+' grade '+str(grade[i]))
            break
        else:
            i += 1
    if (not flag):
        i = len(scores)-1
        print('mark '+ str(marks[j])+' grade '+str(grade[i]))
    j += 1
