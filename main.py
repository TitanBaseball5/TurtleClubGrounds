import requests
from bs4 import BeautifulSoup
import datetime
import os
from flask import Flask, render_template
from datetime import date
from datetime import datetime
from pytz import timezone
from jinja2 import Template
from colorama import Fore, Back, Style



app = Flask(__name__)

def league_organizer(diamondEvents, diamondMound, diamondBase):
	listCounter2 = 0
	for x in range(len(diamondEvents)):
		if "LittleTurtles" in diamondEvents[listCounter2]:
			diamondMound.append("50 ft")
			diamondBase.append("60 ft with Safety Bag")
		elif "SeniorT-Ball" in diamondEvents[
		    listCounter2] or "JuniorT-Ball" in diamondEvents[listCounter2]:
			diamondMound.append("50 ft")
			diamondBase.append("60 ft")
		elif "Rookie" in diamondEvents[listCounter2]:
			diamondMound.append("44 ft with circle 8ft")
			diamondBase.append("65 ft")
		elif "Mosquito" in diamondEvents[listCounter2]:
			diamondMound.append("44 ft")
			diamondBase.append("65 ft")
		elif "PeeWee" in diamondEvents[listCounter2]:
			diamondMound.append("50 ft")
			diamondBase.append("75 ft")
		elif "Jr.Softball" in diamondEvents[listCounter2]:
			diamondMound.append("30 ft")
			diamondBase.append("45 ft SB")
		elif "Sr.Softball" in diamondEvents[listCounter2]:
			diamondMound.append("35 ft")
			diamondBase.append("55 ft SB")
		elif "AthleticsU10" in diamondEvents[listCounter2]:
			diamondMound.append("35 ft")
			diamondBase.append("50 ft SB")
		elif "AthleticsU12" in diamondEvents[listCounter2]:
			diamondMound.append("38 ft")
			diamondBase.append("60 ft SB")
		elif "AthleticsU14" in diamondEvents[listCounter2]:
			diamondMound.append("38 ft")
			diamondBase.append("60 ft SB")
		elif "AthleticsU16" in diamondEvents[listCounter2]:
			diamondMound.append("40 ft")
			diamondBase.append("60  SBft")
		elif "AthleticsU19" in diamondEvents[listCounter2]:
			diamondMound.append("43 ft")
			diamondBase.append("60 ft SB")
		elif "Titans8U" in diamondEvents[listCounter2]:
			diamondMound.append("44 ft with circle 8ft")
			diamondBase.append("65 ft")
		elif "Titans9U" in diamondEvents[listCounter2]:
			diamondMound.append("44 ft with circle 8ft")
			diamondBase.append("65 ft")
		elif "Titans10U" in diamondEvents[listCounter2]:
			diamondMound.append("44 ft")
			diamondBase.append("65 ft")
		elif "Titans11U" in diamondEvents[listCounter2]:
			diamondMound.append("44 ft")
			diamondBase.append("65 ft")
		elif "Titans12U" in diamondEvents[listCounter2]:
			diamondMound.append("50 ft")
			diamondBase.append("75 ft")
		elif "Titans13U" in diamondEvents[listCounter2]:
			diamondMound.append("50 ft")
			diamondBase.append("75 ft")
		elif "Titans14U" in diamondEvents[listCounter2]:
			diamondMound.append("60 ft")
			diamondBase.append("90 ft")
		elif "Titans15U" in diamondEvents[listCounter2]:
			diamondMound.append("60 ft")
			diamondBase.append("90 ft")
		elif "Titans16U" in diamondEvents[listCounter2]:
			diamondMound.append("60-1/2 ft")
			diamondBase.append("90 ft")
		elif "Titans17U/18U" in diamondEvents[listCounter2]:
			diamondMound.append("60-1/2 ft")
			diamondBase.append("90 ft")
		listCounter2 = listCounter2 + 1
	return diamondMound, diamondBase


def day_adjuster(diamondCounter, stringOfEvents, rWselectiveColoum):
	while True:

		rWstringOfSEvents = stringOfEvents[diamondCounter].text.replace(
		    " ", "")

		listOfTEvents.append(rWstringOfSEvents)
		rWselectiveColoum = rWselectiveColoum.replace(rWstringOfSEvents, "")

		diamondCounter = diamondCounter + 1

		if len(rWselectiveColoum) == 0:
			break
	return listOfTEvents, diamondCounter


def preList_DiamondOrganizer(preList):
	preListCounter = 0
	runLoopForPreEvents = len(preList)

	for z in range(runLoopForPreEvents):

		if "TurtleClub-Diamond#1" in preList[preListCounter]:
			preDiamondOneEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "TurtleClub-Diamond#2" in preList[preListCounter]:
			preDiamondTwoEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "TurtleClub-Diamond#3" in preList[preListCounter]:
			preDiamondThreeEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "TurtleClub-Diamond#4" in preList[preListCounter]:
			preDiamondFourEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "TurtleClub-Diamond#5" in preList[preListCounter]:
			preDiamondFiveEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "TurtleClub-Diamond#6" in preList[preListCounter]:
			preDiamondSixEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "TurtleClub-Diamond#7" in preList[preListCounter]:
			preDiamondSevenEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "Villanova-Diamond#1" in preList[preListCounter]:
			preVDiamondOneEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		elif "Villanova-Diamond#2" in preList[preListCounter]:
			preVDiamondTwoEvents.append(preList[preListCounter])
			preListCounter = preListCounter + 1
		else:
			preListCounter = preListCounter + 1
	return preDiamondOneEvents, preDiamondTwoEvents, preDiamondThreeEvents, preDiamondFourEvents, preDiamondFiveEvents, preDiamondSixEvents, preDiamondSevenEvents, preVDiamondOneEvents, preVDiamondTwoEvents

def preDistance_adjuster(preMound,preBase,mound,base):
    nightlyMoundChange = preMound[(len(preMound)-1)]
    nightlyBaseChange = preBase[(len(preBase)-1)]

    if nightlyMoundChange == mound[0]:
        mound[0] = "No changes"
    if nightlyBaseChange == base[0]:
        base[0] = "No changes"
    return mound,base

