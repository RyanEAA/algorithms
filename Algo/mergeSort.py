import math

stepcounter = 0

def merging(leftCabinet, rightCabinet):
    global stepcounter
    # Merge sort the left and right cabinets
    leftCabinet = mergesort(leftCabinet)
    rightCabinet = mergesort(rightCabinet)

    newCabinet = []
    
    while min(len(leftCabinet), len(rightCabinet)) > 0:
        if leftCabinet[0] > rightCabinet[0]:
            to_insert = rightCabinet.pop(0)
            newCabinet.append(to_insert)
            stepcounter += 1
        elif leftCabinet[0] <= rightCabinet[0]:
            to_insert = leftCabinet.pop(0)
            newCabinet.append(to_insert)
            stepcounter += 1

    if len(leftCabinet) > 0:
        for i in leftCabinet:
            newCabinet.append(i)
            stepcounter += 1

    if len(rightCabinet) > 0:
        for i in rightCabinet:
            newCabinet.append(i)
            stepcounter += 1
            
    return newCabinet

def mergesort(cabinet):
    if len(cabinet) == 1:
        return cabinet
    else:
        leftCabinet = mergesort(cabinet[:math.floor(len(cabinet) / 2)])
        rightCabinet = mergesort(cabinet[math.floor(len(cabinet) / 2):])
        return merging(leftCabinet, rightCabinet)

leftCabinet = [1, 3, 4, 4, 5, 7, 8, 9]
rightCabinet = [2, 4, 6, 7, 8, 8, 10, 12, 13, 14]
newCab = merging(leftCabinet, rightCabinet)
print(newCab)
print("Number of steps:", stepcounter)
