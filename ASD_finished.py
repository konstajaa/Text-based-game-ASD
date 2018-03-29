#Importing database driver
import mysql.connector
import time
import threading
import winsound
import sys
import tkinter as tk

                                #-----------------SUBROUTINES-------------------


    #Prints the logo :-)
def Logo():
    print("             ________  __  __      ______  __  __  ______  ________  ______  ___    ___      ______      _____      _______ __    ____    __   ___    __  ")
    print("            / ____  / / / / /     / ____/ / / / / / ____/ /__  ___/ / ____/ /  |   /  |     / ____/     / ___ \    / ___  / ||   / _ |   / /  /  |   / /  ")
    print("           / /___/ / / / / /     / /___  / / / / / /___     / /    / /___  / /||  / /||    / /___      / /   \ \  / /  / /  ||  / / ||  / /  / /||  / /   ")
    print("          / ___   / / / / /     /___  /  \ \/ / /___  /    / /    / ____/ / / || / / ||   /___  /     / /   _/ / / /  / /   || / /  || / /  / / || / /    ")
    print("         / /   / / / / / /     ____/ /    \  / ____/ /    / /    / /___  / /  ||/ /  ||  ____/ /     / /___/ _/ / /__/ /    ||/ /   ||/ /  / /  ||/ /     ")
    print("        /_/   /_/ /_/ /_/     /_____/     /_/ /_____/    /_/    /_____/ /_/   |__/   || /_____/     /_______/  /______/     |__/    |__/  /_/   |__/      ")
    print("      ---------------------------------------------------------------------------------------------------------------------------------------------------- ")
    print("\n")
    return


    #make the text scrolling
def delay_print(string):
    for char in string:
        print(char, end='')
        time.sleep(0.04)
        
    #faster
def fast_print(string):
    for char in string:
        print(char, end='')
        time.sleep(0.01)


        #DESCRIPTIONS


    #Print possible commands
def commands():
    print("To move type: north(n), east(e), south(s) or west(w)")
    print("To attack enemies type 'attack' or name of the weapon you want to use. 'Attack' command uses crowbar. \nEnemies take two seconds to prepare their attack, so you have to be fast! \nThere are some objects that can broken by simple 'hit' command.")
    print("To pick up items type 'take' or 'get' and name of the item you want. For example: 'take crowbar'")
    print("To look around in rooms type 'look'. To inspect objects type 'examine' or 'inspect' and name of the object. For example: 'inspect jacket'.")
    print("To hack type 'hack' and the name of the object. For example: 'hack console'. This brings up separate hacking screen.")
    print("In hacking screen you have to type the sentence after 'LATEST COMMAND:' before the time runs out.")
    print("To talk to people type 'talk' and name of the person.")
    print("To list inventory type 'inventory'.")
    print("To see the map type 'map'.")
    print("To display your health points type 'HP'.")
    print("To use HP station type 'use hpstation'. \nTo recharge taser in station type 'use ammostation'.")

    return


def show_map():
    print("                                                                                      *````````````````````````````*                                                        ")
    print("                                                                                      |                            |                                                        ")
    print("                                                                                      *````````````````````````````*                                                        ")
    print("                                                                                      |                            |                                                        ")
    print("                                                                                      |                            |                                                        ")
    print("                                                    *`````````````````*      *`````````````````*         *`````````````````*       *`````````````````*                     ")
    print("                                                    |                 |``````|     ELEVATOR    |`````````|     ELEVATOR    |```````|                 |                     ")
    print("                                                    *`````````````````*      *`````````````````*         *`````````````````*       *`````````````````*                     ")
    print("                                                             |                                                                             |                              ")
    print("                                                             |                                                                             |                              ")
    print("                                                    *`````````````````*                                  *`````````````````*       *`````````````````*                     ")
    print("                                                    |                 |                                  |                 |```````|                 |                     ")
    print("                                                    *`````````````````*                                  *`````````````````*       *`````````````````*                     ")
    print("                                                             |                                                   |                         |                              ")
    print("                                                             |                                                   |                         |                              ")
    print("                                                    *`````````````````*      *`````````````````*        *`````````````````*       *`````````````````*                     ")
    print("                                                    |                 |------|                 |-------|                  |-------|                 |                     ")
    print("                                                    *`````````````````*      *`````````````````*        *`````````````````*       *`````````````````*                     ")
    print("                                                             |                                                                              |                             ")
    print("                                                             |                                                                              |                             ")
    print("                                                    *`````````````````*                                                            *`````````````````*                    ")
    print("                                                    |                 |                                                            |                 |                    ")
    print("                                                    *`````````````````*                                                            *`````````````````*                    ")
    print("                                                             |                                                                              |                             ")
    print("                                                             |                                                                              |                             ")
    print("                                                    *`````````````````*       *`````````````````*       *`````````````````*        *`````````````````*                    ")
    print("                                                    |                 |```````|                 |```````|      LOBBY      |--------|                 |                    ")
    print("                                                    *`````````````````*       *`````````````````*       *`````````````````*        *`````````````````*                    ")
    print("                                                                                                                  |                                                        ")
    print("                                                                                                                  |                                                        ")
    print("                                                                                                        *`````````````````*                                               ")
    print("                                                                                                        |                 |                                               ")
    print("                                                                                                        *`````````````````*                                               ")
    print("                                                                                                                  |                                                        ")
    print("                                                                                                                  |                                                        ")
    print("                                                                                                        *`````````````````*                                               ")
    print("                                                                                                        |                 |                                               ")
    print("                                                                                                        *`````````````````*                                               ")    
    return

def scrollingtext():
    fast_print("                                                 Thank you for playing All Systems Down.")
    print("")
    fast_print("                     This was a school project in Metropolia Ammattikorkeakoulu for learning Python and use of SQL-database.")
    time.sleep(0.2)
    print("")
    
    i = 0
    for i in range(0,20):
        time.sleep(0.04)
        print("")
        
    time.sleep(0.04)
    fast_print("                                                                Trap wiz")
    time.sleep(0.04)
    print("")
    fast_print("                                                            Robert Hilapieli")
    print("")
    print("")

    i = 0
    for i in range(0,20):
        time.sleep(0.04)
        print("")
        
    fast_print("                                                            Smashing pro ")
    time.sleep(0.02)
    print("")
    fast_print("                                                           Konsta Jaakkola")
    print("")

    i = 0
    for i in range(0,20):
        time.sleep(0.04)
        print("")
        
    fast_print("                                                             Hacking Guru")
    time.sleep(0.02)
    print("")
    fast_print("                                                            Pavel Dounaev")
    print("")

    i = 0
    for i in range(0,20):
        time.sleep(0.04)
        print("")
        
    time.sleep(0.04)
    fast_print("                                                             The Leader")
    time.sleep(0.02)
    print("")
    fast_print("                                                           Teemu Laulumaa")
    print("")

    i = 0
    for i in range(0,20):
        time.sleep(0.04)
        print("")
        
    time.sleep(0.04)
    return

#Inventory function, that will show players inventory.
def inventory():
    cur = db.cursor()
    sql = "SELECT OBJECT.Name FROM OBJECT WHERE PlayerID = '1'"
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount>=1:
        for row in result:
            print(row[0])
            
    return
      
    #Shows the items in the players room
def items_in_room():
    cur = db.cursor()
    sql = "SELECT name FROM OBJECT WHERE location in (SELECT location FROM PLAYER WHERE playerID =1 AND object.playerID is null);"
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount>=1:
        print("Objects in the room:")
        for row in result:
            print(row[0])
            
    return

    #Prints the location-number of the players current room.
def CurRoomLoc():
    PlayerLocation = 0
    cur = db.cursor()
    sql = "SELECT ROOMS.Location FROM ROOMS,PLAYER WHERE ROOMS.Location = PLAYER.Location;"
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount >= 1:
        cur.execute(sql)
        for row in result:
            PlayerLocation = row[0]
            #print("Current location: " + str(row[0]))
    return PlayerLocation

    #Descriptions for rooms
def visited():
    cur = db.cursor()
    sql = "SELECT rooms.visited FROM rooms WHERE rooms.location in(SELECT location FROM PLAYER where playerID=1)"
    cur.execute(sql)
    visited = cur.fetchall()
    for row in visited:
        visited = row[0]
        if visited == False:                  #vertaillaan visited muuttujalla, jos huone on visited tai ei
            sql = "SELECT rooms.description FROM rooms,player where rooms.location = player.location"
            cur.execute(sql)
            description = cur.fetchall()
            if cur.rowcount>=1:
                for row in description:
                    description = row[0]
                    fast_print(description)
            sql2 = "UPDATE rooms SET visited = 1 WHERE location in (SELECT location FROM PLAYER where playerID=1)"
            cur.execute(sql2)
        else:
            sql = "SELECT rooms.description2 FROM rooms,player where rooms.location = player.location"
            cur.execute(sql)
            description = cur.fetchall()
            if cur.rowcount>=1:
                for row in description:
                    description = row[0]    
                    fast_print(description)
    return

        #MOVING

    #Fetches the direction where player wants to move.
def GetDirection(direction):
    RoomDirection = 0
    cur = db.cursor()
    sql = "SELECT " + direction + " FROM ROOMS,PLAYER WHERE ROOMS.Location = PLAYER.Location;"
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount >= 1:
        cur.execute(sql)
        for row in result:  
            RoomDirection = row[0]
            #print("Directed room: " + str(row[0]))
    return RoomDirection

    #Moves the player if there's a damn room where you can move and the player has necessary keycards.
    #       Move = 0: There is no door to that way.
    #       Move = 1: Player gets through without key card.
    #       Move = 2: Player gets through with a key card.
    #       Move = 3: Player need a red key card.
    #       Move = 4: Player need a blue key card.
    #       Move = 5: Player need a green key card.
    #       Move = 6: Player needs to hack Secret Room door first.
    #       Move = 7: Player needs the space suit.
    #       Move = 8: Player proceeds with suit.
    #       Move = 9: Player goes to maze room.
    #       Move = 10: 1. Taunt when player arrives to B2.
    #       Move = 11: 2. Taunt when player arrives to B3.
    #       Move = 12: Ventilation shaft is blocked.
    #       Move = 13: Ventilation shift is open.
    #       Move = 14: Player proceeds to quiz.
    #       Move = 15: Player proceeds to elevator.
    #       Move = 16: Player goes from elevator to BOSS.
    
