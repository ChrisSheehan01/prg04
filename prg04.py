#connecting to database
import mysql.connector
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='prg04')

#Can't get this to work:
try:
   cursor = cnx.cursor()
   cursor.execute("""
      select 3 from reservationsview
   """)
   result = cursor.fetchall()
   #print result
finally:
    cnx.close()

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='prg04')

cursor = cnx.cursor()


#1. List Reservation
#not printing anything, maybe do it in prg04.sql?
def list_reservations():
    cursor.execute("SELECT * FROM ReservationsView")
    for response in cursor:
        print(response)


#2. Make a new Reservation
#Should be able to catch potiential problems:
    #Referential integrity errors (non existent rooms or users)
    #Database errors (connection problems, invalid dates, transaction errors)
def make_reservations():
    #Gets room building and number from user
    room = raw_input("Room (building-number)?: ")
    room_build = room.split("-")

    #Checks if given building is valid
    build = room_build[0]
    buildCount = "SELECT COUNT(*) FROM Rooms WHERE room = " + "\"" + build + "\""
    if buildCount == 0:
        return "Not a valid room!"

    #Checks if given room number is valid
    number = room_build[1]
    numberCount = "SELECT COUNT(*) FROM Rooms WHERE room = " + "\"" + number + "\""
    if numberCount == 0:
        return "Not a valid room number!"



    #Gets date from user
    date = raw_input("Date (YYYY-MM-DD)?: ")


    #Checks if given date is valid
    valid_numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if len(date) == 10:
        for i in date:
            if i !=4 or i !=7:
                if valid_numbers.__contains__(date[i]) == False:
                    return "Date not in valid format"
            else:
                if date[i] != '-':
                    return "Date not in valid format"
    else:
        return "Date not in valid format"


    #Gets time from user
    time = raw_input("Time (begin-end)?: ")



    roomSQL = "SELECT COUNT(*) FROM ReservationsView WHERE room = " + "\"" + room + "\""
    cursor.execute(roomSQL)
    result1 = cursor.fetchone()
    found1 = result1[0]

    dateSQL = "SELECT COUNT(*) FROM ReservationsView WHERE date = " + "\"" + date + "\""
    cursor.execute(dateSQL)
    result2 = cursor.fetchone()
    found2 = result2[0]

    timeSQL = "SELECT COUNT(*) FROM ReservationsView WHERE time = " + "\"" + time + "\""
    cursor.execute(timeSQL)
    result3 = cursor.fetchone()
    found3 = result3[0]

    if found1 == 0 or found2 == 0 or found3 == 0:
       print("Room available")
       user_id = raw_input("Your ID?: ")
       user_idSQL = "SELECT COUNT(*) FROM Users WHERE id = " + "\"" + user_id + "\""
       cursor.execute(user_idSQL)
       result4 = cursor.fetchone()
       found4 = result4[0]
       if found4 > 0:
           print("Room reserved")
           #user name?
           #user_name = "SELECT * FROM Users WHERE id = "
           #beg_time = time[0] + time[1]
           #end_time = time[3] + time[4]
           #str.split(str="-",num=string.count())
           cursor.execute('INSERT INTO Reserved_Rooms VALUES (%s, %s, %s, %s)',(0,date,beg_time,end_time,user_id,room))
           #"""INSERT INTO Reservationsview VALUES (%s,%s,%s)"""
           #cursor.execute('INSERT INTO reservationsview VALUES (Reserved_Rooms_, b_id, %s, %s)',(room,date,time,user_id))
       else:
           print("Not a valid ID")

       #So we need to just make this into a new entry but I can't connect
       #to sql yet so not sure how to test it. So maybe something like this:




    else:
       print("Room not available")

    list_reservations()



#3. Delete a reservation
#Ask user for reservation number
#If reservation exists:
    #Display all the info associated with reservation (room, date, time, user)
    #prompt user to confirm operation
def delete_reservations():
    number = raw_input('Reservation Number?:')

    numberSQL = "SELECT COUNT(*) FROM ReservationsView WHERE number = " + number
    cursor.execute(numberSQL)
    idResult = cursor.fetchone()
    foundID = idResult[0]

    room = "SELECT room FROM ReservationsView WHERE number = " + number
    cursor.execute(room)
    result1 = cursor.fetchone()

    date = "SELECT date FROM ReservationsView WHERE number = " + number
    cursor.execute(date)
    result2 = cursor.fetchone()

    time = "SELECT time FROM ReservationsView WHERE number = " + number
    cursor.execute(time)
    result3 = cursor.fetchone()

    user = "SELECT user FROM ReservationsView WHERE number = " + number
    cursor.execute(user)
    result4 = cursor.fetchone()

    if foundID == 0:
          print(room + "is reserved to " + user + "on " + date + "from " + time)

          #ask for confirmation
          #print according to y or n

    else:
       print("Room not found")




#Calls #1
list_reservations()
#Calls #2
make_reservations()
#Calls #3
delete_reservations()


#4. Quit
# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()
#//end #4