def tuplecount_adjuster(timeE,mound,base,diamondNumber,diamondEvents):
    data = []
    if len(mound) == 1:
        data = (
            (diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0])
        )
    elif len(mound) == 2:
        data = (
            (diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0]),
            (diamondNumber,timeE[1],mound[1],base[1],diamondEvents[1])
        )
    elif len(mound) == 3:
        data = (
            (diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0]),
            (diamondNumber,timeE[1],mound[1],base[1],diamondEvents[1]),
            (diamondNumber,timeE[2],mound[2],base[2],diamondEvents[2])
        )
    elif len(mound) == 4:
        data = (
            (diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0]),
            (diamondNumber,timeE[1],mound[1],base[1],diamondEvents[1]),
            (diamondNumber,timeE[2],mound[2],base[2],diamondEvents[2]),
            (diamondNumber,timeE[3],mound[3],base[3],diamondEvents[3])
        )
    return data

def newTupleLogic(timeE,mound,base,diamondNumber,diamondEvents):
    if len(mound) == 1:
        data = [diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0]]
        data2 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')
        data3 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')
        data4 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')

        return data,data2,data3,data4
    elif len(mound) == 2:
        data = [diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0]]
        

        data2 = [diamondNumber,timeE[1],mound[1],base[1],diamondEvents[1]]

        data3 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')
        data4 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')

        return data,data2,data3,data4
    elif len(mound) == 3:
        data = [diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0]]
        

        data2 = [diamondNumber,timeE[1],mound[1],base[1],diamondEvents[1]]

        data3 = [diamondNumber,timeE[2],mound[2],base[2],diamondEvents[2]]
        
        data4 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')

        return data,data2,data3,data4
    elif len(mound) == 4:
        data = [diamondNumber,timeE[0],mound[0],base[0],diamondEvents[0]]
        

        data2 = [diamondNumber,timeE[1],mound[1],base[1],diamondEvents[1]]
        

        data3 = [diamondNumber,timeE[2],mound[2],base[2],diamondEvents[2]]
        
        
        data4 = [diamondNumber,timeE[3],mound[3],base[3],diamondEvents[3]]
        

        return data,data2,data3,data4
    else:
        data = (diamondNumber, 'NA', 'NA', 'NA', 'NA')
        data2 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')
        data3 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')
        data4 = (diamondNumber, 'NA', 'NA', 'NA', 'NA')
        return data,data2,data3,data4
        

def time_keeper(diamondEvents):
    counter = 0
    timeOfEvent = []
    for l in range(len(diamondEvents)):
        
        if "AM" in diamondEvents[counter]:
            comparator = 0
            subStringCount = diamondEvents[counter].find("AM")
            subStringEvent = diamondEvents[counter]
            timeOfEvent.append(subStringEvent[subStringCount-5:subStringCount+2])
              
            
            if (((timeOfEvent[counter])[0:1]).isdigit()) == False:
                timeOfEvent[counter] = (timeOfEvent[counter])[1:8]
                if (((timeOfEvent[counter])[0:1]).isdigit()) == False:
                    timeOfEvent[counter] = (timeOfEvent[counter])[1:8]

            if ((timeOfEvent[counter])[0:2]).isdigit() == True:
                comparator = int((timeOfEvent[counter])[0:2])
                if comparator > 17:
                    timeOfEvent[counter] = (timeOfEvent[counter])[1:8]


            counter = counter + 1
            
        elif "PM" in diamondEvents[counter]:
            subStringCount = diamondEvents[counter].find("PM")
            subStringEvent = diamondEvents[counter]
            timeOfEvent.append(subStringEvent[subStringCount-5:subStringCount+2])

            if (((timeOfEvent[counter])[0:1]).isdigit()) == False:
                timeOfEvent[counter] = (timeOfEvent[counter])[1:8]
                if (((timeOfEvent[counter])[0:1]).isdigit()) == False:
                    timeOfEvent[counter] = (timeOfEvent[counter])[1:8]
            
            if ((timeOfEvent[counter])[0:2]).isdigit() == True:
                comparator = int((timeOfEvent[counter])[0:2])
                if comparator > 9 and comparator != 12:
                    timeOfEvent[counter] = (timeOfEvent[counter])[1:8]

            counter = counter + 1


    return timeOfEvent

def tuple_NA(diamondNumber,data,comparatorNumber,chartNumber):
    if len(data) == 1 or len(data) == 2 or len(data) == 3 or len(data) == 4:
        if chartNumber == 1 :
            data = data[0]
            data = tuple(data)

        if chartNumber == 2 :
            data = data[1]
            data = tuple(data)
        if chartNumber == 3 :
            data = data[2]
            
            
    elif not len(data) >= comparatorNumber:
        data = (
            (diamondNumber,"NA","NA","NA","NA")
        )
        
    return data

def game_upper(diamondEvents):
    counter = 0
    newList = []
    for s in range (len(diamondEvents)):
        if "vs" in diamondEvents[counter]:
            diamondEvents[counter] = "GAME: *"+diamondEvents[counter]+"*"
            newList.append(diamondEvents[counter])

        else:
            newList.append(diamondEvents[counter])
        counter = counter + 1
    
    return newList

def practice_lower(diamondEvents):
    counter = 0
    newList = []
    for a in range (len(diamondEvents)):
        if "Practice" in diamondEvents[counter]:
            diamondEvents[counter] = "PRACTICE: "+diamondEvents[counter]
            newList.append(diamondEvents[counter])
        else:
            newList.append(diamondEvents[counter])
        counter = counter +1
    return newList

#Variables
diamondCounter = 0
listOfTEvents = []
listCounter = 0
diamondOneEvents = []
diamondTwoEvents = []
diamondThreeEvents = []
diamondFourEvents = []
diamondFiveEvents = []
diamondSixEvents = []
diamondSevenEvents = []
villanovaOneEvents = []
villanovaTwoEvents = []
TCBattingCages = []

diamondOneMound = []
diamondTwoMound = []
diamondThreeMound = []
diamondFourMound = []
diamondFiveMound = []
diamondSixMound = []
diamondSevenMound = []
vDiamondOneMound = []
vDiamondTwoMound = []

