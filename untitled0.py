# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 17:55:03 2017

@author: ianb

This is all about counting histories that have been carried out on the Act!
database.
Running the program will initially execute all histories created. This will be
displayed as all histories created today, then all this week, then all this month,
then all this year and then all time. 
It then displays the option to select the different usernames. 
It also displays the option to look at different history types.
"""

"""
THE DATABASE CONNECTION
"""
import pyodbc
act_conn = pyodbc.connect(r"DSN=ACT;"r"UID='bd team pot';"r"PWD=CabinetBlinds54;")
act_cursor = act_conn.cursor()

"""
TIME AND DATE VARIABLES
The below import organises date variables.
"""
import time
today_full = time.localtime()
print(today_full)

"""
The below variable uses the format needed to carry out an SQL BETWEEN date function
using the day from import time and the organisation of date variables. The variable below
just looks at what has been done today. It does this by pulling specific date elements from
time.localtime() 
"""
sql_today_between = ("BETWEEN '"+str(today_full[0])+"-0"+str(today_full[1])+"-"+str(today_full[2])+
" 00:00:00' AND '"+str(today_full[0])+"-0"+str(today_full[1])+"-"+str(today_full[2]+1)+" 00:00:00')")

"""
DIFFERENT USERNAMES FUNCTIONS AND VARIABLES

Simple select execution from a single table. In this case we use it to obtain 
logins and the reference id's. Because it is easier for users to recognise the 
usernames and the computer stores everything via the userid we can use then store
these values in a python dictionary using the fetchall to collect the data
and calling dict over the function and storing it in the variable user_id_dict.  
 
"""
#to create a dictionary that links userlogin with userid
act_cursor.execute("SELECT USERLOGIN, USERID FROM dbo.TBL_USER")
user_id = dict(act_cursor.fetchall())

#to create a list of usernames
act_cursor.execute("SELECT USERLOGIN FROM dbo.TBL_USER")
username_list = act_cursor.fetchall()
print(username_list)

"""
selected_id








The below function calls an the pyodbc link to execute a call on the act database
We are looking at counting every history created by a specific user between some dates 
set.
The reason why the function doesn't currently work is that we haven't defined the
userid.
"""

def count_this_year():
    act_cursor.execute("SELECT COUNT (CREATEUSERID) FROM dbo.TBL_HISTORY \
                       WHERE (CREATEUSERID = 'D26B6923-EAA2-471F-87DA-49C3F778684A') AND (CREATEDATE {0};".format(sql_today_between))          
    historycount = act_cursor.fetchall()
    print(historycount)

count_this_year()

