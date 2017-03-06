    
def calcHandicap(rounds, diffList):
    handicapDiff = diffList[:]
    x = 0
    total = 0
    if rounds <= 6:
        diffUsed = 1
    elif rounds <=8:
        diffUsed = 2
    elif rounds <= 10:
        diffUsed = 3
    elif rounds <= 12:
        diffUsed = 4
    elif rounds <= 14:
        diffUsed = 5
    elif rounds <= 16:
        diffUsed = 6
    elif rounds == 17:
        diffUsed = 7
    elif rounds == 18:
        diffUsed = 8
    elif rounds == 19:
        diffUsed = 9
    elif rounds >= 20:
        diffUsed = 10    
    while x < diffUsed:
        low = min(handicapDiff)
        handicapDiff.remove(low)
        total = total+low
        x += 1
    handicap = (.96*(total/diffUsed))
    handicap = round(handicap, 2)
    return handicap
        