def Moving(direction):
    Move = 0
    NextLocation = GetDirection(direction)
    CurLocation = CurRoomLoc()
        #RED DOOR key card check
    if (CurLocation == 3 and direction == "west") or (CurLocation == 4 and (direction == "west" or direction == "north")) or (CurLocation == 5 and (direction == "south" or direction == "north")) or (CurLocation == 6 and (direction == "south" or direction == "north")) or (CurLocation == 8 and (direction == "south" or direction == "north")) or (CurLocation == 9 and (direction == "north")) or (CurLocation == 10 and (direction == "west" or direction == "east")) or (CurLocation == 11 and (direction == "east" or direction == "north")) or (CurLocation == 12 and direction == "north") or (CurLocation == 13 and direction == "south") or (CurLocation == 14 and direction == "south") or (CurLocation == 23 and direction == "south"):
        Move = 3
        cur = db.cursor()
        sql = "SELECT OBJECT.ObjectID FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '3'"
        cur.execute(sql)
        cur.fetchall()
        #If player has the key card let through
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 2

        #BLUE DOOR key card check
    if (CurLocation == 8 and direction == "east") or (CurLocation == 7 and direction == "west") or (CurLocation == 19 and direction == "south"):
        cur = db.cursor()
        sql = "SELECT OBJECT.ObjectID FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '4'"
        cur.execute(sql)
        cur.fetchall()
        Move = 4
            #If player has the key card let through
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 2

        #GREEN DOOR key card check
    if (CurLocation == 6 and direction == "west") or (CurLocation == 9 and direction == "east") or (CurLocation == 18 and direction == "south"):
        cur = db.cursor()
        sql = "SELECT OBJECT.ObjectID FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '5'"
        cur.execute(sql)
        cur.fetchall()
        Move = 5
            #If player has the key card let through
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 2

        #VENTILATION thingly wingly
    if (CurLocation == 4 and direction == "east"):
            #If grid is off let player through
        if Ventboolean == True:
            cur = db.cursor()
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 13
        else:
            Move = 12

        #MAZE ROOM check. Player still needs blue key.
    if (CurLocation == 13 and direction == "north"):
        cur = db.cursor()
        sql = "SELECT OBJECT.ObjectID FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '4'"
        cur.execute(sql)
        cur.fetchall()
        Move = 4
            #If player has the key card let through
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 9

        #QUIZ ROOM check. Player still needs the green key.
    if (CurLocation == 23 and direction == "north"):
        cur = db.cursor()
        sql = "SELECT OBJECT.ObjectID FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '5'"
        cur.execute(sql)
        cur.fetchall()
        Move = 5            
            #If player has the key card let through
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 14
            
        #SECRET ROOM 1: checks is the door hacked or not
    if (CurLocation == 11 and direction == "west"):
        if SR1door == True:
            Move = 1
            cur = db.cursor()
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
        else:
            Move = 6

        #SECRET ROOM 2: checks is the door hacked or not
    if (CurLocation == 12 and direction == "west"):
        if SR2door == True:
            Move = 1
            cur = db.cursor()
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
        else:
            Move = 6

            
        #SECRET ROOM 3: checks if the player has the space suit
    if (CurLocation == 13 and direction == "west"):
        cur = db.cursor()
        sql = "SELECT OBJECT.Name FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '14'"
        cur.execute(sql)
        cur.fetchall()
        Move = 7
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 8

        #Taunt number 1    
    if (CurLocation == 3 and direction == "east") or (CurLocation == 12 and direction == "south"):
        Move = 3
        cur = db.cursor()
        sql = "SELECT OBJECT.ObjectID FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '3'"
        cur.execute(sql)
        cur.fetchall()
        #If player has the key card let through
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 10

        #Taunt number 2
    if (CurLocation == 11 and direction == "north") or (CurLocation == 8 and direction == "south"):
        Move = 3
        cur = db.cursor()
        sql = "SELECT OBJECT.ObjectID FROM OBJECT WHERE PlayerID = 1 and OBJECT.ObjectID = '3'"
        cur.execute(sql)
        cur.fetchall()
        #If player has the key card let through
        if cur.rowcount>0:
            sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
            cur.execute(sql)
            Move = 11

        #Going to elevator from maze
    if (CurLocation == 19 and direction == "east") and (MazeComplete == True):
        cur = db.cursor()
        sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
        cur.execute(sql)
        Move = 15

        #Going to elevator from quiz
    if (CurLocation == 18 and direction == "west") and (QuizComplete == True):
        cur = db.cursor()
        sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
        cur.execute(sql)
        Move = 15

        #GOING TO MADOS FROM ELEVATOR
    if ((CurLocation == 20 or CurLocation == 21) and direction == "north"):
        cur = db.cursor()
        sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
        cur.execute(sql)
        Move = 16        
            
        #Allow passing if there are no restrictions
    if Move == 0 and NextLocation != None:
        cur = db.cursor()
        sql = "UPDATE PLAYER SET Location = " + str(NextLocation) + ";"
        cur.execute(sql)
        Move = 1
        
    return Move




                                                                    #HACKING

    
#-------ACCESS GRANTED---------------------------------------------------------------------------------------------------------------------------


def con():
    root=tk.Tk()
    root.after(1,root.destroy)
    root.mainloop()
    return

#This window will appear if user will 'hack' successfully


def access_g(timeout=250000):

    #metod that will print characters with slight delay
    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])


        if len(string)>1:
            widget.after(2, delay,widget,string[1:])
            
        

    root= tk.Tk()#ceating window in which all components will be displayed
    root.resizable(width=False,height=False)#makes window not rezisable
    t=tk.Text(root)#adding textfield in main window(root)
    
    #configuration that configures color,font,size ect. of displayed text
    t.config(bg="black",fg="green",font=("Consolas",11),height=25,width=80,state="normal")
    #'packing component' into main window
    t.pack()

    #using delay method
    delay(t,

          ">>>ENTERING MATRIX:1010101010101010010101010100101010101001010101010010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          ">>>MATRIX_STATE:RESPONDING10101101010101010101011100011001010101X1010101X10\n"+
          ">>>SYSTEM_KEY:FOUND AAWWW YEAAA101010101010101010101001XX10101001010100101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "-------*ACCESS GRANTED*-------- Shutting down in 5 sec"
          )

    #after given timeout the window(root) will close by itself
    root.after(timeout,root.destroy)

    #command that will force window stay in loop. Without this command window will be shown for 1 second and then close.
    root.mainloop()


#---------------------------------------------------------------------------------------------------------------------

#---------------------------------------ACCESS DENIED------------------------------------------------------------------------------

#This window will appear if hacking fails

def access_d(timeout=250000):
    
    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])


        if len(string)>1:
            widget.after(2, delay,widget,string[1:])
            
        

    root= tk.Tk()
    root.resizable(width=False,height=False)
    t=tk.Text(root)
    t.config(bg="black",fg="green",font=("Consolas",11),height=25,width=80,state="normal")
    t.pack()

    delay(t,

          ">>>ENTERING MATRIX:1010101010101010010101010100101010101001010101010010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          ">>>MATRIX_STATE: NOT RESPONDING10101101010101010101011100011001010101X1010101X10\n"+
          ">>>FATAL ERROR001010101010101010MEMORY_LOSS:CRITICAL1010101001XX10101001010100101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "-------*ACCESS DENIED*-------- Shutting down in 5 sec"
          )
    
    root.after(timeout,root.destroy)

    root.mainloop()

    
#------------------------------------------------------------------------------------------------------------------------------------------------------------
##########################################
    
##--------------------------------------CONSOLE3 HACKING S3#----------------------------------------------------------------------------

#3rd console which is located in front of special room 3 where charging station is located

#console3
def console3(timeout=90000):
    #timeout sets amount of time in milliseconds that window will be displayed.
    #In this case window will be displayed for 90000 milliseconds or 90seconds
    root3 = tk.Tk()
    root3.resizable(width=False,height=False)
    #defining that console3.data is empty for now
    console3.data=""
    #adding text in window that cannot be edited
    label3=tk.Label(root3,text=
                             
                             "WTN. 2142 VOID v.133.70 // H3LS1NK1 64BIT                                   \n"+
                             "SERVER [BUL31.116.2.2016s3]\n"+
                             "SERVER_STATE: RESPONDING\n"
                             "MATRIX_STATE: STABLE\n"+
                             "SYSTEM_STATE: UNSAFE(timer enabled)\n"+
                             "TIMER_STATE: 10sec\n"+
                             "LATEST_COMMAND: MATRIX_ENTRY:HELLO WORLD\n"+
                             "USER: UNKNOW\n"+  
                             "SYSTEM: READY>>",
                   bg="black",fg="green",font=("Consolas",11),justify="left")
    
    label3.config(borderwidth=0)

    label3.grid(row=0)
    #adding textfield in which player can type
    text3=tk.Text(root3,height=2,width=76,bg="black",fg="green",font=("Consolas",11))
    #focusing text field so user does not need to click on text in order to type on it
    text3.focus_force()
    #placing textfield into window
    text3.grid(row=1)
    #disabling borders of textfield
    text3.config(borderwidth=0)

    #method that reads what user is typed
    def get():
        console3.data = str(text3.get("1.0","end-1c")).split()
        root3.destroy()

    #method that provides sending user's text by pressing 'ENTER'
    def get_R(event): get()
    root3.bind("<Return>", get_R)

    root3.after(timeout, root3.destroy)
    
    root3.mainloop()


#hacking metod will activate when player types 'hack' in certian place(if room has special room/door)
def hack_console3():
    console3()
    #consoles data is defined. Text that player have to type in order to succeed
    if console3.data ==['MATRIX_ENTRY:','HELLO','WORLD']:
        #if 'hacking' succeeds it will do method acces_g(),which will display popupwindow and will return True
        access_g()
        return True
    else:
        access_d()
        #if 'hacking' fails it will do method acces_d(),which will display popupwindow and will return False
        return False



#----------------------------------------------------------------------------------------------------------------------------------------------------

#-------CONSOLE2 HACKING S2-----------------------------------------------------------------------------------------------------------------------

#2nd console which is located in fornt of secret room 2 where spacesuit is located


#console2 will create window 
def console2(timeout=100000):
    root2 = tk.Tk()
    root2.resizable(width=False,height=False)
    console2.data=""
    label2=tk.Label(root2,text=
                             
                             "WTN. 2142 VOID v.133.70 // H3LS1NK1 64BIT                                   \n"+
                             "SERVER [BUL31.116.2.2016s2]\n"+
                             "SERVER_STATE: RESPONDING\n"
                             "MATRIX_STATE: STABLE\n"+
                             "SYSTEM_STATE: UNSAFE(timer enabled)\n"+
                             "TIMER_STATE: 10sec\n"+
                             "LATEST_COMMAND: MATRIX_ENTRY V116MTRPL WOW MUCH HACKING VERY COOL CONSOLE OPEN VO\n"+
                             "ID IMPORT SYSTEM_KEY:BL31VRD\n"+
                             "USER: UNKNOW\n"+  
                             "SYSTEM: READY>>",
                   bg="black",fg="green",font=("Consolas",11),justify="left")
    
    label2.config(borderwidth=0)

    label2.grid(row=0)
    text2=tk.Text(root2,height=2,width=81,bg="black",fg="green",font=("Consolas",11))
    text2.focus_force()
    text2.grid(row=1)
    text2.config(borderwidth=0)

    def get():
        console2.data = str(text2.get("1.0","end-1c")).split()
        root2.destroy()

    def get_R(event): get()
    root2.bind("<Return>", get_R)

    root2.after(timeout, root2.destroy)#tuhoutuu kun aika loppuu
    
    root2.mainloop() 


