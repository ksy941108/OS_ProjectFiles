# Sang Kim

from pandas import *

# reading CSV file
data = read_csv("processes.csv")

# converting column data to list
process = data["Process"].tolist()
bt = data["Burst Time"].tolist()
mem = data["Memory"].tolist()

# printing list data
print("Burst Time:", bt)
print("Memory Required:", mem)

max = 10000000
bigCore = []
littleCore = []

for i in range(len(bt)):
    if bt[i] > (max / 2):
        bigCore.append(bt[i])
    else:
        littleCore.append(bt[i])

# Little Cores
coreA = []
coreB = []
coreC = []

# Big Cores
coreD = []
coreE = []
coreF = []


a = 0
b = 1
c = 2
d = 0
e = 1
f = 2


while a < len(littleCore):
    if a == 0:
        coreA.append(littleCore[0])
        a += 3
    else:
        coreA.append(littleCore[a])
        a += 3

while b < len(littleCore):
    coreB.append(littleCore[b])
    b += 3

while c < len(littleCore):
    coreC.append(littleCore[c])
    c += 3

while d < len(bigCore):
    if d == 0:
        coreD.append(bigCore[0])
        d += 3
    else:
        coreD.append(bigCore[d])
        d += 3

while e < len(bigCore):
    coreE.append(bigCore[e])
    e += 3

while f < len(bigCore):
    coreF.append(bigCore[f])
    f += 3


def turnaround_time(exit, arrival):
    tat = []
    tat.append(exit + arrival)
    return tat


def littleCoreA():
    i = 0
    wt = [0]
    avg_wait = 0
    for i in range(len(coreA)):
        tat = turnaround_time(coreA[i], wt[i])
        if i > 0:
            print("CoreA[", i, "] Turnaround Time", tat, "Wait Time:", wt[i])
        else:
            print(
                "CoreA[ 0 ] Turnaround Time",
                turnaround_time(coreA[0], wt[0]),
                "Wait Time:",
                wt[i],
            )
        if i == 0:
            wt.append(coreA[i])
            avg_wait = wt[i] + avg_wait
        else:
            wt.append(coreA[i] + coreA[i - 1])
            avg_wait = wt[i] + avg_wait
    length = len(wt) - 1
    print("Average Turnaround Time:", tat[-1] / length)
    print("Average Wait Time:", avg_wait / length)
    print("")


def littleCoreB():
    i = 0
    wt = [0]
    avg_wait = 0
    for i in range(len(coreB)):
        tat = turnaround_time(coreB[i], wt[i])
        print("CoreB[", i, "] Turnaround Time", tat, "Wait Time:", wt[i])
        if i == 0:
            wt.append(coreB[i])
            avg_wait = wt[i] + avg_wait
        else:
            wt.append(coreB[i] + coreB[i - 1])
            avg_wait = wt[i] + avg_wait
    length = len(wt) - 1
    print("Average Turnaround Time:", tat[-1] / length)
    print("Average Wait Time:", avg_wait / (len(wt) - 1))
    print("")


def littleCoreC():
    i = 0
    wt = [0]
    avg_wait = 0
    for i in range(len(coreC)):
        tat = turnaround_time(coreC[i], wt[i])
        print("CoreC[", i, "] Turnaround Time", tat, "Wait Time:", wt[i])
        if i == 0:
            wt.append(coreC[i])
            avg_wait = wt[i] + avg_wait
        else:
            wt.append(coreC[i] + coreC[i - 1])
            avg_wait = wt[i] + avg_wait
    length = len(wt) - 1
    print("Average Turnaround Time:", tat[-1] / length)
    print("Average Wait Time:", avg_wait / length)
    print("")


def bigCoreD():
    i = 0
    wt = [0]
    avg_wait = 0
    for i in range(len(coreD)):
        tat = turnaround_time(coreD[i] / 2, wt[i])
        if i > 0:
            print("CoreD[", i, "] Turnaround Time", tat, "Wait Time:", wt[i])
        else:
            print(
                "CoreD[ 0 ] Turnaround Time ",
                turnaround_time(coreD[0] / 2, wt[0]),
                "Wait Time:",
                wt[0],
            )
        if i == 0:
            wt.append(coreD[i] / 2)
            avg_wait = wt[i] + avg_wait
        else:
            wt.append(coreD[i] / 2 + coreD[i - 1] / 2)
            avg_wait = wt[i] + avg_wait
    length = len(wt) - 1
    print("Average Turnaround Time:", tat[-1] / length)
    print("Average Wait Time:", avg_wait / length)
    print("")


def bigCoreE():
    i = 0
    wt = [0]
    avg_wait = 0
    for i in range(len(coreE)):
        tat = turnaround_time(coreE[i] / 2, wt[i])
        print("CoreE[", i, "] Turnaround Time", tat, "Wait Time:", wt[i])
        if i == 0:
            wt.append(coreE[i] / 2)
            avg_wait = wt[i] + avg_wait
        else:
            wt.append(coreE[i - 1] / 2 + coreE[i] / 2)
            avg_wait = wt[i] + avg_wait
    length = len(wt) - 1
    print("Average Turnaround Time:", tat[-1] / length)
    print("Average Wait Time:", avg_wait / (len(wt) - 1))
    print("")


def bigCoreF():
    i = 0
    wt = [0]
    avg_wait = 0
    for i in range(len(coreF)):
        tat = turnaround_time(coreF[i] / 2, wt[i])
        print("CoreF[", i, "] Turnaround Time", tat, "Wait Time:", wt[i])
        if i == 0:
            wt.append(coreF[i] / 2)
            avg_wait = wt[i] + avg_wait
        else:
            wt.append(coreF[i] / 2 + coreF[i - 1] / 2)
            avg_wait = wt[i] + avg_wait
    length = len(wt) - 1
    print("Average Turnaround Time:", tat[-1] / length)
    print("Average Wait Time:", avg_wait / (len(wt) - 1))
    print("")


littleCoreA()
littleCoreB()
littleCoreC()
bigCoreD()
bigCoreE()
bigCoreF()
