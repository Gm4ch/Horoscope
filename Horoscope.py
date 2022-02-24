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
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    monthNum = months.index(monthName)
    return monthNum

def chineseZodiacSign(sign_num): #reuturns the animal name based on the number that is inputed
    sign_text = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Sheep"]
    return sign_text[sign_num]

def chinese_zodiac_calc(year):
    chineseZodiacNum = int(year) % 12 #the math to turn the birthyear ito a remainder.
    chineseZodiacNum = int(chineseZodiacNum)
    retSign = chineseZodiacSign(chineseZodiacNum) #running the function to turn the remainder number into an animal name.
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
    int(birthMonth) #if the month is a number it runs a conversion function to turn it into a word
    stringMonth = num_to_month(birthMonth)
except ValueError:
    stringMonth = birthMonth #if an error occurs the program knows that month is a string

invalidDay = True
while (invalidDay):
    try: #telling the computer to try the following
        birthDay = int(input("what day of " + stringMonth.capitalize() + " were you born on? "))
        if int(birthDay) in range(1,32):
            invalidDay = False
        else:
            print("please provide a valid answer")
    except ValueError: #if the computer has a "Value error" error type rather than the program shutting down it does the following
        print("please provide a valid answer")
try: 
    intMonth = int(birthMonth) #if the month is a word it runs a conversion function to turn it into a number
except ValueError:
    intMonth = month_to_num(birthMonth) #if a type error occurs the program knows its a string and changes it.

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

print("Your chinese zodiac sign is", chinese_zodiac_calc(birthYear))