diamondOneBase = []
diamondTwoBase = []
diamondThreeBase = []
diamondFourBase = []
diamondFiveBase = []
diamondSixBase = []
diamondSevenBase = []
vDiamondOneBase = []
vDiamondTwoBase = []

preDiamondOneEvents = []
preDiamondTwoEvents = []
preDiamondThreeEvents = []
preDiamondFourEvents = []
preDiamondFiveEvents = []
preDiamondSixEvents = []
preDiamondSevenEvents = []
preVDiamondOneEvents = []
preVDiamondTwoEvents = []

preDiamondOneMound = []
preDiamondTwoMound = []
preDiamondThreeMound = []
preDiamondFourMound = []
preDiamondFiveMound = []
preDiamondSixMound = []
preDiamondSevenMound = []
preVDiamondOneMound = []
preVDiamondTwoMound = []

preDiamondOneBase = []
preDiamondTwoBase = []
preDiamondThreeBase = []
preDiamondFourBase = []
preDiamondFiveBase = []
preDiamondSixBase = []
preDiamondSevenBase = []
preVDiamondOneBase = []
preVDiamondTwoBase = []

timeReference = ["12:00AM","12:15AM","12:30AM","12:45AM","1:00AM","1:15AM","1:30AM","1:45AM","2:00AM","2:15AM","2:30AM","2:45AM","3:00AM","3:15AM","3:30AM","3:45AM","4:00AM","4:15AM","4:30AM","4:45AM","5:00AM","5:15AM","5:30AM","5:45AM","6:00AM","6:15AM","6:30AM","6:45AM","7:00AM","7:15AM","7:30AM","7:45AM","8:00AM","8:15AM","8:30AM","8:45AM","9:00AM","9:15AM","9:30AM","9:45AM","10:00AM","10:15AM","10:30AM","10:45AM","11:00AM","11:15AM","11:30AM","11:45AM","12:00PM","12:15PM","12:30PM","12:45PM","1:00PM","1:15PM","1:30PM","1:45PM","2:00PM","2:15PM","2:30PM","2:45PM","3:00PM","3:15PM","3:30PM","3:45PM","4:00PM","4:15PM","4:30PM","4:45PM","5:00PM","5:15PM","5:30PM","5:45PM","6:00PM","6:15PM","6:30PM","6:45PM","7:00PM","7:15PM","7:30PM","7:45PM","8:00PM","8:15PM","8:30PM","8:45PM","9:00PM","9:15PM","9:30PM","9:45PM","10:00PM","10:15PM","10:30PM","10:45PM","11:00PM","11:15PM","11:30PM","11:45PM"]

dayChange = 0

#Finding Day

est = timezone('EST')
todayDay = datetime.now(est)
todayDay = str(todayDay)
numberDate = todayDay[0:10].replace("-", " ")
day = numberDate[8:10]
month = numberDate[5:7]
year = numberDate[0:4]
space = " "
correctFormat = day + space + month + space + year

date = correctFormat

day_name = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
]

day = (datetime.strptime(date, '%d %m %Y').weekday())

r = requests.get("https://turtleclubbaseball.com/Calendar/")
soup = BeautifulSoup(r.text, 'html.parser')

stringOfEvents = soup.find_all('div', attrs={'class': 'calItem'})
#Coloums of Data in each calaendar coloum
coloumsOfData = soup.find_all('td', attrs={})

selectiveColoum = str(coloumsOfData[17].text)
rWselectiveColoum = selectiveColoum.replace(" ", "")



#MAKE SURE TO AUTOMATE THE PROCESS OF COLOUM PICKING
if day_name[day] == "Monday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    preDiamondOneEvents, preDiamondTwoEvents, preDiamondThreeEvents, preDiamondFourEvents, preDiamondFiveEvents, preDiamondSixEvents, preDiamondSevenEvents, preVDiamondOneEvents, preVDiamondTwoEvents = preList_DiamondOrganizer(preList)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Tuesday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Wednesday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Thursday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[21].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter4 = day_adjuster(diamondCounter3,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Friday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[21].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter4 = day_adjuster(diamondCounter3,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[22].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter5 = day_adjuster(diamondCounter4,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Saturday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[21].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter4 = day_adjuster(diamondCounter3,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[22].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter5 = day_adjuster(diamondCounter4,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[23].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter6 = day_adjuster(diamondCounter5, stringOfEvents,rWselectiveColoum)
    

else:
	#This is Sunday But need to get access to a preList of Saturday!!
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)


if type(listOfTEvents) == tuple:
    listOfTEvents = listOfTEvents[0]

runLoopForEvents = len(listOfTEvents)

for i in range(runLoopForEvents):
	if "TurtleClub-Diamond#1" in listOfTEvents[listCounter]:
		diamondOneEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#2" in listOfTEvents[listCounter]:
		diamondTwoEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#3" in listOfTEvents[listCounter]:
		diamondThreeEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#4" in listOfTEvents[listCounter]:
		diamondFourEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#5" in listOfTEvents[listCounter]:
		diamondFiveEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#6" in listOfTEvents[listCounter]:
		diamondSixEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#7" in listOfTEvents[listCounter]:
		diamondSevenEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TC-BattingCage#1" in listOfTEvents[listCounter]:
		TCBattingCages.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TC-BattingCage#2" in listOfTEvents[listCounter]:
		TCBattingCages.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	#Villy Diamond 1 is the bigger Diamond
	elif "Villanova-Diamond#1" in listOfTEvents[listCounter]:
		villanovaOneEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "Villanova-Diamond#2" in listOfTEvents[listCounter]:
		villanovaTwoEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1
	else:
		listCounter = listCounter + 1

diamondOneMound, diamondOneBase = league_organizer(diamondOneEvents,diamondOneMound,diamondOneBase)

diamondTwoMound, diamondTwoBase = league_organizer(diamondTwoEvents,diamondTwoMound,diamondTwoBase)

diamondThreeMound, diamondThreeBase = league_organizer(diamondThreeEvents,diamondThreeMound,diamondThreeBase)

diamondFourMound, diamondFourBase = league_organizer(diamondFourEvents,diamondFourMound,diamondFourBase)

diamondFiveMound, diamondFiveBase = league_organizer(diamondFiveEvents,diamondFiveMound,diamondFiveBase)

