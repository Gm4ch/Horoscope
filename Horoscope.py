import calendar
import datetime
from bs4 import BeautifulSoup as bs
import requests as rq
import re
#importing the calender library

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

#function to take a number from the user and turn it into the month name
def num_to_month(monthNum):
    return months[int(monthNum)-1] #returning the month name when the function is called

def month_to_num(monthName):
    return months.index(monthName)+1

def chineseZodiacSign(sign_num): #reuturns the animal name based on the number that is inputed
    sign_text = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Sheep"]
    return sign_text[sign_num]

def chinese_zodiac_calc(year):
    chineseZodiacNum = int(year) % 12 #the math to turn the birthyear ito a remainder.
  #running the function to turn the remainder number into an animal name.
    return chineseZodiacSign(chineseZodiacNum)

def zodiac_finder(birthMonth,birthDay):
    if (birthMonth == 3 and birthDay >= 21) or (birthMonth == 4 and birthDay <= 20):
        zodiac = 'Aries'
    elif (birthMonth == 4 and birthDay >= 21) or (birthMonth == 5 and birthDay <= 20):
        zodiac = 'Taurus'
    elif (birthMonth == 5 and birthDay >= 21) or (birthMonth == 6 and birthDay <= 20):
        zodiac = 'Gemini'
    elif (birthMonth == 6 and birthDay >= 21) or (birthMonth == 7 and birthDay <= 22):
        zodiac = 'Cancer'
    elif (birthMonth == 7 and birthDay >= 23) or (birthMonth == 8 and birthDay <= 22):
        zodiac = 'Leo'
    elif (birthMonth == 8 and birthDay >= 23) or (birthMonth == 9 and birthDay <= 22):
        zodiac = 'Virgo'
    elif (birthMonth == 9 and birthDay >= 23) or (birthMonth == 10 and birthDay <= 22):
        zodiac = 'Libra'
    elif (birthMonth == 10 and birthDay >= 23) or (birthMonth == 11 and birthDay <= 22):
        zodaic = 'Scorpio'
    elif (birthMonth == 11 and birthDay >= 23) or (birthMonth == 12 and birthDay <= 21):
        zodaic = 'Sagittarius'
    elif (birthMonth == 12 and birthDay >= 22) or (birthMonth == 1 and birthDay <= 19):
        zodaic = 'Capricorn'
    elif (birthMonth == 1 and birthDay >= 20) or (birthMonth == 2 and birthDay <= 19):
        zodiac = 'Aquarius'
    elif (birthMonth == 2 and birthDay >= 20) or (birthMonth == 3 and birthDay <= 20):
        zodiac = 'Pisces'
    return zodiac

print("welcome to the horoscope and zodiac program!\n\n") #welcoming the user ot the program

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
            print("Not a valid month name. Check for misspelling or incorrect number format.") #if neither of the arguments are true the program tells the user thier input is wrong and keeps looping.
    except ValueError:
        print("Not a valid month name. Check for misspelling or incorrect number format.") #if neither of the arguments are true the program tells the user thier input is wrong and keeps looping.

try: 
    int(birthMonth) #if the month is a number it runs a conversion function to turn it into a word
    stringMonth = num_to_month(birthMonth)
except ValueError:
    stringMonth = birthMonth #if an error occurs the program knows that month is a string

invalidDay = True
while invalidDay:
    try: #telling the computer to try the following
        birthDay = int(input("What day of " + stringMonth.capitalize() + " were you born on? "))
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

zodiac_finder(intMonth, birthDay)

"""WEB SCRAPING!!!!""" 
def get_horoscope():
    
    def remove_html_tags(text):
        #Remove html tags from a string
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    website = ("https://nypost.com/horoscopes/"+zodiac_finder(intMonth, birthDay)+"/") #setting the correct website for the daily horoscope
    html_text = rq.get(website).text #getting the website through beautiful soup
    soup = bs(html_text, 'lxml')
    allDivs = soup.find_all('div', class_ = "horoscope__description") #finding the correct class in the HTML of the website
    dailyHoroscope = allDivs[1] #selecting the 2nd class of the divs
    return(remove_html_tags(str(dailyHoroscope))) #running the function to remove any tags

print('\n')
print("Your chinese zodiac sign is: ", chinese_zodiac_calc(birthYear))
print("Your official zodiac sign is: "+zodiac_finder(intMonth, birthDay))
print("you daily horoscope is:")
print(get_horoscope())




    
