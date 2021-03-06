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
   #print result
finally:
    cnx.close()

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='prg04')

cursor = cnx.cursor()

#Changes based on whether user says yes or no
commit_rollback = True

def commit_rollback_change():
    commit_rollback = False


#1. List Reservation
def list_reservations():
    cursor.execute("SELECT * FROM ReservationsView")
    for response in cursor:
        print(response)
    print("")

#2. Make a new Reservation
#Should be able to catch potiential problems:
def make_reservations():

    #Gets room building and number from user
    valid_room_input = False

    #Loops until correct room is given
    while valid_room_input == False:
        room = raw_input("Room (building-number)?: ")

        if room.__contains__("-") == True:
            room_build = room.split("-")
            #Checks if given building is valid (character wise)
            build = room_build[0]
            #Queries the tables Rooms for value of build
            buildCount = "SELECT COUNT(*) FROM Rooms WHERE build = " + "\"" + build + "\""
            cursor.execute(buildCount)
            buildCountValue = cursor.fetchone()
            foundBuild = buildCountValue[0]
            if foundBuild == 0:
                print "Not a valid room"
            #Goes here if building exists
            else:
                #Checks if given room number is valid (character wise)
                if len(room_build) == 2:
                    if len(room_build[1]) > 0 and len(room_build[0]) > 0:
                        number = room_build[1]
                        numberCount = "SELECT COUNT(*) FROM Rooms WHERE number = " + "\"" + number + "\""
                        cursor.execute(numberCount)
                        numberCountValue = cursor.fetchone()
                        foundNumber = numberCountValue[0]
                        if foundNumber == 0:
                            print "Not a valid room number"
                        #Goes here if buliding and number exists
                        else:
                            valid_room_input = True
                    else:
                        print "Invalid room input"
                else:
                    print "Invalid room input"
        else:
            print "Invalid room input"


    #Gets date from user
    valid_date_input = False

    #Loops until correct date is given
    while valid_date_input == False:
        date = raw_input("Date (YYYY-MM-DD)?: ")

        if len(date) == 10:

            #Should be 8 by end if correct
            correct_digits = 0
            #Should be 2 by end if correct
            correct_hyphens = 0

            for j in range(len(date)):
                if (j != 4 or j != 7) and str.isdigit(date[j]):
                    correct_digits += 1
                elif (j == 4 or j == 7) and date[j] == "-":
                    correct_hyphens += 1
                else:
                    print "Invalid date input"
                    break

            if correct_digits == 8 and correct_hyphens == 2:
                y_m_d = date.split("-")
                year = int(y_m_d[0])
                month = int(y_m_d[1])
                day = int(y_m_d[2])
                #Makes sure years, months, and days are possible
                if year > 0 and 0 < month < 13 and 0 < day < 32:
                    #Handles months with 30 or less days
                    if month == (1 or 9 or 4 or 6 or 2)and day == 31:
                        print "31st does not exist in that month"
                    else:
                        #Handles February
                        if month == 2 and day > 28:
                            if day == 30:
                                print "30th can not exist in February"
                            elif (day == 29 and year%4 == 0) == False:
                                print str(year) + " is not a leapyear, date invalid"
                            else:
                                valid_date_input = True
                        else:
                            valid_date_input = True
                else:
                    print "Invalid date given"

        else:
            print "Invalid date input format"


    #Gets time from user
    valid_time_input = False

    #Loops until correct time is given
    while valid_time_input == False:
        time = raw_input("Time (begin-end)?: ")

        if len(time) == 5:

            #Should be 4 by end if correct
            correct_digits = 0
            #Should be 1 by end if correct
            correct_hyphens = 0

            for i in range(len(time)):
                if i != 2 and str.isdigit(time[i]):
                    correct_digits += 1
                elif i == 2 and time[i] == "-":
                    correct_hyphens += 1
                else:
                    print "Invalid time input"
                    break

            if correct_digits == 4 and correct_hyphens == 1:
                beg_end = time.split("-")
                begin_time = int(beg_end[0])
                end_time = int(beg_end[1])
                if begin_time >= 24 or end_time >= 24:
                    print "Invalid hours given, 00-23 are acceptable hours"
                else:
                    if (begin_time < 23 and begin_time + 1 != end_time) or (begin_time == 23 and end_time != 0):
                        print "Rooms may only be reserved for an hour"
                    else:
                        valid_time_input = True

        else:
            "Invalid length of time input"
    ##END OF WHILE LOOP
    new_time = str(begin_time) + "-" + str(end_time)


    #Prints out requested room, date, & time if all in valid format
    print("Checking if " + room + " is available on " + date + " from " + time + "...")


    #Gets info to check if the room is available
    roomSQL = "SELECT COUNT(*) FROM ReservationsView WHERE room = " + "\"" + room + "\"" + " AND date = " \
              + "\"" + date + "\"" + " AND time = " + "\"" + new_time + "\""
    cursor.execute(roomSQL)
    result1 = cursor.fetchone()
    found1 = result1[0]

    #Confirms if room, date, and time are available
    if found1 == 0:# or found2 == 0 or found3 == 0:
       print("Room available at requested date and time")

       valid_user_id = False

       #Loops until correct ID given
       while valid_user_id == False:
           user_id = raw_input("Your ID?: ")
           user_idSQL = "SELECT COUNT(*) FROM Users WHERE id = " + "\"" + user_id + "\""
           cursor.execute(user_idSQL)
           result4 = cursor.fetchone()
           found4 = result4[0]
           #Goes into here if correct ID is given
           if found4 > 0:
               #maybe something about isolation here
               valid_user_id = True
               loop = True
               while loop: #reply[0] != "y" or reply[0] != "n":#
                   reply = str(raw_input("Confirm reservation" +' (y/n): ')).lower().strip()
                   if reply[0] == 'y':
                       try:
                           loop = False
                           find_seq = "SELECT COUNT(*) FROM Reserved_Rooms"
                           cursor.execute(find_seq)
                           seq = cursor.fetchone()
                           cursor.execute('INSERT INTO Reserved_Rooms VALUES (%s, %s, %s, %s, %s, %s, %s)',(seq[0]+1,date,begin_time,end_time,user_id,build,number))
                           quit_system()
                           print("Room reserved\n")
                       except Exception as e:
                           print "Another user's transaction is in progress, try again later"
                   elif reply[0] == 'n':
                       loop = False
                       commit_rollback_change()
                       quit_system()
                       print("Reservation not made\n")
                   else:
                       loop = True
                       print "Wrong input, type either (y/n)"
           else:
               print("Invalid ID")

    else:
       print("Room not available")
       print("")


