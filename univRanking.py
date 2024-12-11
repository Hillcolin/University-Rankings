#
# @Author Colin Hill
#
# @Version 0.1
#
# This code takes two input files, reads them and produces: a count of the total universities in the top 100, a list of the total universities in the top 100,
# a list of available continents in the top 100, the ranking of a chosen university (the highest rank in that country), the top university in that country,
# the average score within the selected country, the relative score of a selected country in comparison to the continent, the capital city of the chosen
# country, and a list of universities that have the name of the capital in its name. All of these are printed onto another file.
#
# CSV1 - holds filename
# CSV2 - holds filename
# selectedCountry is the chosen input/ country from the user
#

import csv

import pandas as pd

global CSV1, CSV2

CSV1 = "TopUni.csv"
CSV2 = "capitals.csv"


# This function calls the separate functions that contain code to execute the above explained items and is called by testing files
# This also opens the files
# selectedCountry - the selected country
# output is the output file

def getInformation(selectedCountry, CSV1, CSV2):

    output = open("output.txt", "w")

    selectedCountry = selectedCountry.upper()

    try:
        topUni = open(CSV1, "r")
        cont = open(CSV2, "r")

    except FileNotFoundError:
        quit()

    Acountries()
    IntRank(selectedCountry)
    Ascore(selectedCountry)
    Rscore(selectedCountry)
    IntRank(selectedCountry)
    CapCity(selectedCountry)
    uniCap()

    output.write("Total number of universities => {}\n\n".format(uniCount()))
    output.write("Available countries => {}\n\n".format(newCountList))
    output.write("Available continents => {}\n\n".format(Acontinents()))
    output.write("At international rank => {} the university name is => {}\n\n".format(line[0], line[1].upper()))
    output.write(
        "At national rank => {} the university name is => {}\n\n".format(1, natRank(selectedCountry)[1].upper()))
    output.write("The average score => {:.2f}%\n\n".format(avScore))
    output.write(
        "The relative score to the top university in {} is => ({}/ {}) x 100% = {}\n\n".format(continent.upper(),avScore, max1, round(relativeScore, 2)))
    output.write("The capital is => {}\n\n".format(capital.upper()))

    # This prints the names of the universities that contain the capital name in its title
    output.write("The universities that contain the capital name => \n")

    for num in range(len(capList)):
        output.write("  #{} {}\n".format(num + 1, capList[num]))

    output.close()


# ////////////////////////////////////////////////////////////////////////////////

# This counts the number of universities in the TopUni.csv file
# topUni is opening CSV1
# outWrite reads each line
# uniCount increases by one each time the while loop, loops around through the file

def uniCount():  # Question 1

    topUni = open(CSV1, "r")
    outWrite = topUni.readline()
    uniCount = 0

    while outWrite != "":
        outWrite = topUni.readline()
        uniCount += 1

    uniCount = uniCount - 1
    topUni.close()

    return str(uniCount)


# ////////////////////////////////////////////////////////////////////////////////

# This makes a list of the countries included in the capitals.csv file, removing any repeats
# Countries opens CSV1
# countList is a column of the countries from CSV1
# newCountList is countList turn into a list

def Acountries():  # Question 2

    global newCountList
    Countries = pd.read_csv(CSV1, usecols=[2])
    countList = (Countries["Country"])
    countList = set(countList)
    newCountList = (", ".join(countList))
    newCountList.upper()


# ////////////////////////////////////////////////////////////////////////////////

# This prints the continents in the capitals.csv file, removing any repeats
# cont is CSV2
# contList is the column of the continents
# newContList is a list of contList

def Acontinents():  # Question 3

    cont = pd.read_csv(CSV2, usecols=[5])
    contList = (cont["Continent"])
    contList = set(contList)
    newContList = (", ".join(contList))

    return newContList.upper()


# ////////////////////////////////////////////////////////////////////////////////

# This function finds the top ranking university internationally of the chosen university and states what "place" it is in and the name of the top university
# first, the top ranked internationally university is chosen then all other universities are comapred to the placement
# for the national, if the national ranking of one is higher than that of the #1 internationally, then the national highest is that
# topUNIS is CSV1
# lien is the row of the top university internationally

