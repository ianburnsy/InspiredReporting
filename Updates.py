import pyodbc
import time
from datetime import date

"""
# Database connections
# Act! connection
"""
act_conn = pyodbc.connect(r"DSN=ACT;"r"UID='bd team pot';"r"PWD=CabinetBlinds54;")
act_cursor = act_conn.cursor()

def sales_identities():
    act_cursor.execute("SELECT USERLOGIN, USERID FROM dbo.TBL_USER")
    global salespeople
    salespeople = act_cursor.fetchall()

sales_identities()
x = str(date.today())



namespace1 = salespeople[0]
namespace2 = salespeople[1]
namespace3 = salespeople[2]
namespace4 = salespeople[3]
namespace5 = salespeople[4]
namespace6 = salespeople[5]
namespace7 = salespeople[6]
namespace8 = salespeople[7]
namespace9 = salespeople[8]

name1 = namespace1[0]
name2 = namespace2[0]
name3 = namespace3[0]
name4 = namespace4[0]
name5 = namespace5[0]
name6 = namespace6[0]
name7 = namespace7[0]
name8 = namespace8[0]
name9 = namespace9[0]


id1 = namespace1[1]
id2 = namespace2[1]
id3 = namespace3[1]
id4 = namespace4[1]
id5 = namespace5[1]
id6 = namespace6[1]
id7 = namespace7[1]
id8 = namespace8[1]
id9 = namespace9[1]




selectedid = "{4D20E74E-356B-428C-A7FD-49A8941D1336}"


thisyear = x[:4]
thismonth = x[5:7]
thisday = x[8:10]
startyear = thisyear
startmonth = thismonth
startday = "01"



def count_history1():

    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                       WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                       '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear,startmonth,startday,thisyear,thismonth,thisday,id1))
    historycount1 = act_cursor.fetchall()
    global name_and_results1
    name_and_results1 = (str(name1)+" "+str(historycount1))

count_history1()

def count_history2():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday,
                                                                                   thisyear, thismonth, thisday, id2))
    historycount2 = act_cursor.fetchall()
    global name_and_results1
    name_and_results1 = (str(name2) + " " + str(historycount2))

count_history2()

def count_history3():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday, thisyear, thismonth, thisday, id3))
    historycount3 = act_cursor.fetchall()
    global name_and_results3
    name_and_results3 = (str(name3) + " " + str(historycount3))
count_history3()

def count_history4():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday,
                                                                                   thisyear, thismonth, thisday, id4))
    historycount4 = act_cursor.fetchall()
    global name_and_results4
    name_and_results4 = (str(name4) + " " + str(historycount4))
count_history4()

def count_history5():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday,
                                                                                   thisyear, thismonth, thisday, id5))
    historycount5 = act_cursor.fetchall()
    global name_and_results5
    name_and_results5 = (str(name5) + " " + str(historycount5))
count_history5()

def count_history6():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday,
                                                                                   thisyear, thismonth, thisday, id6))
    historycount6 = act_cursor.fetchall()
    global name_and_results6
    name_and_results6 = (str(name6) + " " + str(historycount6))
count_history6()

def count_history7():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday,
                                                                                   thisyear, thismonth, thisday, id7))
    historycount7 = act_cursor.fetchall()
    global name_and_results7
    name_and_results7 = (str(name7) + " " + str(historycount7))
count_history7()

def count_history8():

    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday,
                                                                                   thisyear, thismonth, thisday, id8))

    historycount8 = act_cursor.fetchall()
    global name_and_results8
    name_and_results8 = (str(name8) + " " + str(historycount8))
count_history8()

def count_history9():
    act_cursor.execute("SELECT COUNT (CREATEDATE) FROM dbo.TBL_HISTORY \
                           WHERE (CREATEDATE BETWEEN'{0}-{1}-{2} 00:00:00' AND \
                           '{3}-{4}-{5} 00:00:00') AND CREATEUSERID='{6}';".format(startyear, startmonth, startday,
                                                                                   thisyear, thismonth, thisday, id9))
    historycount9 = act_cursor.fetchall()
    global name_and_results9
    name_and_results9 = (str(name9) + " " + str(historycount9))
count_history9()





print(x)
