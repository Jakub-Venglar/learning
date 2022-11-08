#calculates the chance of streak of 6 heads or tails in 100 coin flips in a row
import random
pokusu = 100
thereWasAStreak  = 0
for experimentNumber in range(pokusu):
    numberOfStreaks = 0
    streak=0
    flipList = []
    for flips in range(100):
        flipList.append(random.choice(['H','T']))
        if flips == 0:
            pass
        elif flipList[flips] == flipList[(flips-1)]:
            streak += 1
        else:
            streak = 0
        if streak == 5:
            numberOfStreaks +=1
    if numberOfStreaks > 0:
        thereWasAStreak += 1
print('The chance is %.2f%%' % (100*thereWasAStreak/pokusu))