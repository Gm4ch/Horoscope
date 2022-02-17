import calendar
import datetime
#importing the calender library

myGlobal = 0

#function to take a number from the user and turn it into the month name
def num_to_month(month):
    if month == '1':
        month = 'january'
    if month == '2':
        month = 'february'  
    if month == '3':       
        month = 'march'
    if month == '4':
        month = 'april'
    if month =='5':
        month = 'may'
    if month == '6':
        month = 'june'
    if month == '7':
        month = 'july'
    if month == '8':
        month = 'august'
    if month == '9':
        month = 'september'
    if month =='10':
        month = 'october'
    if month == '11':
        month = 'november'
    if month == '12':
        month = 'december'
    return month #returning the month name when the function is called

#Return ... TBD
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
        birthMonth = input("What month were you born on? ").lower().strip() #asking user when they were born
        if(birthMonth.capitalize() in list(calendar.month_name)): #if the month that the user entered is a valid month in the calender library the loop ends
            birthMonth = birthMonth.lower()
            invalidMonth = False
        elif(int(birthMonth) <=12 and int(birthMonth) >=1): #if the month is between 1 and 12 the loop ends
            str(birthMonth)
            birthMonth = birthMonth.lstrip("0")
            int(birthMonth)
            invalidMonth = False
            birthMonth
            num_to_month(birthMonth) #the program calls on the function to convert the number into a name
        else:
            print("Not a valid month name. check for misspelling or incorrect number format") #if neither of the arguments are true the program tells the user thier input is wrong and keeps looping.
    except ValueError:
        print("Not a valid month name. check for misspelling or incorrect number format") #if neither of the arguments are true the program tells the user thier input is wrong and keeps looping.


invalidDay = True
while (invalidDay):
    try: #telling the computer to try the following
        birthDay = input("what day of " + num_to_month(birthMonth) + " were you born on? ")
        if int(birthDay) in range(1,32):
            invalidDay = False
        else:
            print("please provide a valid answer")
    except ValueError: #if the computer has a "Value error" error type rather than the program shutting down it does the following
        print("please provide a valid answer")
    
invalidYear = True
while (invalidYear):
    try: #telling the computer to try the following
        birthYear = input("what year were you born on? ")
        if datetime.datetime(int(birthYear), int(birthMonth), int(birthDay)) and len(birthYear) == 4:
            invalidYear = False
        else:
            print("please provide a valid answer")
    except ValueError: #if the computer has a "Value error" error type rather than the program shutting down it does the following
        print("please provide a valid answer!")

#rework user input for month name rather than month number

print("your chinese zodiac sign is", chinese_zodiac_calc(birthYear))