diamondSixMound, diamondSixBase = league_organizer(diamondSixEvents,diamondSixMound,diamondSixBase)

diamondSevenMound, diamondSevenBase = league_organizer(diamondSevenEvents,diamondSevenMound,diamondSevenBase)

vDiamondOneMound, vDiamondOneBase = league_organizer(villanovaOneEvents,vDiamondOneMound,vDiamondOneBase)

vDiamondTwoMound, vDiamondTwoBase = league_organizer(villanovaTwoEvents,vDiamondTwoMound,vDiamondTwoBase)

#Start writing the pre statements for the funciton league orgainzer
listCounter  = 0
runLoopForEvents = len(preList)
for z in range(runLoopForEvents):

    if "TurtleClub-Diamond#1" in preList[listCounter]:
        preDiamondOneEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        
    elif "TurtleClub-Diamond#2" in preList[listCounter]:
        preDiamondTwoEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        

    elif "TurtleClub-Diamond#3" in preList[listCounter]:
        preDiamondThreeEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        

    elif "TurtleClub-Diamond#4" in preList[listCounter]:
        preDiamondFourEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        

    elif "TurtleClub-Diamond#5" in preList[listCounter]:
        preDiamondFiveEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        

    elif "TurtleClub-Diamond#6" in preList[listCounter]:
        preDiamondSixEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        

    elif "TurtleClub-Diamond#7" in preList[listCounter]:
        preDiamondSevenEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        

	#Villy Diamond 1 is the bigger Diamond
    elif "Villanova-Diamond#1" in preList[listCounter]:
        preVDiamondOneEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        

    elif "Villanova-Diamond#2" in preList[listCounter]:
        preVDiamondTwoEvents.append(preList[listCounter])
        listCounter = listCounter + 1
        
    else:
        listCounter = listCounter + 1
        


preDiamondOneMound, preDiamondOneBase = league_organizer(preDiamondOneEvents, preDiamondOneMound, preDiamondOneBase)

preDiamondTwoMound, preDiamondTwoBase = league_organizer(preDiamondTwoEvents, preDiamondTwoMound, preDiamondTwoBase)

preDiamondThreeMound, preDiamondThreeBase = league_organizer(preDiamondThreeEvents, preDiamondThreeMound, preDiamondThreeBase)

preDiamondFourMound, preDiamondFourBase = league_organizer(preDiamondFourEvents, preDiamondFourMound, preDiamondFourBase)

preDiamondFiveMound, preDiamondFiveBase = league_organizer(preDiamondFiveEvents, preDiamondFiveMound, preDiamondFiveBase)

preDiamondSixMound, preDiamondSixBase = league_organizer(preDiamondSixEvents, preDiamondSixMound, preDiamondSixBase)

preDiamondSevenMound, preDiamondSevenBase = league_organizer(preDiamondSevenEvents, preDiamondSevenMound, preDiamondSevenBase)

preVDiamondOneMound, preVDiamondOneBase = league_organizer(preVDiamondOneEvents, preVDiamondOneMound, preVDiamondOneBase)

preVDiamondTwoMound, preVDiamondTwoBase = league_organizer(preVDiamondTwoEvents, preVDiamondTwoMound, preVDiamondTwoBase)

diamondTimeOne = time_keeper(diamondOneEvents)
diamondTimeTwo = time_keeper(diamondTwoEvents)
diamondTimeThree = time_keeper(diamondThreeEvents)
diamondTimeFour = time_keeper(diamondFourEvents)
diamondTimeFive = time_keeper(diamondFiveEvents)
diamondTimeSix = time_keeper(diamondSixEvents)
diamondTimeSeven = time_keeper(diamondSevenEvents)
diamondTimeVOne = time_keeper(villanovaOneEvents)
diamondTimeVTwo = time_keeper(villanovaTwoEvents)

diamondOneEvents = [diamondOneEvents.replace("TurtleClub-Diamond#1", "") for diamondOneEvents in diamondOneEvents] 
diamondTwoEvents = [diamondTwoEvents.replace("TurtleClub-Diamond#2", "") for diamondTwoEvents in diamondTwoEvents]  
diamondThreeEvents = [diamondThreeEvents.replace("TurtleClub-Diamond#3", "") for diamondThreeEvents in diamondThreeEvents] 
diamondFourEvents = [diamondFourEvents.replace("TurtleClub-Diamond#4", "") for diamondFourEvents in diamondFourEvents]  
diamondFiveEvents = [diamondFiveEvents.replace("TurtleClub-Diamond#5", "") for diamondFiveEvents in diamondFiveEvents]  
diamondSixEvents = [diamondSixEvents.replace("TurtleClub-Diamond#6", "") for diamondSixEvents in diamondSixEvents]  
diamondSevenEvents = [diamondSevenEvents.replace("TurtleClub-Diamond#7", "") for diamondSevenEvents in diamondSevenEvents] 
villanovaOneEvents = [villanovaOneEvents.replace("Villanova-Diamond#1","") for villanovaOneEvents in villanovaOneEvents]
villanovaTwoEvents = [villanovaTwoEvents.replace("Villanova-Diamond#2","") for villanovaTwoEvents in villanovaTwoEvents]

diamondOneEvents = game_upper(diamondOneEvents)
diamondTwoEvents = game_upper(diamondTwoEvents)
diamondThreeEvents = game_upper(diamondThreeEvents)
diamondFourEvents = game_upper(diamondFourEvents)
diamondFiveEvents = game_upper(diamondFiveEvents)
diamondSixEvents = game_upper(diamondSixEvents)
diamondSevenEvents = game_upper(diamondSevenEvents)
villanovaOneEvents = game_upper(villanovaOneEvents)
villanovaTwoEvents = game_upper(villanovaTwoEvents)

diamondOneEvents = practice_lower(diamondOneEvents)
diamondTwoEvents = practice_lower(diamondTwoEvents)
diamondThreeEvents = practice_lower(diamondThreeEvents)
diamondFourEvents = practice_lower(diamondFourEvents)
diamondFiveEvents = practice_lower(diamondFiveEvents)
diamondSixEvents = practice_lower(diamondSixEvents)
diamondSevenEvents = practice_lower(diamondSevenEvents)
villanovaOneEvents = practice_lower(villanovaOneEvents)
villanovaTwoEvents = practice_lower(villanovaTwoEvents)

