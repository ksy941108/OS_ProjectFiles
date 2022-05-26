# Sang Kim

from pandas import *

# reading CSV file
data = read_csv("processes.csv")

# converting column data to list
process = data["Process"].tolist()
bt = data["Burst Time"].tolist()
mem = data["Memory"].tolist()

max = 16000
btMax = 10000000
bigMem = []
littleMem = []
bt1 = []
bt2 = []

for i in range(len(mem)):
    if mem[i] > (max / 2):
        bigMem.append(mem[i])
        bt2.append(bt[i])
    else:
        littleMem.append(mem[i])
        bt1.append(bt[i])

# Little mems
memA = []
memB = []
memC = []

# Big mems
memD = []
memE = []
memF = []

btA = []
btB = []
btC = []
btD = []
btE = []
btF = []

btmemA = []
btmemB = []
btmemC = []
btmemD = []
btmemE = []
btmemF = []

a = 0
b = 1
c = 2
d = 0
e = 1
f = 2


print(len(mem))
print(len(bt1))
print(len(bt2))
print(len(littleMem))
print(len(bigMem))


while a < len(littleMem):
    if a == 0:
        memA.append(littleMem[0])
        btA.append(bt1[0])
        a += 3
    else:
        memA.append(littleMem[a])
        btA.append(bt1[a])
        a += 3

while b < len(littleMem):
    memB.append(littleMem[b])
    btB.append(bt1[b])
    b += 3

while c < len(littleMem):
    memC.append(littleMem[c])
    btC.append(bt1[c])
    c += 3

while d < len(bigMem):
    if d == 0:
        memD.append(bigMem[0])
        btD.append(bt2[0])
        d += 3
    else:
        memD.append(bigMem[d])
        btD.append(bt2[d])
        d += 3

while e < len(bigMem):
    memE.append(bigMem[e])
    btE.append(bt2[e])
    e += 3


while f < len(bigMem):
    memF.append(bigMem[f])
    btF.append(bt2[f])
    f += 3


def turnaround(exit, arrival):
    tat = []
    tat.append(exit + arrival)
    return tat


def littleMemA():
    spaceA = 8000
    i = 0
    count = 0
    wt = [0]
    avg_wait = 0
    avg_tat = 0
    print(len(memA))
    for i in range(len(memA)):
        if spaceA >= memA[i]:
            spaceA -= memA[i]
            btmemA.append(btA[i])
        else:
            btmemA.append(btA[i])
            count += 1
            spaceA = 8000

    for j in range(len(btmemA)):
        tat = turnaround(btmemA[j], wt[j])
        if j > 0:
            print("btmemA [", j, "[ Turnaround Time", tat, "Wait Time:", wt[j])
        else:
            print(
                "btmemA [ 0 ] Turnaround Time",
                turnaround(btmemA[0], wt[0]),
                "Wait Time:",
                wt[j],
            )

        if j == 0:
            wt.append(btmemA[j])
            avg_wait = wt[j] + avg_wait
        else:
            wt.append(btmemA[j] + btmemA[j - 1])
            avg_wait = wt[j] + avg_wait
    length = (len(wt) - 1) + count
    print("AVG TAT:", tat[-1] / length)
    print("AVG WT:", avg_wait / length)


def littleMemB():
    spaceB = 8000
    i = 0
    count = 0
    wt = [0]
    avg_wait = 0
    print(len(memB))
    for i in range(len(memB)):
        if spaceB >= memB[i]:
            spaceB -= memB[i]
            btmemB.append(btB[i])
        else:
            btmemB.append(btB[i])
            count += 1
            spaceB = 8000

    for j in range(len(btmemB)):
        tat = turnaround(btmemB[j], wt[j])
        if j > 0:
            print("btmemB [", j, "[ Turnaround Time", tat, "Wait Time:", wt[j])
        else:
            print(
                "btmemB [ 0 ] Turnaround Time",
                turnaround(btmemB[0], wt[0]),
                "Wait Time:",
                wt[j],
            )

        if j == 0:
            wt.append(btmemB[j])
            avg_wait = wt[j] + avg_wait
        else:
            wt.append(btmemB[j] + btmemB[j - 1])
            avg_wait = wt[j] + avg_wait
    length = (len(wt) - 1) + count
    print("AVG TAT:", tat[-1] / length)
    print("AVG WT:", avg_wait / length)