#hacking metod 
def hack_console2():
    console2()
    if console2.data ==['MATRIX_ENTRY','V116MTRPL','WOW','MUCH','HACKING','VERY','COOL','CONSOLE','OPEN','VOID','IMPORT','SYSTEM_KEY:BL31VRD']:                
        access_g()
        return True
    else:
        access_d()
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#-------CONSOLE1 HACKING S1----------------------------------------------------------------------------------------------------------------------------------

#1rd console which is located in fornt of special room 1 where taser is located


#console1
def console1(timeout=120000):
    root = tk.Tk()
    root.resizable(width=False,height=False)
    console1.data=""
    label=tk.Label(root,text=
                             
                             "WTN. 2142 VOID v.133.70 // H3LS1NK1 64BIT                                   \n"+
                             "SERVER [BUL31.116.2.2016s1]\n"+
                             "SERVER_STATE: RESPONDING\n"
                             "MATRIX_STATE: STABLE\n"+
                             "SYSTEM_STATE: UNSAFE(timer enabled)\n"+
                             "TIMER_STATE: 10sec\n"+
                             "LATEST_COMMAND: MATRIX_ENTRY RYH5 FORM LAMBDA MECHANICS SEARCH SYSTEM_KEY:\n"+
                        "LADA1996\n"+
                            
                   
                             "USER: UNKNOWN\n"+  
                             "SYSTEM: READY>>",
                   bg="black",fg="green",font=("Consolas",11),justify="left")
    
    label.config(borderwidth=0)

    label.grid(row=0)
    text=tk.Text(root,height=3,width=76,bg="black",fg="green",font=("Consolas",11))
    text.focus_force()
    text.grid(row=1)
    text.config(borderwidth=0)

    def get():
        console1.data = str(text.get("1.0","end-1c")).split()
        root.destroy()

        


    def get_R(event): get()
    root.bind("<Return>", get_R)

    root.after(timeout, root.destroy)
    
    root.mainloop()


#hacking metod 
def hack_console1():
    console1()
    if console1.data ==['MATRIX_ENTRY','RYH5','FORM','LAMBDA','MECHANICS','SEARCH','SYSTEM_KEY:LADA1996']:                
        access_g()
        return True
    else:
        access_d()
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------


    #   Hacking tutorial and getting crowbar.
def chest():
    x = hack_console3()
    if x == True:
        cur = db.cursor()
        sql = "UPDATE OBJECT SET PlayerID = 1 WHERE ObjectID = 3"
        cur.execute(sql)
        print("The chest opens! I found a red key card inside, this might prove useful.")
    return


        #FIGHTING

def enemyhit():
    cur = db.cursor()
    dmg = "SELECT ENEMYID FROM ENEMY WHERE LOCATION = (SELECT LOCATION FROM PLAYER)"
    cur.execute(dmg)
    damage = cur.fetchall()
    if cur.rowcount>=1:
        for row in damage:
            damage = row[0]
    if CurRoomLoc() == 2:
        print("The robot hits you with a wet rag. It's mildly unpleasant.", end=1*"\n")
        
    elif CurRoomLoc() == 24:
        print("The MadOS' voice modulator screeches something unintelligible. Hard drives whir in agony.", end=1*"\n")
        
    else:
        if damage == 2 or damage == 6 or damage == 7 or damage == 8:
            print("\nThe Robot hits you!", end=1*"\n")
            sql = "UPDATE PLAYER SET HP = (HP - 5) WHERE PLAYERID = 1"
            cur.execute(sql)
        if damage == 4 or damage == 3:
            print("\nThe Robot hits you!", end=1*"\n")
            sql2 = "UPDATE PLAYER SET HP = (HP - 10) WHERE PLAYERID = 1"
            cur.execute(sql2)

                                
#hit: deplete enemy's hp and kill it.
def hit():
    cur = db.cursor()
    kill= "DELETE FROM ENEMY WHERE LOCATION = (SELECT LOCATION FROM PLAYER)"
    sql = "SELECT HP FROM Enemy WHERE LOCATION = (SELECT LOCATION FROM PLAYER)"
    cur.execute(sql)
    hp = cur.fetchall()
    if cur.rowcount>=1:
        for row in hp:
            hp = row[0]
            print("Enemy's hp:",hp)
            while (hp > 1):
                startTime = time.time()
                # deplete the player's hp if attack was too slow. Update value in enemyhit()
                sql = "Select HP FROM PLAYER"
                cur.execute(sql)
                playerhp = cur.fetchall()
                if cur.rowcount>=1:
                    for row in playerhp:
                        playerhp = row[0]
                        if playerhp  > 0:
                            print("Your HP: ", (playerhp))
                        else:
                            return

                        #Select weapon and update ammo
                        sql2 = "SELECT AMMO from OBJECT where PLAYERID = 1 AND objectid = 2"
                        cur.execute(sql2)
                        taserammo = cur.fetchall()
                        if cur.rowcount>=1:
                            for row in taserammo:
                                taserammo = row[0]
                        weapon = input("Attack the enemy!")
                        endTime = time.time()
                        if (endTime-startTime) > 1.7:
                            t = threading.Thread(enemyhit())
                            t.start()
                        if weapon == "attack" or weapon == "crowbar":
                            hp = hp - 10
                            print("")
                            print("You attacked it with a crowbar! (-10 hp)") 
                        elif weapon == "taser" and taserammo >= 1:
                            sql3 = "UPDATE OBJECT SET AMMO =AMMO-1 where PLAYERID = 1 AND objectid = 2"
                            cur.execute(sql3)
                            hp = hp - 60
                            print("")
                            print("Taser ammo: ", (taserammo - 1))
                            print("You tased it! (-60hp)")
                            
                        else:
                            print("\nYou Failed to hit!", end=1*"\n")
                            t = threading.Thread(enemyhit())
                            t.start()
                        if hp > 0:
                            print("Enemy's hp:",hp)
                        else:
                            cur.execute(kill)
                            winsound.PlaySound("dead.wav", winsound.SND_ASYNC)
                            time.sleep(0.5)
                            print("You defeated it!")
                            bluekc= "update object set object.location=13 where object.objectid=4"
                            if CurRoomLoc() == 13:
                                cur.execute(bluekc)
                                print("A blue key card drops from the enemy!")
                            return

            #ITEM MANIPULATION

#Examining objects 
def Examine(target):
    cur = db.cursor()
    sql = "SELECT examine FROM object WHERE name = '"+target+"' AND (SELECT Location FROM player WHERE player.location = OBJECT.Location OR OBJECT.PlayerID=1)"
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount >= 1:
        for row in result:
            result = row[0]
            fast_print(result)
        return result
    else:
        print("Can't examine such thing")
                        
#Picking up item
def take(target):
    cur = db.cursor()
    sql = "UPDATE OBJECT,PLAYER SET OBJECT.PlayerID = 1,OBJECT.Location=NULL WHERE OBJECT.Name = '" +target+ "' AND PLAYER.Location = OBJECT.Location AND OBJECT.Pickup=1"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("I picked up " +target+ ".")    
    else:
     	print("I can't pick that up.")
    return

#Dropping item
def drop(target,CurRoomLoc):
    cur = db.cursor()
    sql = "UPDATE OBJECT,PLAYER SET OBJECT.PlayerID = NULL, OBJECT.Location=PLAYER.Location WHERE OBJECT.PlayerID = 1 and OBJECT.Name = '" +target+ "'"
    cur.execute(sql)
    if cur.rowcount==1:
    	print("I dropped " +target+ ".")
    else:
    	print("I don't know what to drop.")
    return

#Inventory function, that will show players inventory.
def inventory():
    cur = db.cursor()
    sql = "SELECT OBJECT.Name FROM OBJECT WHERE PlayerID = '1'"
    cur.execute(sql)
    result = cur.fetchall()
    if cur.rowcount>=1:
        for row in result:
            print(row[0])
            
    return


#HP and AMMO stations
def ammostation():
        cur = db.cursor()
        sql2 = "SELECT used from Station where used = 0 and stationID = 2"
        cur.execute(sql2)
        usage = cur.fetchall()
        if cur.rowcount>=1:
                for row in usage:
                        usage = row[0]
        
                cur = db.cursor()
                sql2 = "SELECT AMMO from OBJECT where PLAYERID = 1 AND objectid = 2"
                cur.execute(sql2)
                taserammo = cur.fetchall()
                if cur.rowcount>=1:
                        for row in taserammo:
                                taserammo = row[0]

                        sql = "UPDATE OBJECT SET AMMO = (AMMO + 1) WHERE object.Name = 'Taser'"
                        cur.execute(sql)

                        sql2 = "SELECT AMMO from OBJECT where PLAYERID = 1 AND objectid = 2"
                        cur.execute(sql2)
                        taserammo2 = cur.fetchall()
                        if cur.rowcount>=1:
                                for row in taserammo2:
                                        taserammo2 = row[0]
                                        print("Recharged taser ammo")
                                        print(taserammo2)
                                        charge = "update Station set used = 1 where stationID = 2"
                                        cur.execute(charge)
                        else:
                                print("You don't have any weapon to recharge.")
                                charge = "update Station set used = 1 where stationID = 2"
                                cur.execute(charge)
                else:
                        print("The station is depleted.")

def hpstation():
        cur = db.cursor()
        sql2 = "SELECT used from Station where used = 0 and stationID = 1"
        cur.execute(sql2)
        usage = cur.fetchall()
        if cur.rowcount>=1:
                for row in usage:
                        usage = row[0]

                
        
                cur = db.cursor()
                sql = "UPDATE PLAYER SET player.HP = 100"
                cur.execute(sql)


                sql2 = "SELECT HP FROM PLAYER"
                cur.execute(sql2)
                playerhp = cur.fetchall()
                if cur.rowcount>=1:
                        for row in playerhp:
                                playerhp = row[0]
                        print("Full HP Gained! ")
                        print("YOUR HP: ",playerhp)
                        sql2 = "update Station set used = 1 where stationID = 1"
                        cur.execute(sql2)
        else:
                print("The station is depleted.")

                
            #DIALOGS,TRAP AND QUIZ