diamondOneEvents = [diamondOneEvents.replace("Practice", "") for diamondOneEvents in diamondOneEvents] 
diamondTwoEvents = [diamondTwoEvents.replace("Practice", "") for diamondTwoEvents in diamondTwoEvents]  
diamondThreeEvents = [diamondThreeEvents.replace("Practice", "") for diamondThreeEvents in diamondThreeEvents] 
diamondFourEvents = [diamondFourEvents.replace("Practice", "") for diamondFourEvents in diamondFourEvents]  
diamondFiveEvents = [diamondFiveEvents.replace("Practice", "") for diamondFiveEvents in diamondFiveEvents]  
diamondSixEvents = [diamondSixEvents.replace("Practice", "") for diamondSixEvents in diamondSixEvents]  
diamondSevenEvents = [diamondSevenEvents.replace("Practice", "") for diamondSevenEvents in diamondSevenEvents] 
villanovaOneEvents = [villanovaOneEvents.replace("Practice","") for villanovaOneEvents in villanovaOneEvents]
villanovaTwoEvents = [villanovaTwoEvents.replace("Practice","") for villanovaTwoEvents in villanovaTwoEvents]

headings = ("Diamond #","Time","Pitching Distance","Base Distance", "Info",)
headings2 = ("Diamond #","Time","Pitching Distance","Base Distance", "Info",)
headings3 = ("Diamond #","Time","Pitching Distance","Base Distance", "Info",)
headings4 = ("Diamond #","Time","Pitching Distance","Base Distance", "Info",)

caption = "Today's Schedule"
caption2 = "Today's Schedule Cont'd"
caption3 = "Today's Schedule Cont'd"
caption4 = "Today's Schedule Cont'd"



dOne,dOne2,dOne3,dOne4 = newTupleLogic(diamondTimeOne,diamondOneMound,diamondOneBase,"1",diamondOneEvents)
dTwo,dTwo2, dTwo3,dTwo4 = newTupleLogic(diamondTimeTwo,diamondTwoMound,diamondTwoBase,"2",diamondTwoEvents)
dThree,dThree2,dThree3,dThree4 = newTupleLogic(diamondTimeThree,diamondThreeMound,diamondThreeBase,"3",diamondThreeEvents)
dFour,dFour2,dFour3,dFour4 = newTupleLogic(diamondTimeFour,diamondFourMound,diamondFourBase,"4",diamondFourEvents)
dFive,dFive2,dFive3,dFive4 = newTupleLogic(diamondTimeFive,diamondFiveMound,diamondFiveBase,"5",diamondFiveEvents)
dSix,dSix2,dSix3,dSix4 = newTupleLogic(diamondTimeSix,diamondSixMound,diamondSixBase,"6",diamondSixEvents)
dSeven,dSeven2,dSeven3,dSeven4 = newTupleLogic(diamondTimeSeven,diamondSevenMound,diamondSevenBase,"7",diamondSevenEvents)
dVOne,dVOne2,dVOne3,dVOne4 = newTupleLogic(diamondTimeVOne,vDiamondOneMound,vDiamondOneBase,"V1",villanovaOneEvents)
dVTwo,dVTwo2,dVTwo3,dVTwo4 = newTupleLogic(diamondTimeVTwo,vDiamondTwoMound,vDiamondTwoBase,"V2",villanovaTwoEvents)

cC1 = (
    (dOne[0],dOne[1],dOne[2],dOne[3],dOne[4]),
    (dTwo[0],dTwo[1],dTwo[2],dTwo[3],dTwo[4]),
    (dThree[0],dThree[1],dThree[2],dThree[3],dThree[4]),
    (dFour[0],dFour[1],dFour[2],dFour[3],dFour[4]),
    (dFive[0],dFive[1],dFive[2],dFive[3],dFive[4]),
    (dSix[0],dSix[1],dSix[2],dSix[3],dSix[4]),
    (dSeven[0],dSeven[1],dSeven[2],dSeven[3],dSeven[4]),
    (dVOne[0],dVOne[1],dVOne[2],dVOne[3],dVOne[4]),
    (dVTwo[0],dVTwo[1],dVTwo[2],dVTwo[3],dVTwo[4]),
)

cC2 = (
    (dOne2[0],dOne2[1],dOne2[2],dOne2[3],dOne2[4]),
    (dTwo2[0],dTwo2[1],dTwo2[2],dTwo2[3],dTwo2[4]),
    (dThree2[0],dThree2[1],dThree2[2],dThree2[3],dThree2[4]),
    (dFour2[0],dFour2[1],dFour2[2],dFour2[3],dFour2[4]),
    (dFive2[0],dFive2[1],dFive2[2],dFive2[3],dFive2[4]),
    (dSix2[0],dSix2[1],dSix2[2],dSix2[3],dSix2[4]),
    (dSeven2[0],dSeven2[1],dSeven2[2],dSeven2[3],dSeven2[4]),
    (dVOne2[0],dVOne2[1],dVOne2[2],dVOne2[3],dVOne2[4]),
    (dVTwo2[0],dVTwo2[1],dVTwo2[2],dVTwo2[3],dVTwo2[4]),
)

cC3 = (
    (dOne3[0],dOne3[1],dOne3[2],dOne3[3],dOne3[4]),
    (dTwo3[0],dTwo3[1],dTwo3[2],dTwo3[3],dTwo3[4]),
    (dThree3[0],dThree3[1],dThree3[2],dThree3[3],dThree3[4]),
    (dFour3[0],dFour3[1],dFour3[2],dFour3[3],dFour3[4]),
    (dFive3[0],dFive3[1],dFive3[2],dFive3[3],dFive3[4]),
    (dSix3[0],dSix3[1],dSix3[2],dSix3[3],dSix3[4]),
    (dSeven3[0],dSeven3[1],dSeven3[2],dSeven3[3],dSeven3[4]),
    (dVOne3[0],dVOne3[1],dVOne3[2],dVOne3[3],dVOne3[4]),
    (dVTwo3[0],dVTwo3[1],dVTwo3[2],dVTwo3[3],dVTwo3[4]),
)