def littleMemC():
    spaceC = 8000
    i = 0
    count = 0
    wt = [0]
    avg_wait = 0
    print(len(memC))
    for i in range(len(memC)):
        if spaceC >= memC[i]:
            spaceC -= memC[i]
            btmemC.append(btC[i])
        else:
            btmemC.append(btC[i])
            count += 1
            spaceC = 8000

    for j in range(len(btmemC)):
        tat = turnaround(btmemC[j], wt[j])
        if j > 0:
            print("btmemC [", j, "[ Turnaround Time", tat, "Wait Time:", wt[j])
        else:
            print(
                "btmemC [ 0 ] Turnaround Time",
                turnaround(btmemC[0], wt[0]),
                "Wait Time:",
                wt[j],
            )

        if j == 0:
            wt.append(btmemC[j])
            avg_wait = wt[j] + avg_wait
        else:
            wt.append(btmemC[j] + btmemC[j - 1])
            avg_wait = wt[j] + avg_wait
    length = (len(wt) - 1) + count
    print("AVG TAT:", tat[-1] / length)
    print("AVG WT:", avg_wait / length)


def bigMemD():
    spaceD = 16000
    i = 0
    count = 0
    wt = [0]
    avg_wait = 0
    print(len(memD))
    for i in range(len(memD)):
        if spaceD >= memD[i]:
            spaceD -= memD[i]
            btmemD.append(btD[i])
        else:
            btmemD.append(btD[i])
            count += 1
            spaceD = 16000

    for j in range(len(btmemD)):
        tat = turnaround(btmemD[j], wt[j])
        if j > 0:
            print("btmemD [", j, "[ Turnaround Time", tat, "Wait Time:", wt[j])
        else:
            print(
                "btmemD [ 0 ] Turnaround Time",
                turnaround(btmemD[0], wt[0]),
                "Wait Time:",
                wt[j],
            )

        if j == 0:
            wt.append(btmemD[j])
            avg_wait = wt[j] + avg_wait
        else:
            wt.append(btmemD[j] + btmemD[j - 1])
            avg_wait = wt[j] + avg_wait
    length = (len(wt) - 1) + count
    print("AVG TAT:", tat[-1] / length)
    print("AVG WT:", avg_wait / length)


def bigMemE():
    spaceE = 16000
    i = 0
    count = 0
    wt = [0]
    avg_wait = 0
    print(len(memE))
    for i in range(len(memE)):
        if spaceE >= memE[i]:
            spaceE -= memE[i]
            btmemE.append(btD[i])
        else:
            btmemE.append(btD[i])
            count += 1
            spaceE = 16000

    for j in range(len(btmemE)):
        tat = turnaround(btmemE[j], wt[j])
        if j > 0:
            print("btmemE [", j, "[ Turnaround Time", tat, "Wait Time:", wt[j])
        else:
            print(
                "btmemE [ 0 ] Turnaround Time",
                turnaround(btmemE[0], wt[0]),
                "Wait Time:",
                wt[j],
            )

        if j == 0:
            wt.append(btmemE[j])
            avg_wait = wt[j] + avg_wait
        else:
            wt.append(btmemE[j] + btmemE[j - 1])
            avg_wait = wt[j] + avg_wait
    length = (len(wt) - 1) + count
    print("AVG TAT:", tat[-1] / length)
    print("AVG WT:", avg_wait / length)


def bigMemF():
    spaceF = 16000
    i = 0
    count = 0
    wt = [0]
    avg_wait = 0
    print(len(memF))
    for i in range(len(memF)):
        if spaceF >= memF[i]:
            spaceF -= memF[i]
            btmemF.append(btD[i])
        else:
            btmemF.append(btD[i])
            count += 1
            spaceF = 16000

    for j in range(len(btmemF)):
        tat = turnaround(btmemF[j], wt[j])
        if j > 0:
            print("btmemF [", j, "[ Turnaround Time", tat, "Wait Time:", wt[j])
        else:
            print(
                "btmemF [ 0 ] Turnaround Time",
                turnaround(btmemF[0], wt[0]),
                "Wait Time:",
                wt[j],
            )

        if j == 0:
            wt.append(btmemF[j])
            avg_wait = wt[j] + avg_wait
        else:
            wt.append(btmemF[j] + btmemF[j - 1])
            avg_wait = wt[j] + avg_wait
    length = (len(wt) - 1) + count
    print("AVG TAT:", tat[-1] / length)
    print("AVG WT:", avg_wait / length)


littleMemA()
littleMemB()
littleMemC()
bigMemD()
bigMemE()
bigMemF()