#3. Delete a reservation
#Ask user for reservation number
#If reservation exists:
    #Display all the info associated with reservation (room, date, time, user)
    #prompt user to confirm operation
def delete_reservations():
    number = raw_input('Reservation Number?:')

    numberSQL = "SELECT COUNT(*) FROM ReservationsView WHERE number = " + "\"" + number + "\""
    cursor.execute(numberSQL)
    idResult = cursor.fetchone()
    foundID = idResult[0]

    if idResult[0] >= 1:
        room = "SELECT room FROM ReservationsView WHERE number = " + "\"" + number + "\""
        cursor.execute(room)
        result1 = cursor.fetchone()
        found1 = result1[0]

        date = "SELECT date FROM ReservationsView WHERE number = " + "\"" + number + "\""
        cursor.execute(date)
        result2 = cursor.fetchone()
        found2 = result2[0]

        time = "SELECT time FROM ReservationsView WHERE number = " + "\"" + number + "\""
        cursor.execute(time)
        result3 = cursor.fetchone()
        found3 = result3[0]

        user = "SELECT user FROM ReservationsView WHERE number = " + "\"" + number + "\""
        cursor.execute(user)
        result4 = cursor.fetchone()
        found4 = result4[0]

    if foundID > 0:
       #maybe something about isolation here
       print(found1 + " is reserved to " + found4 + " on " + str(found2) + " from " + found3)
       loop2 = True
       while loop2:
           reply = str(raw_input("Confirm deletion of reservation" +' (y/n): ')).lower().strip()
           if reply[0] == 'y':
              try:
                  loop2 = False
                  delete = "Delete FROM Reserved_Rooms WHERE seq = " + "\"" + number + "\""
                  cursor.execute(delete)
                  quit_system()
                  print("Reservation Deleted")
                  print("")
              except Exception as e:
                  print "Another user's transaction is in progress, try again later"
           elif reply[0] == 'n':
              loop2 = False
              commit_rollback_change()
              quit_system()
              print("Reservation not deleted")
              print("")
           else:
               loop2 = True
               print "Wrong input, type either (y/n)"
    else:
       print("Reservation not found")
       print("")


#4.
# Make sure data is committed to the database
def quit_system():
    if commit_rollback:
        cnx.commit()
    else:
        cnx.rollback()


#For the Input System
#is true until Quit() is called
running = True

started = False

#Input System
while running == True:
    print("1. List reservations\n"
          "2. Make a new reservation\n"
          "3. Delete a reservation\n"
          "4. Quit\n"
          )
    user_input = raw_input("Pick an option: ")
    if user_input == "1":
        if not started:
            started = True
            cnx.start_transaction()
            #Calls #2
            list_reservations()
        else:
            list_reservations()
    elif user_input == "2":
        if not started:
            started = True
            cnx.start_transaction()
            #Calls #2
            make_reservations()
        else:
            make_reservations()
    elif user_input == "3":
        if not started:
            started = True
            cnx.start_transaction()
            #Calls #3
            delete_reservations()
        else:
            delete_reservations()
    elif user_input == "4":
        quit_system()
        cursor.close()
        cnx.close()
        running = False
    else:
        print("Invalid input, please give a number from 1 to 4")