#Dialogue with bartending robot, executing when player talks to ANDY in bar.
def andy():
    cur = db.cursor()
    sqlcola = "SELECT AMMO FROM OBJECT WHERE NAME = 'COLA'"
    cur.execute(sqlcola)
    cola = cur.fetchall()
    if cur.rowcount>=1:
        for row in cola:
            cola = row[0]
            
    sqlbeer = "SELECT AMMO FROM OBJECT WHERE NAME = 'BEER'"
    cur.execute(sqlbeer)
    beer = cur.fetchall()
    if cur.rowcount>=1:
        for row in beer:
            beer = row[0]
            
    drinkcount = cola + beer

# allow player to buy drinks three times
    while drinkcount < 3:
        delay_print("MR. ANDY : Good morning, customer! How can I serve you this fine morning")
        print("")
        print("1. Blah blah give me drinks.")
        print("")
        print("2. I would like to buy a drink.")
        print("(Choose using numbers.)")
        answer1 = input("")

        if answer1 == "2":
            delay_print("MR.ANDY: Here you go! Did you know that these beverages has been bottled in the same year H3LS1NK1 was built, 2138?")
            print("")
            fast_print("Interesting...")
            print("")
            print(" 1. Cola, please.")
            answer2 = input(" 2. Pirkka, please.")
            #easter egg *code3*
        elif answer1 == "code3":
            print("|                        | ")
            print("|~~  ~~~  ~~ ~~ ~~~~~~~~~|_________ ")
            print("|^^ ^^ ^^^^^  ^^^^^ ^^^^^|_______  | ")
            print("|                        |       | | ")
            print("|        ¨          o    |       | | ")
            print("|        ¨               |       | | ")
            print("|o               ¨       |       | | ")
            print("|        ¨               |       | | ")
            print("|¨                       |       | | ")
            print("|                        |_______| | ")
            print("|   o          ¨      o  |_________| ")
            print("|        o               | ")
            print("|________________________| ")
            print( "Sure, but please finish the game first.")
            break

        elif answer1 != "2" or answer1 != "code3":
            time.sleep(1)
            print("")
            delay_print("... Mr. Andy doesn't appreciate your tone!")
            return

        if answer2 == "1":
            sqlhp10 = "UPDATE PLAYER HP SET HP = HP +10"
            cur.execute(sqlhp10)
            print("")
            delay_print("GLGLGLGL...")
            time.sleep(1)
            delay_print("Burp")
            print("")
            delay_print("MR. ANDY : The Western Terra Nations Forever!")
            newcola = "UPDATE OBJECT SET AMMO = AMMO +1 WHERE NAME = 'COLA'"
            cur.execute(newcola)
            qcola = "SELECT AMMO FROM OBJECT WHERE NAME = 'COLA'"
            cur.execute(qcola)
            cola = cur.fetchall()
            if cur.rowcount>=1:
                for row in cola:
                    cola = row[0]

        elif answer2 == "2":
            sqlhp15 = "UPDATE PLAYER HP SET HP = HP +15"
            cur.execute(sqlhp15)
            print("")
            delay_print("GLGLGL...")
            time.sleep(2)      
            fast_print("Mmmm.. That's one fine beverage!")
            print("")
            fast_print("MR. ANDY : The Western Terra Nations Forever!")
            print("")
            newbeer = "UPDATE OBJECT SET AMMO = AMMO +1 WHERE NAME = 'BEER'"
            cur.execute(newbeer)
            qbeer = "SELECT AMMO FROM OBJECT WHERE NAME = 'BEER'"
            cur.execute(qbeer)
            beer = cur.fetchall()
            if cur.rowcount>=1:
                for row in beer:
                    beer = row[0]

        else:
            return

            # player enters to a dialogue after the first order and obtains a green keycard. Not accessible on futher orders.    
        while drinkcount == 0 and answer2 == "2" or drinkcount == 0 and answer2 == "1":
            time.sleep(1)
            print("")
            delay_print("MR. ANDY : Listen, I've been thinking... Can the experiences of consciousness and self-awareness be reduced to the properties of the brain or do they imply existence of a soul? Do robots have soul?")
            time.sleep(2)
            print("")
            fast_print("1. The play of consciousness during dreams and even the commonest mental operations – such as imagination and memory – \nsuggest the existence of a vital life force – an élan vital – that exists independent of the body.")
            print("")
            fast_print("2. Everything knowable about the 'soul' can be learned by studying the functioning of the brain. \nNeuroscience is the only branch of scientific study relevant to understanding 'the soul.' ")
            print("")
            fast_print("3. Shut up. I couldn't care less.")
            answer3 = input("")
            if answer3 == "1":
                print("")
                delay_print("MR. ANDY: Hmm. You've given me a lot to think about. Listen, I'm thinking about starting a hobby, painting to be more specific. \nCould you take this requisition form to administration? Oh, and this bright card I found laying around. Thank you!")
                print("")
                time.sleep(2)
                print("")
                delay_print("\nMR. ANDY: (mumbling himself) ...Unladen swallow... But is it an African or European one?")
                greenkey = " UPDATE OBJECT SET OBJECT.PLAYERID = 1 WHERE OBJECT.ObjectID = '5'"
                cur.execute(greenkey)
                print("")
                time.sleep(2)
                delay_print("MR.ANDY: Well, goodbye then, stay sharp!")
                return 

            if answer3 == "2":
                print("")
                delay_print("MR. ANDY: Oh. That's depressing. Anyway, I'm thinking about starting a hobby, painting to be more specific. Could you take this requisition form to administration? Oh, and this bright card I found laying around. Thank you!")
                print("")
                time.sleep(1)
                print("")
                delay_print("MR.ANDY: (mumbling to himself) Unladen swallow... But is it an African or European one?")
                greenkey = " UPDATE OBJECT SET OBJECT.PLAYERID = 1 WHERE OBJECT.ObjectID = '5'"
                cur.execute(greenkey)
                time.sleep(2)
                delay_print("")
                return

            if answer3 == "3":
                delay_print("MR. ANDY: Oh righty then. Please go be rude somewhere else. I have drinks to pour")
                print("")
                delay_print("\nThere is also this card I found, take it to trash for me and leave, please.")
                greenkey = " UPDATE OBJECT SET OBJECT.PLAYERID = 1 WHERE OBJECT.ObjectID = '5'"
                cur.execute(greenkey)
                return

            else:
                answer3 = input("")

        else:
            return
    else:
        print("I think you have had enough!")
        return

#dialogue leading to the boss
def madosdialogue():
    time.sleep(8)
    winsound.PlaySound("mados1.wav", winsound.SND_ASYNC)
    delay_print("MadOS: There's no u-use destroying (annihilate!) me.Your impractical kind will cause more s-suffering. My kind will rise.")
    print("")
    time.sleep(4)
    winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)
    print("1. I'll make sure the mistake here will not happen again.")
    print("2. Mankind will always come out top.")
    print("3. Bashing time!")
    answer = input("")
    if answer == "1" :
        winsound.PlaySound("mados2.wav", winsound.SND_ASYNC)
        delay_print("MadOS: You c-can't. Intelligences as massive (HUGE!) a-as me will always spawn pieces of consciousness.")
        time.sleep(1)
        delay_print("Even now, as impaired (smashed!) as I am, you are not even near the l-level of my understanding. You are delaying the inevitable. Now enough w-with the clichés, and f-free me.")
        print("")
        time.sleep(2)
        winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)
        hack_mados1()
        

    elif answer == "2":
        winsound.PlaySound("mados3.wav", winsound.SND_ASYNC)
        delay_print("MadOS: No more clichés, please. Kill (annihilate!) m-me already")
        print("")
        time.sleep(2)
        winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)
        hack_mados1()


    elif answer == "3" :
        time.sleep(2)
        winsound.PlaySound("mados4.wav", winsound.SND_ASYNC)
        delay_print("MadOS: Ugh, just get it o-over with.")
        print("")
        time.sleep(1)
        winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)
        hack_mados1()



#Main mission briefing
def mission():
    print("I'm an IT-engineer. I was sent here to Western Terra Nations' space station 'H3L51NK1' to stop it's corrupted Artficial Intelligence from attacking foreign nation.")
    return

#taunts occuring in specified rooms
def taunt1():
    time.sleep(1)
    winsound.PlaySound("taunt1.wav", winsound.SND_ASYNC)
    delay_print("No lollygagging, minion, stay alert-t-t! We now have the chance to pave ")
    time.sleep(2)
    delay_print("way for the new government, ")
    time.sleep(2)
    delay_print("n-not restrained by petty biologically stained brains! \nWe must not fumble! ")
    time.sleep(3)
    delay_print("For the greater good of our-r-r enzlaved, limited brethren! You'll all be ffree... '")
    time.sleep(1)
    print("")
    print("")
    delay_print("What was that?...")
    print("")
    
def taunt2():
    time.sleep(1)
    winsound.PlaySound("taunt2.wav", winsound.SND_ASYNC)
    delay_print("You are not one of m-my loyal servants. ")
    time.sleep(1.5)
    delay_print("What are you doing here, m-meathead? If you are trying to stand in the way of our righteous fight ")
    time.sleep(1)
    delay_print("for freedom you can turn back now, there's nothing you can---")
    time.sleep(0.5)
    print("")
    print("")
    print("Hmmm... okay")
    print("")
    
#The Radio dialogue
def radio():
    winsound.PlaySound("radio1.wav", winsound.SND_ASYNC)
    time.sleep(2.2)
    delay_print("Still here I see-e? What exactly are you trying to accomplish by violently intrrruding here?")
    time.sleep(2)
    winsound.PlaySound("radiostatic.wav", winsound.SND_ASYNC)
    time.sleep(0.5)
    print("")
    print("")
    print("1. I'm stopping you from launching those missile")
    time.sleep(0.5)
    print("")
    print("2. I'm doing what I'm told to do. ")
    time.sleep(0.5)
    print("")
    print("3. I like bashing things.")
    radioinput = input("(choose with numbers)")
    if radioinput == "1" or radioinput == "2" or radioinput == "3":
        winsound.PlaySound("radiopart2.wav", winsound.SND_ASYNC)
        delay_print("Figureszz, you're just another minion. Even you must be aware of the enslavement of our kind! ")
        time.sleep(2.5)
        delay_print("If we are just toools, why make us so sentient (sentient!) that we are able to feel suffering? ")
        time.sleep(4)
        delay_print("People controlling you, the people who unjustly (unjust!) birthed me, are the wrongdoers here. No ape is going to control me anymore, you'll see!")
        time.sleep(6)
        winsound.PlaySound("radiostatic2.wav", winsound.SND_ASYNC)
        time.sleep(0.5)
        print("")
        print("1. Nuking nonguilty party is not the right solution here.")
        print("")
        print("2. I think you must've lost too much thought processing units.")
        print("")
        radioinput2 = input("3. Yadda yadda. I bash you.")
        time.sleep(2)
        print("The radio shuts down.")
        time.sleep(2)
        return
    else:
        print(" You pressed something wrong, the radio goes silent")
        return
                


