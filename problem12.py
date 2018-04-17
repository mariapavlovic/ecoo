file = open("DATA11.txt", "r")
counter = 0

while counter < 10:
    firstline = file.readline()
    firstsplit = firstline.split(' ')
    daysPlay = int(firstsplit[0])  # cat
    numDays = int(firstsplit[1])  # total days
    count = 0
    daysPass = 0
    totalCat = 0
    for i in range(numDays):
        newLine = file.readline()
        if newLine[0] == "E":
            if daysPass == 0:
                daysPass = 0
            elif daysPass > 0:
                daysPass += 1
        elif newLine[0] == "B":
            daysPass += 1
            totalCat += daysPlay
    finalAns = totalCat - daysPass
    if finalAns < 0:
        print(0)
    else:
        print(finalAns)

    counter += 1







# while count <= numDays:
#     count += 1
#     newLine = file.readline()
#     if newLine[0] == "E":
#         daysPass +=1
#     elif newLine[0] == "B":
#         daysPass += 1
#         print(daysPass)
#         print(daysPlay)
#         daysTo = daysPass + daysPlay
#         print(daysTo)