cC4 =(
    (dOne4[0],dOne4[1],dOne4[2],dOne4[3],dOne4[4]),
    (dTwo4[0],dTwo4[1],dTwo4[2],dTwo4[3],dTwo4[4]),
    (dThree4[0],dThree4[1],dThree4[2],dThree4[3],dThree4[4]),
    (dFour4[0],dFour4[1],dFour4[2],dFour4[3],dFour4[4]),
    (dFive4[0],dFive4[1],dFive4[2],dFive4[3],dFive4[4]),
    (dSix4[0],dSix4[1],dSix4[2],dSix4[3],dSix4[4]),
    (dSeven4[0],dSeven4[1],dSeven4[2],dSeven4[3],dSeven4[4]),
    (dVOne4[0],dVOne4[1],dVOne4[2],dVOne4[3],dVOne4[4]),
    (dVTwo4[0],dVTwo4[1],dVTwo4[2],dVTwo4[3],dVTwo4[4]),
)



if cC1 == (('1', 'NA', 'NA', 'NA', 'NA'), ('2', 'NA', 'NA', 'NA', 'NA'), ('3', 'NA', 'NA', 'NA', 'NA'), ('4', 'NA', 'NA', 'NA', 'NA'), ('5', 'NA', 'NA', 'NA', 'NA'), ('6', 'NA', 'NA', 'NA', 'NA'), ('7', 'NA', 'NA', 'NA', 'NA'), ('V1', 'NA', 'NA', 'NA', 'NA'), ('V2', 'NA', 'NA', 'NA', 'NA')):
    cC1 = (
        ()
    )
    headings = (
        ()
    )
    caption = ""

if cC2 == (('1', 'NA', 'NA', 'NA', 'NA'), ('2', 'NA', 'NA', 'NA', 'NA'), ('3', 'NA', 'NA', 'NA', 'NA'), ('4', 'NA', 'NA', 'NA', 'NA'), ('5', 'NA', 'NA', 'NA', 'NA'), ('6', 'NA', 'NA', 'NA', 'NA'), ('7', 'NA', 'NA', 'NA', 'NA'), ('V1', 'NA', 'NA', 'NA', 'NA'), ('V2', 'NA', 'NA', 'NA', 'NA')):
    cC2 = (
        ()
    )
    headings2 = (
        ()
    )
    caption2 = ""


if cC3 == (('1', 'NA', 'NA', 'NA', 'NA'), ('2', 'NA', 'NA', 'NA', 'NA'), ('3', 'NA', 'NA', 'NA', 'NA'), ('4', 'NA', 'NA', 'NA', 'NA'), ('5', 'NA', 'NA', 'NA', 'NA'), ('6', 'NA', 'NA', 'NA', 'NA'), ('7', 'NA', 'NA', 'NA', 'NA'), ('V1', 'NA', 'NA', 'NA', 'NA'), ('V2', 'NA', 'NA', 'NA', 'NA')):
    cC3 = (
        ()
    )
    headings3 = (
        ()
    )
    caption3 = ""

if cC4 == (('1', 'NA', 'NA', 'NA', 'NA'), ('2', 'NA', 'NA', 'NA', 'NA'), ('3', 'NA', 'NA', 'NA', 'NA'), ('4', 'NA', 'NA', 'NA', 'NA'), ('5', 'NA', 'NA', 'NA', 'NA'), ('6', 'NA', 'NA', 'NA', 'NA'), ('7', 'NA', 'NA', 'NA', 'NA'), ('V1', 'NA', 'NA', 'NA', 'NA'), ('V2', 'NA', 'NA', 'NA', 'NA')):
    cC4 = (
        ()
    )
    headings4 = (
        ()
    )
    caption4 = ""





diamondCounter = 0
listOfTEvents = []
listCounter = 0
diamondOneEvents = []
diamondTwoEvents = []
diamondThreeEvents = []
diamondFourEvents = []
diamondFiveEvents = []
diamondSixEvents = []
diamondSevenEvents = []
villanovaOneEvents = []
villanovaTwoEvents = []
TCBattingCages = []

diamondOneMound = []
diamondTwoMound = []
diamondThreeMound = []
diamondFourMound = []
diamondFiveMound = []
diamondSixMound = []
diamondSevenMound = []
vDiamondOneMound = []
vDiamondTwoMound = []

diamondOneBase = []
diamondTwoBase = []
diamondThreeBase = []
diamondFourBase = []
diamondFiveBase = []
diamondSixBase = []
diamondSevenBase = []
vDiamondOneBase = []
vDiamondTwoBase = []



dayChange = 0

if day == 6:
    day = 0
else:
    day = day + 1

if day_name[day] == "Monday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    preDiamondOneEvents, preDiamondTwoEvents, preDiamondThreeEvents, preDiamondFourEvents, preDiamondFiveEvents, preDiamondSixEvents, preDiamondSevenEvents, preVDiamondOneEvents, preVDiamondTwoEvents = preList_DiamondOrganizer(preList)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Tuesday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Wednesday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Thursday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[21].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter4 = day_adjuster(diamondCounter3,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Friday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[21].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter4 = day_adjuster(diamondCounter3,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[22].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter5 = day_adjuster(diamondCounter4,stringOfEvents,rWselectiveColoum)
    