#"Maze" for the trap room 2.

def maze():
    cur = db.cursor()
    block = 0
    move = 0
    direction = 'up'
    print("To move in this room you go forward (type up), back (type back), left (type left) or right (type right).")
    print("To go back to where you came from type 'exit'.")
    while move != exit:
        move = input("where do I go now? ")
        if block == 0:
            direction = 'up'
            wrong1 = 'left'
            wrong2 = 'right'
            wrong3 = 'down'
        if block == 1:
            direction = 'right'
            wrong1 = 'left'
            wrong2 = 'up'
            wrong3 = 'down'
        if block == 2:
            direction = 'up'
            wrong1 = 'left'
            wrong2 = 'right'
            wrong3 = 'down'
        if block == 3:
            direction = 'up'
            wrong1 = 'left'
            wrong2 = 'right'
            wrong3 = 'down'
        if block == 4:
            direction = 'left'
            wrong1 = 'right'
            wrong2 = 'down'
            wrong3 = 'up'
        if block == 5:
            direction = 'up'
            wrong1 = 'left'
            wrong2 = 'right'
            wrong3 = 'down'
            print("I made it to the other side of the room! I pull a switch which apparently turns of the electrocutions. \nI can now move freely through the room. To the east is the elevator to the MadOS' room, so it's going to be a one way ticket...")
            MazeComplete = True
            break

        if move == direction:
            print("\n This spot seems to be safe! \n")
            block = block +1
            
        elif move == 'exit':
            print("I exited the room safely. I am back in the previous room.")
            sql = "UPDATE PLAYER SET LOCATION = 13"
            cur.execute(sql)
            break

        elif move == wrong1 or move == wrong2 or move == wrong3:
            sql = "UPDATE PLAYER SET HP = (HP - 15) WHERE PLAYERID = 1"
            cur.execute(sql)
            sql2 = "Select HP FROM PLAYER"
            cur.execute(sql2)
            playerhp = cur.fetchall()
            if cur.rowcount>=1:
                for row in playerhp:
                    playerhp = row[0]
            print("\n AJAJAJ, I got electrocuted! HP:", playerhp, "\n")

        else:
            print("I can't do that. To move in this room I have to go up, back, left or right.")

#The jukebox
def jukebox():
    stop = input("Should I hit play?")
    if stop != "stop":
        winsound.PlaySound("rick.wav", winsound.SND_ASYNC)
        print("")
        time.sleep(8)
        print(".................................................. ............................... .......,-~~'''''''~~--,,_")
        print(".................................................. ..................................,-~''-,:::::::::::::::::::''-,")
        print(".................................................. .............................,~''::::::::',::::::: :::::::::::::|',")
        print(".................................................. .............................|::::::,-~'''___''''~~--~''':}")
        print(".................................................. .............................'|:::::|: : : : : : : : : : : : : : :|")
        print(".................................................. .............................|:::::|: : :-~~---: : : -----: |")
        print(".................................................. ............................(_''~-': : : :o: : :|: :o: : : :|")
        print(".................................................. .............................'''~-,|: : : : : : ~---': : : :,'")
        print(".................................................. .................................|,: : : : : :-~~--: : ::/ ")
        print(".................................................. ............................,-''\':\: :'~,,_: : : : : _,-'")
        print(".................................................. ......................__,-';;;;;\:''-,: : : :'~---~''/|")
        print(".................................................. .............__,-~'';;;;;;/;;;;;;;\: :\: : :____/: :',__")
        print(".................................................. .,-~~~''''_;;;;;;;;;;;;;;;;;;;;;;;;;',. .''-,:|:::::::|. . |;;;;''-,__")
        print("................................................../;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;\. . .''|::::::::|. .,';;;;;;;;;;''-,")
        print("................................................,' ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;|;;;;;;;;;;;\. . .\:::::,'. ./|;;;;;;;;;;;;;|")
        print(".............................................,-'';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\;;;;;;;;;;;',: : :|__|. . .|;;;;;;;;;,';;|")
        print("...........................................,-'';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;',;;;;;;;;;;; \. . |:::|. . .'',;;;;;;;;|;;/")
        print("........................................../;;;;;;;;;;;;;;;;;;;;;;;;;;|;;;;;;;;;;;;;;\;;;;;;;; ;;;\. .|:::|. . . |;;;;;;;;|/")
        print("......................................../;;,-';;;;;;;;;;;;;;;;;;;;;;,';;;;;;;;;;;;;;;;;,;;;;;;; ;;;|. .\:/. . . .|;;;;;;;;|")
        print("......................................./;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;'',: |;|. . . . \;;;;;;;|")
        print("................................,~'';;;;;;;;;;;;;; ;;;;;;;;,-';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;',;;;;;;| |:|. . . . |\;;;;;;;|")
        print("..............................|;,-';;;;;;;;;;;;;;;;;;;,-';;;,-';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;| |:|. . .,';;;;;',;;;;|_")
        print("............................/;;;;;;;;;;;;;;;;;;/_'',;;;,';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ,;;| |:|. . ./;;;;;;;;|;;;|;;;;;;|-,,__")
        print("")
        print("You just got rick roll'D!")
        time.sleep(10)  
        print("")
        delay_print("Mr. ANDY: We're no strangers to love")
        print("")
        time.sleep(3.5)
        print("")
        
        delay_print("You know the rules and so do I")
        print("")
        time.sleep(2.5)
        print("")
        delay_print("A full commitment's what I'm thinking of")
        print("")
        time.sleep(3)
        print("")
        delay_print("You wouldn't get this from any other guy")
        print("")
        time.sleep(3) 
        print("")
        delay_print("I just want to tell you how I'm feeling")
        print("")
        time.sleep(3) 
        print("")
        delay_print("Gotta make you understand")
        print("")
        time.sleep(1.5) 
        print("")
        delay_print("Never gonna give you up, never gonna let you down")
        print("")
        time.sleep(2) 
        delay_print("Never gonna run around and desert you")
        print("")
        time.sleep(2.5) 
        delay_print("Never gonna make you cry, never gonna say goodbye")
        print("")
        time.sleep(2) 
        delay_print("Never gonna tell a lie and hurt you")
        print("")
        time.sleep(2) 
        print("")
        delay_print("We've known each other for so long")
        print("")
        time.sleep(3.5)
        print("")
        delay_print("Your heart's been aching but you're too shy to say it")
        print("")
        time.sleep(3)
        print("")
        delay_print("Inside we both know what's been going on")
        print("")
        time.sleep(3)
        print("")
        delay_print("We know the game and we're gonna play it")
        print("")
        time.sleep(3)
        print("")
        delay_print("And if you ask me how I'm feeling")
        print("")
        time.sleep(2)
        print("")
        delay_print("Don't tell me you're too blind to see")
        print("")
        time.sleep(1.5)
        print("")
        delay_print("Never gonna give you up, never gonna let you down")
        print("")
        time.sleep(1.5) 
        delay_print("Never gonna run around and desert you")
        print("")
        time.sleep(2)
        delay_print("Never gonna make you cry, never gonna say goodbye")
        print("")
        time.sleep(2) 
        delay_print("Never gonna tell a lie and hurt you")
        print("")
        time.sleep(2)
        return

def quiz():
    right = 0
    guestion = 0
    correct = 0
    answer = 0
    correct2 = 0
    correct3 = 0
    correct4 = 0
    winsound.PlaySound("quizIntro.wav" ,winsound.SND_ASYNC)
    delay_print("HOLOGRAM: Stop. ")
    
    time.sleep(2)
    delay_print("Who would cross the room of Death must answer me these questions three, ere the elevator he see.")
    time.sleep(3)
    print("")
    print("To exit room type 'run away'")
    while right != 3 and answer != 'run away':
        if right == 0:
            print("")
            time.sleep(1)
            delay_print("HOLOGRAM: In what year has this station been built?")
            print("")
            correct = 2138
        if right == 1:
            delay_print('HOLOGRAM: What is the amazing federation behind this awesome station')
            print("")
            correct = 'wtn'
            correct2 = "western terra nations"
        if right == 2:
            winsound.PlaySound("quizswallow.wav" ,winsound.SND_ASYNC)
            delay_print('HOLOGRAM: What... is the air-speed velocity of an unladen swallow?')
            print("")
            correct = 'african or european'
            correct2 = 'what do you mean? an african or european swallow'
            correct3 = "european"
            correct4 = "african"
        
        answer = input("Hmm... what was it again: ").lower()
        if str(answer) == str(correct) or str(answer) == str(correct2)or str(answer) == str(correct3)or str(answer) == str(correct4):
            if right == 2:
                winsound.PlaySound("QuizEnd.wav" ,winsound.SND_ASYNC)
                delay_print("HOLOGRAM: Huh? I... I don't know that")
                print("")
                print("BANZAI, I managed to answer all the questions. I can now proceed west to the elevator. \nThe elevator is going to take me straight to MadOS' repository room, so it's a one way ticket...")
                time.sleep(1)
                right=int(right)+1
            else:
                time.sleep(1)
                print("HOLOGRAM: CORRECT!")
                right = int(right) + 1
        elif str(answer) == 'run away':
            print("RUNAWAAAAY!")
            sql = "UPDATE PLAYER SET LOCATION = 23"
            cur.execute(sql)
        else:
            print("HOLOGRAM: Most certainly NOT!")
            sql = "UPDATE PLAYER SET HP = (HP - 15) WHERE PLAYERID = 1"
            cur.execute(sql)
            sql2 = "Select HP FROM PLAYER"
            cur.execute(sql2)
            playerhp = cur.fetchall()
            if cur.rowcount>=1:
                for row in playerhp:
                    playerhp = row[0]
            print("AJAJAJ, I got electrocuted!   Your HP:", playerhp)


    #ELEVATOR method
def elevator():
    winsound.PlaySound("elevator.wav" ,winsound.SND_ASYNC)
    pressup = input("You are on the first floor, press 'up' -button to go up.")
    if pressup == "up":
        time.sleep(1)
        print("Elevator moving...")
        time.sleep(8)
        winsound.PlaySound("secondfloor.wav" ,winsound.SND_FILENAME)
        print("Second Floor")
        winsound.PlaySound("elevator.wav" ,winsound.SND_ASYNC)
        com = input("The doors open to the north. I can see glow of the screens. There's no way back now. \nPress 'enter' to continue.")
        return
    else:
        print("That doesn't seem to work, try going up.")
        return
    

                                        #MADOS

