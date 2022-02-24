import calendar
import datetime
from enum import Enum
#importing the calender library


#function to take a number from the user and turn it into the month name
def num_to_month(monthNum):
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    monthNum = int(monthNum) - 1
    month = (months[monthNum])
    return month #returning the month name when the function is called

def month_to_num(monthName):
    if monthName == "january":
        month_Num = 1
    if monthName == "febuary":
        month_Num = 2
    if monthName == "march":
        month_Num = 3
    if monthName == "april":
        month_Num = 4
    if monthName == "may":
        month_Num = 5
    if monthName == "june":
        month_Num = 6
    if monthName == "july":
        month_Num = 7
    if monthName == "august":
        month_Num = 8
    if monthName == "september":
        month_Num = 9
    if monthName == "october":
        month_Num = 10
    if monthName == "november":
        month_Num = 11
    if monthName == "december":
        month_Num = 12
    return int(month_Num)

def chineseZodiacSign(sign_num):
    sign_text = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Sheep"]
    return sign_text[sign_num]

def chinese_zodiac_calc(year):
    chineseZodiacNum = int(year) % 12
    chineseZodiacNum = int(chineseZodiacNum)
    retSign = chineseZodiacSign(chineseZodiacNum)
    return retSign
    
invalidMonth = True 
while (invalidMonth):  #while the month is invalid the loop runs
    try:
        birthMonth = (input("What month were you born on? ").lower().strip()) #asking user when they were born
        if(birthMonth.capitalize() in list(calendar.month_name)): #if the month that the user entered is a valid month in the calender library the loop ends
            birthMonth = birthMonth.lower()
            invalidMonth = False
        elif(int(birthMonth) <=12 and int(birthMonth) >=1): #if the month is between 1 and 12 the loop ends
            str(birthMonth)
            birthMonth = birthMonth.lstrip("0")
            int(birthMonth)
            invalidMonth = False
        else:
            print("Not a valid month name. check for misspelling or incorrect number format") #if neither of the arguments are true the program tells the user thier input is wrong and keeps looping.
    except ValueError:
        print("Not a valid month name. check for misspelling or incorrect number format") #if neither of the arguments are true the program tells the user thier input is wrong and keeps looping.

try: 
    int(birthMonth)
    stringMonth = num_to_month(birthMonth)
except ValueError:
    stringMonth = num_to_month(birthMonth)

invalidDay = True
while (invalidDay):
    try: #telling the computer to try the following
        birthDay = int(input("what day of " + stringMonth + " were you born on? "))
        if int(birthDay) in range(1,32):
            invalidDay = False
        else:
            print("please provide a valid answer")
    except ValueError: #if the computer has a "Value error" error type rather than the program shutting down it does the following
        print("please provide a valid answer")
''' MAIN AREA OF PROBLEM
if type(birthMonth) == str:
    intMonth = month_to_num(birthMonth)
elif type(birthMonth) == int or type(birthMonth) == float:
    intMonth = birthMonth
'''
invalidYear = True
while (invalidYear):
    try: #telling the computer to try the following
        birthYear = input("what year were you born on? ")
        if datetime.datetime(int(birthYear), intMonth, int(birthDay)) and len(birthYear) == 4:
            invalidYear = False
        else:
            print("please provide a valid answer")
    except ValueError: #if the computer has a "Value error" error type rather than the program shutting down it does the following
        print("please provide a valid answer!")

#rework user input for month name rather than month number

print("your chinese zodiac sign is", chinese_zodiac_calc(birthYear))