elif day_name[day] == "Saturday":
    selectiveColoum = str(coloumsOfData[17].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[18].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter1 = day_adjuster(diamondCounter,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[19].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter2 = day_adjuster(diamondCounter1,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[20].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter3 = day_adjuster(diamondCounter2,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[21].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter4 = day_adjuster(diamondCounter3,stringOfEvents,rWselectiveColoum)
    selectiveColoum = str(coloumsOfData[22].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter5 = day_adjuster(diamondCounter4,stringOfEvents,rWselectiveColoum)
    preList = listOfTEvents
    selectiveColoum = str(coloumsOfData[23].text)
    rWselectiveColoum = selectiveColoum.replace(" ", "")
    listOfTEvents = []
    listOfTEvents, diamondCounter6 = day_adjuster(diamondCounter5, stringOfEvents,rWselectiveColoum)
    

else:
	#This is Sunday But need to get access to a preList of Saturday!!
    newUrlPtOne = "https://turtleclubbaseball.com/Calendar/?Day=" 
    newUrlPtTwo = "&Month="
    newUrlPtThree = "&Year=2021&Label="
    
    if int(date[0:1]) == 0:
        
        dayForUrl = int(date[1:2]) 
        dayForUrl = dayForUrl+1
        
    else:
        dayForUrl = int(date[0:2])
        dayForUrl = dayForUrl+1
        
    monthForUrl = int(date[4:5])
    dayForUrl = str(dayForUrl)
    monthForUrl = str(monthForUrl)
    newCompleteUrl = newUrlPtOne+dayForUrl+newUrlPtTwo+monthForUrl+newUrlPtThree
    
    r2 = requests.get(newCompleteUrl)
    soup2 = BeautifulSoup(r.text,'html.parser')
    
    stringOfE = soup.find_all('div', attrs = {'class':'calItem'})
    cOD = soup.find_all('td',attrs = {})
   
    selectiveC = str(cOD[17].text)

    rWselectiveC = selectiveC.replace(" ","")
    listOfTEvents = []
    listOfTEvents,diamondCounter = day_adjuster(diamondCounter,stringOfE,rWselectiveC)

    


if type(listOfTEvents) == tuple:
    listOfTEvents = listOfTEvents[0]

runLoopForEvents = len(listOfTEvents)

for i in range(runLoopForEvents):
	if "TurtleClub-Diamond#1" in listOfTEvents[listCounter]:
		diamondOneEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#2" in listOfTEvents[listCounter]:
		diamondTwoEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#3" in listOfTEvents[listCounter]:
		diamondThreeEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#4" in listOfTEvents[listCounter]:
		diamondFourEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#5" in listOfTEvents[listCounter]:
		diamondFiveEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#6" in listOfTEvents[listCounter]:
		diamondSixEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TurtleClub-Diamond#7" in listOfTEvents[listCounter]:
		diamondSevenEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TC-BattingCage#1" in listOfTEvents[listCounter]:
		TCBattingCages.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "TC-BattingCage#2" in listOfTEvents[listCounter]:
		TCBattingCages.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	#Villy Diamond 1 is the bigger Diamond
	elif "Villanova-Diamond#1" in listOfTEvents[listCounter]:
		villanovaOneEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1

	elif "Villanova-Diamond#2" in listOfTEvents[listCounter]:
		villanovaTwoEvents.append(listOfTEvents[listCounter])
		listCounter = listCounter + 1
	else:
		listCounter = listCounter + 1

diamondOneMound, diamondOneBase = league_organizer(diamondOneEvents,diamondOneMound,diamondOneBase)

diamondTwoMound, diamondTwoBase = league_organizer(diamondTwoEvents,diamondTwoMound,diamondTwoBase)

diamondThreeMound, diamondThreeBase = league_organizer(diamondThreeEvents,diamondThreeMound,diamondThreeBase)

diamondFourMound, diamondFourBase = league_organizer(diamondFourEvents,diamondFourMound,diamondFourBase)

diamondFiveMound, diamondFiveBase = league_organizer(diamondFiveEvents,diamondFiveMound,diamondFiveBase)

diamondSixMound, diamondSixBase = league_organizer(diamondSixEvents,diamondSixMound,diamondSixBase)

diamondSevenMound, diamondSevenBase = league_organizer(diamondSevenEvents,diamondSevenMound,diamondSevenBase)

vDiamondOneMound, vDiamondOneBase = league_organizer(villanovaOneEvents,vDiamondOneMound,vDiamondOneBase)

vDiamondTwoMound, vDiamondTwoBase = league_organizer(villanovaTwoEvents,vDiamondTwoMound,vDiamondTwoBase)
        
diamondTimeOne = time_keeper(diamondOneEvents)
diamondTimeTwo = time_keeper(diamondTwoEvents)
diamondTimeThree = time_keeper(diamondThreeEvents)
diamondTimeFour = time_keeper(diamondFourEvents)
diamondTimeFive = time_keeper(diamondFiveEvents)
diamondTimeSix = time_keeper(diamondSixEvents)
diamondTimeSeven = time_keeper(diamondSevenEvents)
diamondTimeVOne = time_keeper(villanovaOneEvents)
diamondTimeVTwo = time_keeper(villanovaTwoEvents)

diamondOneEvents = [diamondOneEvents.replace("TurtleClub-Diamond#1", "") for diamondOneEvents in diamondOneEvents] 
diamondTwoEvents = [diamondTwoEvents.replace("TurtleClub-Diamond#2", "") for diamondTwoEvents in diamondTwoEvents]  
diamondThreeEvents = [diamondThreeEvents.replace("TurtleClub-Diamond#3", "") for diamondThreeEvents in diamondThreeEvents] 
diamondFourEvents = [diamondFourEvents.replace("TurtleClub-Diamond#4", "") for diamondFourEvents in diamondFourEvents]  
diamondFiveEvents = [diamondFiveEvents.replace("TurtleClub-Diamond#5", "") for diamondFiveEvents in diamondFiveEvents]  
diamondSixEvents = [diamondSixEvents.replace("TurtleClub-Diamond#6", "") for diamondSixEvents in diamondSixEvents]  
diamondSevenEvents = [diamondSevenEvents.replace("TurtleClub-Diamond#7", "") for diamondSevenEvents in diamondSevenEvents] 
villanovaOneEvents = [villanovaOneEvents.replace("Villanova-Diamond#1","") for villanovaOneEvents in villanovaOneEvents]
villanovaTwoEvents = [villanovaTwoEvents.replace("Villanova-Diamond#2","") for villanovaTwoEvents in villanovaTwoEvents]

diamondOneEvents = game_upper(diamondOneEvents)
diamondTwoEvents = game_upper(diamondTwoEvents)
diamondThreeEvents = game_upper(diamondThreeEvents)
diamondFourEvents = game_upper(diamondFourEvents)
diamondFiveEvents = game_upper(diamondFiveEvents)
diamondSixEvents = game_upper(diamondSixEvents)
diamondSevenEvents = game_upper(diamondSevenEvents)
villanovaOneEvents = game_upper(villanovaOneEvents)
villanovaTwoEvents = game_upper(villanovaTwoEvents)

diamondOneEvents = practice_lower(diamondOneEvents)
diamondTwoEvents = practice_lower(diamondTwoEvents)
diamondThreeEvents = practice_lower(diamondThreeEvents)
diamondFourEvents = practice_lower(diamondFourEvents)
diamondFiveEvents = practice_lower(diamondFiveEvents)
diamondSixEvents = practice_lower(diamondSixEvents)
diamondSevenEvents = practice_lower(diamondSevenEvents)
villanovaOneEvents = practice_lower(villanovaOneEvents)
villanovaTwoEvents = practice_lower(villanovaTwoEvents)

diamondOneEvents = [diamondOneEvents.replace("Practice", "") for diamondOneEvents in diamondOneEvents] 
diamondTwoEvents = [diamondTwoEvents.replace("Practice", "") for diamondTwoEvents in diamondTwoEvents]  
diamondThreeEvents = [diamondThreeEvents.replace("Practice", "") for diamondThreeEvents in diamondThreeEvents] 
diamondFourEvents = [diamondFourEvents.replace("Practice", "") for diamondFourEvents in diamondFourEvents]  
diamondFiveEvents = [diamondFiveEvents.replace("Practice", "") for diamondFiveEvents in diamondFiveEvents]  
diamondSixEvents = [diamondSixEvents.replace("Practice", "") for diamondSixEvents in diamondSixEvents]  
diamondSevenEvents = [diamondSevenEvents.replace("Practice", "") for diamondSevenEvents in diamondSevenEvents] 
villanovaOneEvents = [villanovaOneEvents.replace("Practice","") for villanovaOneEvents in villanovaOneEvents]
villanovaTwoEvents = [villanovaTwoEvents.replace("Practice","") for villanovaTwoEvents in villanovaTwoEvents]



data1 = tuplecount_adjuster(diamondTimeOne,diamondOneMound,diamondOneBase,"1",diamondOneEvents)
data2 = tuplecount_adjuster(diamondTimeTwo,diamondTwoMound,diamondTwoBase,"2",diamondTwoEvents)
data3 = tuplecount_adjuster(diamondTimeThree,diamondThreeMound,diamondThreeBase,"3",diamondThreeEvents)
data4 = tuplecount_adjuster(diamondTimeFour,diamondFourMound,diamondFourBase,"4",diamondFourEvents)
data5 =  tuplecount_adjuster(diamondTimeFive,diamondFiveMound,diamondFiveBase,"5",diamondFiveEvents)
data6 = tuplecount_adjuster(diamondTimeSix,diamondSixMound,diamondSixBase,"6",diamondSixEvents)
data7 = tuplecount_adjuster(diamondTimeSeven,diamondSevenMound,diamondSevenBase,"7",diamondSevenEvents)
data8 = tuplecount_adjuster(diamondTimeVOne,vDiamondOneMound,vDiamondOneBase,"V1",villanovaOneEvents)
data9 = tuplecount_adjuster(diamondTimeVTwo,vDiamondTwoMound,vDiamondTwoBase,"V2",villanovaTwoEvents)

data1 = tuple_NA("1",data1,5,1)
data2 = tuple_NA("2",data2,5,1)
data3 = tuple_NA("3",data3,5,1)
data4 = tuple_NA("4",data4,5,1)
data5 = tuple_NA("5",data5,5,1)
data6 = tuple_NA("6",data6,5,1)
data7 = tuple_NA("7",data7,5,1)
data8 = tuple_NA("V1",data8,5,1)
data9 = tuple_NA("V2",data9,5,1)

nextDayChart = (
    (data1[0],data1[1],data1[2],data1[3],data1[4]), 
    (data2[0],data2[1],data2[2],data2[3],data2[4]),
    (data3[0],data3[1],data3[2],data3[3],data3[4]),
    (data4[0],data4[1],data4[2],data4[3],data4[4]),
    (data5[0],data5[1],data5[2],data5[3],data5[4]),
    (data6[0],data6[1],data6[2],data6[3],data6[4]),
    (data7[0],data7[1],data7[2],data7[3],data7[4]),
    (data8[0],data8[1],data8[2],data8[3],data8[4]),
    (data9[0],data9[1],data9[2],data9[3],data9[4]),
)

if len(caption) >=1 and len(caption2)>=1 and len(caption3)>=1 and len(caption4)>=1:
    
    @app.route("/")
    def table():
        return render_template("table.html",headings=headings, data=cC1,data2=cC2,data3 = cC3, data5 = nextDayChart, data4 = cC4,headings2=headings2, headings3 = headings3, headings4 = headings4, caption = caption, caption2 = caption2, caption3 = caption3, caption4 = caption4)

    if __name__ == "__main__":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    
    
elif len(caption) >=1 and len(caption2)>=1 and len(caption3)>=1: 
    
    @app.route("/")
    def table():
        return render_template("table2.html",headings=headings, data= cC1,data2=cC2,data3 = cC3, data5 = nextDayChart, data4 = cC4,headings2=headings2, headings3 = headings3, headings4 = headings4, caption = caption, caption2 = caption2, caption3 = caption3, caption4 = caption4)

    if __name__ == "__main__":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    

elif len(caption) >=1 and len(caption2)>=1: 
    
    @app.route("/")
    def table():
        return render_template("table3.html",headings=headings, data=cC1,data2=cC2,data3 = cC3, data5 = nextDayChart, data4 = cC4,headings2=headings2, headings3 = headings3, headings4 = headings4, caption = caption, caption2 = caption2, caption3 = caption3, caption4 = caption4)

    if __name__ == "__main__":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    
elif len(caption) >=1: 
    
    @app.route("/")
    def table():
        return render_template("table4.html",headings=headings, data=cC1,data2=cC2,data3 = cC3, data5 = nextDayChart, data4 = cC4,headings2=headings2, headings3 = headings3, headings4 = headings4, caption = caption, caption2 = caption2, caption3 = caption3, caption4 = caption4)

    if __name__ == "__main__":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    