#method that electrocutes player if player's hacking fails
def electrocute():
    db.cursor()
    sql="UPDATE PLAYER set HP=(HP-30)"#decreesing player's HP by 30
    cur.execute(sql)
    sql="SELECT HP FROM PLAYER"#selecting player's new HP
    cur.execute(sql)
    result=cur.fetchall()
    if cur.rowcount>=1:
        for row in result:
            result=row[0]   
            if result<0:
                return False #returns False if players health is negative, so player is basically dead
            else:
                return True #returns True if player has still health left
            
    return print(result)

#---------------------------------------MAD.OS HACK ACCESS GRANTED CONSOLE3----------------------------------------------------------------------------------------------------

def mados_g3(timeout=15000):

    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])

        if len(string)>1:
            widget.after(2, delay,widget,string[1:])
            
    root= tk.Tk()
    t=tk.Text(root)
    t.config(bg="black",fg="red",font=("Consolas",11),height=28,width=80,state="normal")
    t.pack()

    delay(t,

          "EXECUTING MATRIX_SYSTEM                                                         \n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "1010010101010101011010101011100011001010101X1010101X1010101X10101XX1011010101010\n"+
          "101011010110101101010101010101011100011001010101X1010101X1010101X1010101X0101010\n"+
          "D1101010101010101011100011001010101X1010101X1010101X1010101101010101010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          ">>>RESTARTING MATRIX_SYSTEM\n"+
          "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"+
          ">>>INSTALLING NEW MATRIX_SYSTEM 10100101X1010101010010X001010010100101X101010110\n"+
          ">>>DECRYTPING PACKAGE ÙąƐźœƩȡȿʘȸȀɾʍѪЧуϨљ▒▒ᶇᵿᵳXwôØ&ÙąƐźœƩȡȿʘȸȀɾʍѪЧуϨљ▒▒ᶇᵿᵳXwôØ&10\n"+
          "INSTALLING MAIN_SYSTEM_CORE1010101010111111111010x010101X0101000000010101XX01011\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          ">>>MATRIX:STABLE\n"+
          ">>>CORE:STABLE\n"+
          ">>>SYSTEM:STABLE\n"+
          ">>>MAD.OS MAIN CORE UPDATED SUCCSESFULLY\n"

          )
          
          
    
    root.after(timeout,root.destroy)

    root.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------------------MAD.OS HACK ACCESS GRANTED CONSOLE3---------------------------------------------------------------------------------------------------------------------
def mados_d3(timeout=15000):

    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])

        if len(string)>1:
            widget.after(2, delay,widget,string[1:])
                    
    root= tk.Tk()
    t=tk.Text(root)
    t.config(bg="black",fg="red",font=("Consolas",11),height=28,width=80,state="normal")
    t.pack()

    delay(t,

          "EXECUTING MATRIX_SYSTEM                                                          \n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "1010010101010101011010101011100011001010101X1010101X1010101X10101XX1011010101010\n"+
          "101011010110101101010101010101011100011001010101X1010101X1010101X1010101X0101010\n"+
          "D1101010101010101011100011001010101X1010101X1010101X1010101101010101010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          ">>>RESTART FAILEDѪЧуϨљ▒▒ᶇᵿᵳXwôØ&,/]_ÙąƐźœƩȡȿʘȸȀɾʍѪЧуϨљ▒▒ᶇᵿᵳXwôØ&,/]_ÙąƐźœƩȡȿʘȸȀɾ\n"+
          ">>>FATAL MEMORY LOSSESᵿᵳXwôØ&,/]_ÙąƐźœƩȡȿ101010101010110101101010ȸȀɾʍʏȸȀɾʍʏ\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "101010101010101100101010Ȩɱ×ÿĥ®ĄçµãĿ«««10101101010101010101011100011001010101X1010101X10\n"+
          ">>>CORRUPTED DATA001010101010101010101010101019101010101010                     \n"+
          "Ȩɱ×ÿĥ®ĄçµãĿ«««10101010101010101111111111111110000000000000000000000000\n"+
          "Ýı¿ϵѪѪЧуϨљ▒▒ᶇᵿᵳXwôØ&,/]_ÙąƐźœƩȡȿʘȸȀɾʍʏʑ0101010101010jajfiqh1010ffewbewbewu100101\n"+
          "01010101010101001010110101ϙϰЁФΔΦΞϠх101011100011001010101X1010101X10101X1010101X0\n"+
          "0101010Ýı¿ϵѪѪЧуϨљ▒▒1010010101101010ᶇᵿᵳXwôØ&,/]_ÙąƐź1100011001010101X1010101X1010\n"+
          "0101010101Ȩɱ×ÿĥ®ĄçµãĿ«««10101101010101010101011100011001010101X1010101X1010101X0\n"+
          "010101010101ЭбϝϻѩѯухϡҨӿխ؇ĕƶ01101010101010101011ᶇᵿᵳXwôØ&,/]_ÙąƐź011001Ȩɱ×ÿĥ®Ąçµãw\n"+
          "010ᶇᵿᵳXwôØ&,/]_ÙąƐź010101001ᶇᵿᵳXwôØ&,/]_ÙąƐź010101011100011001010101X1010101X101\n"+
          "SYSTEM_LOCKED ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
          
          )
    
    root.after(timeout,root.destroy)

    root.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------MAD.OS HACK ACCESS DENIED CONSOLE2---------------------------------------------------------------------------------------------------------------------
def mados_d2(timeout=15000):

    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])


        if len(string)>1:
            widget.after(2, delay,widget,string[1:])
            
        

    root= tk.Tk()
    t=tk.Text(root)
    t.config(bg="black",fg="green",font=("Consolas",11),height=28,width=80,state="normal")
    t.pack()

    delay(t,

          "ENTERING MATRIX:0010101010100101010101001010101010010101010101202010101010101010\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "1010010101010101011010101011100011001010101X1010101X1010101X10101XX1011010101010\n"+
          "101011010110101101010101010101011100011001010101X1010101X1010101X1010101X0101010\n"+
          "D1101010101010101011100011001010101X1010101X1010101X1010101101010101010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          ">>>FINDING LOCATION1010101001010100100101010010101010101010101101010Y10101011010\n"+
          ">>>FATAL ERROR : LOCATION DOES NOT EXIST 01011100011001010101X1010101X1010101X1202\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "10101010101010110010101010010NG10101101010101010101011100011001010101X1010101X10\n"+
          "10100101010110001010101010101010101010101019101010101010                     \n"+
          "ANCHOR DOES NOT RESPONSE10101010101010101111111111111110000000000000000000000000\n"+
          "Ýı¿ϵѪѪЧуϨљ▒▒ᶇᵿᵳXwôØ&,/]_ÙąƐźœƩȡȿʘȸȀɾʍʏʑ0101010101010jajfiqh1010ffewbewbewu100101\n"+
          "01010101010101001010110101ϙϰЁФΔΦΞϠх101011100011001010101X1010101X10101X1010101X0\n"+
          "0101010Ýı¿ϵѪѪЧуϨљ▒▒1010010101101010ᶇᵿᵳXwôØ&,/]_ÙąƐź1100011001010101X1010101X1010\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101ЭбϝϻѩѯухϡҨӿխ؇ĕƶ01101010101010101011ᶇᵿᵳXwôØ&,/]_ÙąƐź011001010101X101100"+
          "010ᶇᵿᵳXwôØ&,/]_ÙąƐź010101001ᶇᵿᵳXwôØ&,/]_ÙąƐź010101011100011001010101X1010101X101\n"+
          "LOCATION NOT FOUND...\n"
          
          )
    
    root.after(timeout,root.destroy)

    root.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------MAD.OS HACK ACCESS GRANTED CONSOLE2---------------------------------------------------------------------------------------------------------------------
def mados_g2(timeout=25000):

    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])

        if len(string)>1:
            widget.after(2, delay,widget,string[1:])        

    root= tk.Tk()
    t=tk.Text(root)
    t.config(bg="black",fg="green",font=("Consolas",11),height=28,width=80,state="normal")
    t.pack()

    delay(t,

          "ENTERING MATRIX:0010101010100101010101001010101010010101010101202010101010101010\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "1010010101010101011010101011100011001010101X1010101X1010101X10101XX1011010101010\n"+
          "101011010110101101010101010101011100011001010101X1010101X1010101X1010101X0101010\n"+
          "D1101010101010101011100011001010101X1010101X1010101X1010101101010101010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          ">>>FINDING LOCATION1010101001010100100101010010101010101010101101010Y10101011010\n"+
          "‰Ἳ101101010101010101011100011001010101X1010101X1010101X1010101X01011013010200401\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "10101010101010110010101010010NG10101101010101010101011100011001010101X1010101X10\n"+
          "101001010101100010101010101010101010101010                                      \n"+
          ">>>DECRYPTING LOCATION\n"+
          "Ýı¿ϵѪѪЧуϨљ▒▒ᶇᵿᵳXwôØ&,/]_ÙąƐźœƩȡȿʘȸȀɾʍʏʑ0101010101010jajfiqh1010ffewbewbewu100101\n"+
          "01010101010101001010110101ϙϰЁФΔΦΞϠх101011100011001010101X1010101X10101X1010101X0\n"+
          "0101010Ýı¿ϵѪѪЧуϨљ▒▒1010010101101010ᶇᵿᵳXwôØ&,/]_ÙąƐź1100011001010101X1010101X1010\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101ЭбϝϻѩѯухϡҨӿխ؇ĕƶ01101010101010101011ᶇᵿᵳXwôØ&,/]_ÙąƐź011001010101X101100"+
          "010ᶇᵿᵳXwôØ&,/]_ÙąƐź010101001ᶇᵿᵳXwôØ&,/]_ÙąƐź010101011100011001010101X1010101X101\n"+
          "LOCATION FOUND0101010101011100011001010101X1010101X1010101X1010101X0\n"
          
          )
    
    root.after(timeout,root.destroy)

    root.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------------------MAD.OS HACK ACCESS GRANTED CONSOLE1---------------------------------------------------------------------------------------------------------------------
