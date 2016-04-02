#connecting to database
import mysql.connector
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='prg04')

try:
   cursor = cnx.cursor()
   cursor.execute("""
      select 3 from reservationsview
   """)
   result = cursor.fetchall()
   print result
finally:
    cnx.close()

cursor = cnx.cursor()


#1. List Reservation
    #Currently in prg04.sql, just does selection from the view ReservationsView
#//end #1



#2. Make a new Reservation

#Should be able to catch potiential problems:
    #Referential integrity errors (non existent rooms or users)
    #Database errors (connection problems, invalid dates, transaction errors)

room = raw_input('Room (building-number)?:') 
date = raw_input('Date (YYYY-MM-DD)?:')
time = raw_input('Time (begin-end)?:') 

roomSQL = "SELECT COUNT(*) FROM ReservationsView WHERE room = " + room
cursor.execute(roomSQL)
result1 = cursor.fetchone()
found1 = result1[0]

dateSQL = "SELECT COUNT(*) FROM ReservationsView WHERE date = " + date
cursor.execute(dateSQL)
result2 = cursor.fetchone()
found2 = result2[0]

timeSQL = "SELECT COUNT(*) FROM ReservationsView WHERE time = " + time
cursor.execute(timeSQL)
result3 = cursor.fetchone()
found3 = result3[0]

if found1 == 0 and found2 == 0 and found3 == 0:
   print("Room available")
   user_id = raw_input('Your ID?:')

   #So we need to just make this into a new entry but I can't connect
   #to sql yet so not sure how to test it. 

else:
   print("Room not available")


#//end #2



#3. Delete a reservation
#Ask user for reservation number

#If reservation exists:
    #Display all the info associated with reservation (room, date, time, user)
    #prompt user to confirm operation
room= raw_input('Room (building-number)?:') #building-number (PPHAC-113)
date= raw_input('Date (YYYY-MM-DD)?:') #(YYYY-MM-DD) (2016-04-01)
time= raw_input('Time (begin-end)?:') #(begin-end) (10-12)


#//end #3



#4. Quit
#//end #4
