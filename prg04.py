#Connect to sql file

#CONNECTING
import mysql.connector
#from mysql.connector import errorcode
#import datetime
#date_time = datetime.strfttime('%a %b %d %H:%M:%S %Y')

cnx = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='prg03')

#ERROR HANDLING
# try:
#   cnx = mysql.connector.connect(user='root@localhost', password='',
#                                 host='127.0.0.1',
#                                 database='prg03')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()

cursor = cnx.cursor()









#1. List Reservation
    #Currently in prg04.sql, just does selection from the view ReservationsView
#//end #1



#2. Make a new Reservation

#Should be able to catch potiential problems:
    #Referential integrity errors (non existent rooms or users)
    #Database errors (connection problems, invalid dates, transaction errors)

#Get User Input
room=eval(input('Room (building-number)?:')) #building-number (PPHAC-113)
date=eval(input('Date (YYYY-MM-DD)?:')) #(YYYY-MM-DD) (2016-04-01)
time=eval(input('Time (begin-end)?:')) #(begin-end) (10-12)

#prints: room, date, and time (PPHAC-113 2016-04-01 10-12)
print(room + date + time)

#Check whether room is available at requested time

#if available ask for user id, then prompt for confirmation
print("Reservation confirmed")

#if not
print("Not available!")



#//end #2



#3. Delete a reservation
#Ask user for reservation number

#If reservation exists:
    #Display all the info associated with reservation (room, date, time, user)
    #prompt user to confirm operation
room=eval(input('Room (building-number)?:')) #building-number (PPHAC-113)
date=eval(input('Date (YYYY-MM-DD)?:')) #(YYYY-MM-DD) (2016-04-01)
time=eval(input('Time (begin-end)?:')) #(begin-end) (10-12)


#//end #3



#4. Quit
#//end #4
