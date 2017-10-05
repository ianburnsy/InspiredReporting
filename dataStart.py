# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""access_conn - currently have the wrong password for SA so this isn't working......
access_conn = pyodbc.connect(r"DSN=TCOACCESS;"r"UID=sa;"r"PWD=Prospect2012;")
access_cursor = access_conn.cursor()
"""
#imports
import pyodbc
import time



"""
# Database connections
# Act! connection
"""
act_conn = pyodbc.connect(r"DSN=ACT;"r"UID='bd team pot';"r"PWD=CabinetBlinds54;")
act_cursor = act_conn.cursor()


"""
The update function fetches all USERID'S AND USERLOGINS and sets globally.
The act cursor in this occasion is selecting the userlogin first, then the
userid from the table dbo.TBL_USER. It then iterates through the number of rows
by using the range zero to the number of rows. In this occasion we are using slicing
to get just the userlogin 
"""
def update_salespeople():
    act_cursor.execute("SELECT USERLOGIN, USERID FROM dbo.TBL_USER")
    global salespeople
    salespeople = act_cursor.fetchall()
    for people in range(0,len(salespeople)):
        print(salespeople[people][0])

update_salespeople()  

#Converts the USERID'S and USERLOGIN's into a dictionary 
salespeopledict = dict(salespeople)
print(salespeopledict["Mikie Butcher"])

#Select USERID from USERLOGIN
selectedlogin = input("Input Login: ")


"""
The below piece of code is for SQL reporting using the between function for
"""


today_full = time.localtime()
this_year = today_full[0]
this_month = today_full[1]
this_daydate = today_full[2]

sql_today_between = ("BETWEEN '"+str(this_year)+"-"+str(this_month)+"-"+str(this_daydate)+
" 00:00:00' AND '"+str(this_year)+"-"+str(this_month)+"-"+str(this_daydate+1)+" 00:00:00');")




def from_today():
    today_full = time.localtime()
    year = today_full[0]
    month = today_full[1]
    week = today_full[2]//7
    day = today_full[2]
    daysfromyearstart = today_full[7]
    if today_full[6] == 0:
        dayname = "Monday"
    elif today_full[6] == 1:
        dayname = "Tuesday"
    elif today_full[6] == 2:
        dayname = "Wednesday"
    elif today_full[6] == 3:
        dayname = "Wednesday"
    elif today_full[6] == 4:
        dayname = "Thursday"
    else:
        dayname = "Friday"
    if year == 2016 or 2020 or 2024:
        febdays = 29
    else: febdays = 28
    print(year,month,week,day,dayname,daysfromyearstart)
    
from_today()



"""
The next function should help serve if we wish to create a user input
button or let the user select a specific date range. 
"""
def dateframe():
    print("Please put year in yyyy format, month in mm and day in dd.")
    global startyear
    startyear = input("Start Year: ")
    global startmonth
    startmonth = input("Start Month: ")
    global startday 
    startday = input("Start Day: ")
    global endyear
    endyear = input("End Year: ")
    global endmonth
    endmonth = input("End Month: ")
    global endday 
    endday = input("End Day: ")
dateframe()





"""
Count the number of histories created within the timespan outlined in the 
dateframe() function and for the salesperson defined in the 
update_salesperson() function.
"""
"""
def count_histories():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                       WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                       '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear,startmonth,startday,endyear,endmonth,endday,selectedid))
    historycount = act_cursor.fetchall()
    print(historycount)
count_histories()
"""
def todayscounting():
    act_cursor.execute("SELECT COUNT (CREATEUSERID) FROM dbo.TBL_HISTORY \
                       WHERE (CREATEUSERID = '{D26B6923-EAA2-471F-87DA-49C3F778684A}')\
                       AND (CREATEDATE BETWEEN '2017-05-17 00:00:00' AND \
                       '2017-05-18 00:00:00');")
    historycount = act_cursor.fetchall()
    print(historycount)

todayscounting()
