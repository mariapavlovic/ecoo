file = open("DATA11.txt","r")
counter = 0

while counter < 3:
    totalCost = file.readline()
    percentYear = file.readline()
    totalPeople = file.readline()

    totalCost = int(totalCost)
    totalPeople = int(totalPeople)

    percentYear = percentYear.split(" ")

    year1 = float(percentYear[0])*totalPeople
    year2 = float(percentYear[1])*totalPeople
    year3 = float(percentYear[2])*totalPeople
    year4 = float(percentYear[3])*totalPeople

    counter += 1

    proceeds = year1*12 + year2*10 + year3*7 + year4*5

    tripProceeds = int(proceeds/2)

    if tripProceeds <= totalCost:
        print("YES")
    else:
        print("NO")