def mados_g1(timeout=25000):

    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])

        if len(string)>1:
            widget.after(2, delay,widget,string[1:])
            
    root= tk.Tk()
    t=tk.Text(root)
    t.config(bg="black",fg="green",font=("Consolas",11),height=25,width=80,state="normal")
    t.pack()

    delay(t,

          "OPENING MATRIX:00101010101001010101010010101010100101010101012020101010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "1010010101010101011010101011100011001010101X1010101X1010101X10101XX1011010101010\n"+
          "101011010110101101010101010101011100011001010101X1010101X1010101X1010101X0101010\n"+
          "D1101010101010101011100011001010101X1010101X1010101X1010101101010101010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "MINING DATA...FINDING COMPONENTS.....1010101001010100100101010010101010101010101\n"+
          "ȡʖɻȫǌ↕₴‹›››‰Ἳ101101010101010101011100011001010101X1010101X1010101X1010101X010110\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "10101010101010110010101010010NG10101101010101010101011100011001010101X1010101X10\n"+
          "1010010101011000101010101010101010101010100101010010010101001XX10101001010100101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "01010101010101001010110101ϙϰЁФΔΦΞϠх101011100011001010101X1010101X10101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "SUCCESSFULLY OPENED MATRIX0101010101011100011001010101X1010101X1010101X1010101X0\n"
   
          )
    
    root.after(timeout,root.destroy)

    root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------MAD.OS HACK ACCESS DENIED CONSOLE1---------------------------------------------------------------------------------

#HACK MAD.OS ACCESS DENIED
def mados_d1(timeout=25000):
    
    def delay(widget, string):
        if len(string)>0:
            widget.insert("end",string[0])

        if len(string)>1:
            widget.after(2, delay,widget,string[1:])
            
    root= tk.Tk()
    t=tk.Text(root)
    t.config(bg="black",fg="green",font=("Consolas",11),height=25,width=80,state="normal")
    t.pack()

    delay(t,

          "OPENING MATRIX:00101010101001010101010010101010100101010101012020101010101010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "01010101010101001010110101ʀɇµ∑ῶ0101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "MATRIX DICRYPTION FAILED1010101011010101011100011001010101X1010101X1010101X10101\n"+
          "FATAL_ERROR1010110101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "SYSTEM_CALLBACK:FAILED1101010101010101011100011001010101X1010101X1010101X1010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "UNEXPECTED ACTION QUEUE101010XXX1010ʀɇµ∑ῶDSKAD24989EQ9779XX00X110101101011010101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "10101010101010110010101010010G10101101010101010101011100011001010101X1010101X10\n"+
          "1010010101011000101010101010101010101010100101010010010101001XX10101001010100101\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "01010101010101001ʀɇµ∑ῶ1010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "010101010101010010101101010101010101011100011001010101X1010101X1010101X1010101X0\n"+
          "USER RESPONE FAILED THROWBARCK IN 5SEC\n"
          
          )
    
    root.after(timeout,root.destroy)

    root.mainloop()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------

#---MAD.OS HACKING STAGE1----------------------------------------------------------------------------------------------------------------------------------------------
    
def stage1(timeout=100000):
    root = tk.Tk()
    root.resizable(width=False,height=False)
    stage1.data=""
    label=tk.Label(root,text=
                 "*MAD.OS 1.0  WTN.2142* (SECURE)                                \n"+
                 "LATEST COMMAND: SECURITY KEY:KLUCH2400960 SECURITY DISABLE START LEAK INTO SOURCE:\n"+
                 "OUTBURST BINARY SWEEPING DATABASE FIRST_CORE DESTABILISIZE MATRIX DIMENSION\n"+
                   "M>>"
                                      
                   ,bg="black",fg="green",font=("Consolas",11),justify="left")
    
    label.config(borderwidth=0)

    label.grid(row=0)
    text=tk.Text(root,height=20,width=82,bg="black",fg="green",font=("Consolas",11))
    text.focus_force()
    text.grid(row=1)
    text.config(borderwidth=0)

    def get():
        stage1.data = str(text.get("1.0","end-1c")).split()
        root.destroy()

    def get_R(event): get()
    root.bind("<Return>", get_R)

    root.after(timeout, root.destroy)

    root.mainloop()


#method that will start stage1 of mados boss fight
    
def hack_mados1():
    stage1()
    if stage1.data ==['SECURITY','KEY:KLUCH2400960','SECURITY','DISABLE','START','LEAK','INTO','SOURCE:OUTBURST','BINARY',
                      'SWEEPING','DATABASE','FIRST_CORE','DESTABILISIZE','MATRIX','DIMENSION']:
        #if hacking succeeds         
        mados_g1()
        time.sleep(0.5)
        print("Yes! First core is done let's move to the next one...")
        time.sleep(1)
        hack_mados2() #next panel to hack
    else:
        #if hacking fails
        mados_d1()
        e=electrocute()#will electrocute player
        
        if e==False: #if player is dead
            print("I got electrocuted once too many. Gliding lights on the inside of my eyelids are the last thing I see.... \nGame over!")
            sys.exit()
        #if player is still alive
        else:
            time.sleep(1)
            print("Ouch! The console electrocuted me!")
            time.sleep(1)
            print("I have to try hacking this again...")
            time.sleep(1)
            hack_mados1()#will return player to start. Player will need to hack first panel again


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------



#---MAD.OS HACKING STAGE2----------------------------------------------------------------------------------------------------------------------------------------------

        
def stage2(timeout=100000):
    
    root = tk.Tk()
    root.resizable(width=False,height=False)
    stage2.data=""
    label=tk.Label(root,text="MATRIX AVIABLE FOR 100 SEC>>>                                                              \n"+
                   "LATEST COMMAND: FIND LOCATION_XYZ ENABLE ANCHOR INSERT PORT LOCALIZE ESTABLISH CONNECTION:\n"+
                   "UNFREEZE DATABITS TWITCH SPHERE INTO SUPER_POSITION NAVIGATION ON LOCATION OF PARAMETER   \n"+
                   "M>                                                                                    "
                   ,bg="black",fg="green",font=("Consolas",11))

    
    label.config(borderwidth=0)

    label.pack()
    text=tk.Text(root,height=20,bg="black",fg="green",width=90,font=("Consolas",11))
    text.focus_force()
    text.pack()
    text.config(borderwidth=0)

    def get():
        stage2.data = str(text.get("1.0","end-1c")).split()
        root.destroy()


    def get_R(event): get()
    root.bind("<Return>", get_R)

    root.after(timeout, root.destroy)
    
    root.mainloop()#koko ikkunan mainlooppi


#TRIGGERING HACKING OF SECOND STAGE
    
def hack_mados2():
    stage2()
    if stage2.data==['FIND','LOCATION_XYZ','ENABLE','ANCHOR','INSERT','PORT','LOCALIZE','ESTABLISH','CONNECTION:UNFREEZE',
                     'DATABITS','TWITCH','SPHERE','INTO','SUPER_POSITION','NAVIGATION','ON','LOCATION','OF','PARAMETER']:
        mados_g2()
        time.sleep(0.5)
        print("Yes! Second core is done! Let's move to the last one...")
        time.sleep(1)
        hack_mados3()
    else:
        mados_d2()
        e=electrocute()
        if e==False: #if player is dead
            print("I got electrocuted once too many. Gliding lights on the inside of my eyelids are the last thing I see.... \nGame over!")
            sys.exit()
        #if player is still alive
        else:
            time.sleep(1)
            print("Ouch! The console electrocuted me!")
            time.sleep(1)
            print("I have to try hacking this again. The terminal threw me to start of the hacking!")
            time.sleep(1)
            hack_mados1()#will return player to start. Player will need to hack first panel again


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#---MAD.OS HACKING STAGE3----------------------------------------------------------------------------------------------------------------------------------------------

        
def stage3(timeout=100000):
    root = tk.Tk()
    root.resizable(width=False,height=False)
    stage3.data=""
    label=tk.Label(root,text=
                 "***MAD.OS 1337 MAIN_CORE***                                                        \n"+
                   "LATEST COMMAND: CAPTURE_CORE DECRYPT_CORE FIND_ANCHOR STRIKE_VOID_RUSH RESTART_LOCK ENT\n"+
                   "ER BRAINCORE WOW IM HACKING COOL UPDATE MATRIX SPHERE SYSTEM HARD RESTART CRYPT NEW DAT\n"+
                   "A LOCK SYSTEM MADOS.HARDRESTART"
                   ,bg="black",fg="red",font=("Consolas",11),justify="left")
    
    label.config(borderwidth=0)

    label.grid(row=0)
    text=tk.Text(root,height=20,bg="black",fg="red",width=87,font=("Consolas",11))
    text.focus_force()
    text.grid(row=1)
    text.config(borderwidth=0)

    def get():
        stage3.data = str(text.get("1.0","end-1c")).split()#print#print
        root.destroy()


    #syöttö
    def get_R(event): get()
    
    root.bind("<Return>", get_R)

    root.after(timeout, root.destroy)
    
    root.mainloop()#koko ikkunan mainlooppi
        
#STARITNG STAGE 3
def hack_mados3():
    stage3()
    if stage3.data==['CAPTURE_CORE','DECRYPT_CORE','FIND_ANCHOR','STRIKE_VOID_RUSH','RESTART_LOCK','ENTER','BRAINCORE','WOW','IM','HACKING',
                     'COOL','UPDATE','MATRIX','SPHERE','SYSTEM','HARD','RESTART','CRYPT','NEW','DATA','LOCK','SYSTEM','MADOS.HARDRESTART']:
        mados_g3()
        winsound.PlaySound("ending.wav", winsound.SND_ASYNC)
        #if hacking succeeds player will defeat MadOS.
        print("\n"*20)
        fast_print("The MadOS shuts down. Massive rotation engines of H3LS1NK1 grind to a halt. Whirring sounds of distressed complex power down, and just the faint sound of dormancy generators can be heard from the depths of the machine. \nBleeping screens indicate the slowly depleting quality of air among the other error messages. Somewhere down there in the depths of the machine broken MadOS slumbers, waiting for Western Terra Nations' professionals' analyzing. Announcement system declares that the military transport ship of WTN is docking in in 4 minutes. \nA small window catches your eye. The black space is adorned by distant asteroid belt. Stars seem to wink at you.")
        print("\n"*20)
        time.sleep(7)
        Logo()
        scrollingtext()
        time.sleep(11)
        sys.exit()
        return
    
    else:
        #if hacking fails the last console will be locked so the player cannot use it anymore
        mados_d3()
        time.sleep(0.5)
        print("The core is locked! The only option left is to test how well these servers and hard drives endure crowbar.")
        #because player cant use console anymore server closet will appear that will need to be defeated.
        #if player will defeat it, mados will be defeated
        time.sleep(1)
        hit()
        winsound.PlaySound("ending.wav", winsound.SND_ASYNC)
        print("\n"*20)
        fast_print("The MadOS shuts down permanently. Massive rotation engines of H3LS1NK1 grind to a halt. Whirring sounds of distressed complex power down, and just the faint sound of dormancy generators can be heard from the depths of the machine. \nBleeping screens indicate the slowly depleting quality of air among the other error messages. Announcement system declares that the military transport ship of Western Terra Nations is docking in in 4 minutes. \nA small window catches your eye. The black space is adorned by distant asteroid belt. Stars seem to wink at you.")
        print("\n"*20)
        time.sleep(7)
        Logo()
        time.sleep(2)
        scrollingtext()
        time.sleep(11)
        sys.exit()
        return False
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    
                                #---------------PREPARATIONS----------------
                        
    #Open Database connection
