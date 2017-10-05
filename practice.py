# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:28:41 2017

@author: ianb
"""



"""When using the act database use this connector
"""
import pyodbc
act_conn = pyodbc.connect(r"DSN=ACT;"r"UID='bd team pot';"r"PWD=CabinetBlinds54;")
act_cursor = act_conn.cursor()



"""
The below piece of code is for SQL reporting using the between function for today.

"""
import time
today_full = time.localtime()
print(today_full)
this_year = today_full[0]
this_month = today_full[1]
this_daydate = today_full[2]

sql_today_between = ("BETWEEN '"+str(this_year)+"-0"+str(this_month)+"-"+str(this_daydate)+
" 00:00:00' AND '"+str(this_year)+"-"+str(this_month)+"-"+str(this_daydate+1)+" 00:00:00'")

sql_this_year =("BETWEEN '"+str(this_year)+"-01-01 00:00:00 AND '"+str(this_year)+"-"+str(this_month)
+"-"+str(this_daydate+1)+" 00:00:00'")
print(sql_this_year)


"""
This function uses pyodbc to count a given column within a given date range.
You can link this with SQL time reporting functions. 
"""
def count_today():
    act_cursor.execute("SELECT COUNT (CREATEUSERID) FROM dbo.TBL_HISTORY \
                       WHERE (CREATEUSERID = '{D26B6923-EAA2-471F-87DA-49C3F778684A}')\
                       AND (CREATEDATE BETWEEN '2017-05-15 00:00:00' AND \
                       '2017-05-18 00:00:00');")
    historycount = act_cursor.fetchall()
    print(historycount)

count_today()

def count_this_year():
    act_cursor.execute("SELECT COUNT (CREATEUSERID) FROM dbo.TBL_HISTORY \
                       WHERE (CREATEUSERID = '{D26B6923-EAA2-471F-87DA-49C3F778684A}')\
                       AND (CREATEDATE {0}.format(sql_today_between));")
    historycount1 = act_cursor.fetchall()
    print(historycount1)
count_this_year()