def IntRank(selectedCountry):  # Question 4

    topUNIS = csv.reader(open(CSV1, "r"), delimiter=",")
    global line

    for row in topUNIS:

        if selectedCountry == row[2].upper():
            line = row
            break



# This function finds the highest ranking university nationally
# line3 is a list
# natLine is the line of the top university nationally
#
# NOTE: This was a bit strange to me because I thought the international highest would be that national highest, however,
# that is not the case with Japan

def natRank(selectedCountry): #Question 5

    topUNIS = csv.reader(open(CSV1, "r"), delimiter=",")
    global line3
    global natLine
    line3 = []
    natLine = ""

    for row in topUNIS:

        if selectedCountry == row[2].upper():
            line3.append(row)

    for row2 in line3:

        if row2[3] < line[3]:
            natLine = row2

    if natLine == "":
        natLine = line
        return natLine

    return natLine


# ////////////////////////////////////////////////////////////////////////////////

# The scores of the universities in the selected countries and averages them
# countryAvScore add together the scores from the country
# uniNum counts the number of universities in that country
# topUNIS is CSV1

def Ascore(selectedCountry):  # Question 6

    countryAvScore = 0
    uniNum = 0

    global avScore
    topUNIS = csv.reader(open(CSV1, "r"), delimiter=",")

    for row in topUNIS:

        if selectedCountry == row[2].upper():
            countryAvScore += float(row[8])
            uniNum += 1

    if uniNum == 0:
        uniNum = 1

    avScore = countryAvScore / uniNum


# ////////////////////////////////////////////////////////////////////////////////
#
# This finds the highest score in the continent then divides the country average score by that
# relativeScore is the relative score
# max is the highest score in the continent.
# continent is the continent of the selected country
# list is a list of the countries in the continent
# list2 is the scores from the continent universities compiled into a list

def Rscore(selectedCountry):  # Question 7

    global relativeScore
    global max1
    global continent

    capitals = csv.reader(open(CSV2, "r"), delimiter=",")
    list = []
    list2 = []
    max1 = 0
    continent = ""

    for row in capitals:

        if selectedCountry == row[0].upper():
            continent = row[5]
            break

    capitals = csv.reader(open(CSV2, "r"), delimiter=",")

    for spot in capitals:

        if continent == spot[5]:
            list.append(spot[0])

    topUni = csv.reader(open(CSV1, "r"), delimiter=",")

    for x in range(len(list)):

        topUni = csv.reader(open(CSV1, "r"), delimiter=",")
        for row1 in topUni:

            if list[x].upper() == row1[2].upper():
                list2.append(float(row1[8]))

    max1 = float(max(list2))

    relativeScore = (avScore / max1) * 100

# ////////////////////////////////////////////////////////////////////////////////

# This scans the capitals.csv file and returns the capital of the chosen country
# capitals is CSV2
# capital is the capital ofp the selected country

def CapCity(selectedCountry):  # Question 8

    capitals = csv.reader(open(CSV2, "r"), delimiter=",")
    global capital

    for spot in capitals:

        if selectedCountry == spot[0].upper():
            capital = spot[1]

            break

# ////////////////////////////////////////////////////////////////////////////////

# This makes a list of the universities that contain the capital name in the university title
# capList is a list of university names which contain the capital name of the selected country
# topUni is CSV1

def uniCap():  # Question 9

    global capList
    capList = []
    topUni = csv.reader(open(CSV1, "r"), delimiter=",")

    for row in topUni:
        words = row[1].split()

        if capital in words:
            capList.append(row[1])

# ////////////////////////////////////////////////////////////////////////////////

# This is commented out to make the code functional with the testers however this allows the user/tester to input a
# country manually

# Acountries()
# while True:
#
#     try:
#         selectedCountry = input("Enter a country name: ").upper()
#         if selectedCountry == "LIST":
#             print(newCountList.upper())
#         if selectedCountry in newCountList.upper():
#             break
#         if selectedCountry != type(str):
#             print("Try again:")
#         else:
#             quit()
#     except ValueError:
#         print("Incorrect input, try again:")
#
#
# getInformation(selectedCountry, CSV1, CSV2)