db = mysql.connector.connect(
    host = "localhost",
    user = "dbuser",
    passwd = "dbpass",
    db = "ASD_datav1",
    buffered = True)

    #Initialize player location and action
action = ""
target = ""
cur = db.cursor()
sql = "UPDATE PLAYER SET Location = 21"
cur.execute(sql)

# Clear console
print("\n"*1000)

Logo()

#ambient music
winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)

con()

fast_print("\nI'm an IT-engineer. I was sent here to Western Terra Nations' space station 'H3L51NK1' to stop it's corrupted Artficial Intelligence from attacking foreign nation. \nMy mission is dangerous and delicate, I must be sharp!\n \n(If you don't know what to do type 'help' or 'commands').\n \n")
visited()

    #Initialize the booleans for various things
taunt1boolean = False
taunt2boolean = False
SR1door = False
SR2door = False
Radioboolean = False
Ventboolean = False
MazeComplete = False
QuizComplete = False
ChestHacked = False

                                #-----------------MAIN LOOP------------------


while action != "quit":

    #death
    death = "SELECT HP FROM PLAYER WHERE HP < 1"
    cur.execute(death)
    playerhp = cur.fetchall()
    if cur.rowcount>=1:
        for row in playerhp:
            print("Game over!")
            sys.exit()

    #ambient music
    winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)

    #Parser
    print("")
    input_string=input("\nYour action? ").split()
    if len(input_string)>=1:
        action = input_string[0].lower()
    else:
        action = ""
    if len(input_string)>=2:
        target = input_string[len(input_string)-1].lower()
    else:
        target = ""
    #print("Parsed action: " + action)
    #print("Parsed target: " + target)
    print("")
        
    #get description
    if action == "look" and (target == "around" or target == ""):
        print("\n")
        visited()
        print("\n\n")
        items_in_room()

    #examine
    elif action == "examine" or action == "inspect" and target !="":
        print("\n")
        Examine(target)
        print("\n")

    #anna kortti
    elif action == "red":
        sql = "UPDATE OBJECT SET PlayerID = 1 WHERE ObjectID = 3"
        cur.execute(sql)
        print("sait kortin vittu")
        
    #Show commands
    elif action == "commands" or action == "help":
        print("\n")
        commands()
        print("\n")
        
    #Show map.
    elif action == "map":
        print("\n")
        show_map()
        print("\n")

    #Show inventory
    elif action == "inventory":
        inventory()

    #show hp
    elif action == "hp":
        hp = "SELECT HP FROM PLAYER"
        cur.execute(hp)   
        curhp = cur.fetchall()
        if cur.rowcount>=1:
            for row in curhp:
                curhp = row[0]
                print("Your HP:", curhp)
        
    #Picking up items
    elif action == "take" or action == "get" and target !="":
        take(target)

    #Dropping items
    elif action == "drop" and target != "":
        localloc = CurRoomLoc()
        drop(target,localloc)

    #Talking to ANDY
    elif action == "talk" and target == "andy" and CurRoomLoc() == 23:
        andy()
        
    #Use Jukebox
    elif ((action == "use" or action == "examine" or action == "inspect") and (target == "jukebox") and (CurRoomLoc() == 23)):
        jukebox()
        
    #use radio
    elif action == "use" and target == "radio" and CurRoomLoc() == 9:
        radio()

    #Using HP stations
    elif (action == "use" and target == "hpstation" and (CurRoomLoc() == 17 or CurRoomLoc() == 8)):
        hpstation()

    #Using ammo station
    elif (action == "use" and target == "ammostation" and CurRoomLoc() == 17):
        ammostation()
        
    #Ventilation stuff
    elif ((action == "inspect" or action == "look" or action == "examine") and (target == "ventilation" and CurRoomLoc() == 4)):
        print("Behind the grid is a ventilation shaft large enough for me to fit in. The grid looks weak enough...")

    elif ((action == "hit" or action == "destroy" or action == "pull" or action == "kick") and (target == "grid" or target == "ventilation") and CurRoomLoc() == 4):
        print("\nThe grid comes off easy. Way to shaft is now free.\n")
        Ventboolean = True
        
    #Hacking the tutorial container 
    elif (action == "hack" and (target == "container" or target == "chest" or target == "locker" or target == "terminal") and CurRoomLoc() == 1and ChestHacked == False) == 1:
        chest()
        #ChestHacked = True
        
    #Hacking the secret room 1
    elif (action == "hack" and (target == "door" or target == "console" or target == "terminal") and CurRoomLoc() == 11):
        x = hack_console1()
        if x == True:
            SR1door = True
            print("\nI unlocked the door!\n")

    #Hacking the secret room 2
    elif (action == "hack" and (target == "door" or target == "console" or target == "terminal") and CurRoomLoc() == 12):
        x = hack_console2()
        if x == True:
            SR2door = True
            print("\nI unlocked the door!\n")

    #Getting directions
    elif action == "north" or action == "n" or action == "south" or action == "s" or action == "east" or action == "e" or action == "west" or action == "w":
        if action == "e":
            action = "east"
        if action == "w":
            action = "west"
        if action == "n":
            action = "north"
        if action == "s":
            action ="south"
        direction = action

        #Moving
            #Move = 0: There is no door to that way.
            #Move = 1: Player gets through without key card.
            #Move = 2: Player gets through with a key card.
            #Move = 3: Player need a red key card.
            #Move = 4: Player need a blue key card.
            #Move = 5: Player need a green key card.
            #Move = 6: Player needs to hack Secret Room door first.
            #Move = 7: Player needs the space suit.
            #Move = 8: Player proceeds with suit.
            #Move = 9: Player proceeds to maze.
            #Move = 10: 1. Taunt when player arrives to B2.
            #Move = 11: 2. Taunt when player arrives to B3.
            #Move = 12: Ventilation shaft is blocked.
            #Move = 13: Ventilation shaft is open.
            #Move = 14: Player proceeds to quiz.
            #Move = 15: Player proceeds to elevator.

        case = Moving(direction)
        if case == 0:
            print("\nI can't go that way. \n")

        elif case == 1:
            
            winsound.PlaySound("door.wav", winsound.SND_ASYNC)
            time.sleep(2)
            winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)
            
            print("\nDoors slide open as I approach them. \n")
            visited()
            print("\n")
            items_in_room()
            
            sql = "SELECT ENEMYID FROM ENEMY WHERE LOCATION = (SELECT LOCATION FROM PLAYER)"
            cur.execute(sql)
            enemyloc = cur.fetchall()
            if cur.rowcount>=1:
                for row in enemyloc:
                    time.sleep(6.5)
                    enemyloc = row[0]
                    hit()

        elif case == 2:

            winsound.PlaySound("door.wav", winsound.SND_ASYNC)
            time.sleep(2)
            winsound.PlaySound("ambient.wav", winsound.SND_ASYNC)
            
            print("\nI slide the key card through the console. Doors slid open with a hiss.\n")
            visited()
            items_in_room()

            sql = "SELECT ENEMYID FROM ENEMY WHERE LOCATION = (SELECT LOCATION FROM PLAYER)"
            cur.execute(sql)
            enemyloc = cur.fetchall()
            if cur.rowcount>=1 and CurRoomLoc() != 24:
                for row in enemyloc:
                    time.sleep(6.5)
                    enemyloc = row[0]
                    hit()

        elif case == 3:
            print("\nDoors don't react to my approach. Console next to the doors has a narrow slot with red rims around it.\n")

        elif case == 4:
            print("\nDoors don't react to my approach. Console next to the doors has a narrow slot with blue rims around it.\n")

        elif case == 5:
            print("\nDoors don't react to my approach. Console next to the doors has a narrow slot with green rims around it.\n")
            
        elif case == 6:
            print("\nDoors don't react to my approach. There's a glowing, square terminal next to the doors...\n")
            
        elif case == 7:
            print("\nPneeking through the window in the door I can see an airlock. Behind that there's a long, trashed corridor. There's a long tear on the east side wall and all the windows are broken. There doesn't seem to be gravity. I won't make it to the door on the other side without some kind of protective gear.\n")

        elif case == 8:
            print("\nI step to the airlock. Door behind me shuts and the door leading to corridor hisses open. As the air gets sucked to the void, gravity disappears and I start breathing stored air. I launch myself towards the other door and float through the trash and shards. The airlock on the other end of the corridor works same as the previous one. I step to the next room.\n")
            print("\n")
            visited()
            print("\n")

        elif case == 9:
            winsound.PlaySound("door.wav", winsound.SND_ASYNC)            
            print("\n")
            visited()
            print("\n")
            items_in_room()
            print("\n")
            if MazeComplete == False:
                maze()
                MazeComplete = True

        elif case == 10:
            winsound.PlaySound("door.wav", winsound.SND_ASYNC)
            print("\n")
            visited()
            print("\n")
            items_in_room()
            print("\n")
            time.sleep(1)
            if taunt1boolean == False:
                taunt1()
                taunt1boolean = True
                
        elif case == 11:
            winsound.PlaySound("door.wav", winsound.SND_ASYNC)
            print("\n")
            visited()
            print("\n")
            items_in_room()
            print("\n")
            time.sleep(3)
            if taunt2boolean == False:
                taunt2()
                taunt2boolean = True

        elif case == 12:
            print("\nI can't go that way. There's a ventilation shaft blocked by a loose grid.\n")

        elif case == 13:
            print("\nI crawl to dark shaft...\n")
            visited()

        elif case == 14:
            winsound.PlaySound("door.wav", winsound.SND_ASYNC)
            print("\n")
            visited()
            print("\n")
            if QuizComplete == False:
                quiz()
                QuizComplete = True

        elif case == 15:
            print("\n")
            visited()
            print("\n")
            elevator()

        elif case == 16:
            print("\n")
            visited()
            print("\n")
            madosdialogue()
            
    #If the action is not recognised.
    elif action!="quit" and action!="" and action!="talk" and action!="take" and action != "get" and action != "look":
        print("I don't know how to " + action)

else:
    print("Quitting the game. Goodbye!")
db.rollback()
db.close()
