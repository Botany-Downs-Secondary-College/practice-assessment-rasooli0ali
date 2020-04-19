from tkinter import *
import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user (usernames text, passwords text)")
conn.commit()
conn.close()

'''
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("DELETE from user WHERE oid=3")
conn.commit()
conn.close()
'''
#========================================Adding or removing data for user================================
def add_data_():
        websitee=website_entry.get()
        passwordss=password_entry.get()
        usernamess=username_entry.get()        
        
        userID=email.get()
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()                
        
        c.execute('''INSERT INTO {} VALUES(:W, :U, :P)'''.format(userID),
                      {
                              'W': websitee,
                              'U': usernamess,
                              'P': passwordss
                      })#Inserts new account into databse  
        feedback2.configure(text="Website Added", bg="green")
        conn.commit()
        conn.close

def add_data_frame():
        frame1.grid_remove()
        frame2.grid_remove()
        frame3.grid_remove()
        
        global frame4
        global feedback2
        global website_entry
        global username_entry
        global password_entry
        
        frame4 = LabelFrame(root, height="800", width="300")
        frame4.grid(row=0, column=0, columnspan=2)
        
        #off screen labels
        website_entry_label=Label(frame4, text="entry website")
        username_entry_label=Label(frame4, text="entry email")
        password_entry_label=Label(frame4, text="entry password")
        
        #on screen labels
        website_entry_label.grid(row=2, column=0)
        username_entry_label.grid(row=3, column=0)
        password_entry_label.grid(row=4, column=0)
        
        #off screen entries
        website_entry=Entry(frame4)
        username_entry=Entry(frame4)
        password_entry=Entry(frame4)
        
        #on screen Entries
        website_entry.grid(row=2, column=1)
        username_entry.grid(row=3, column=1)
        password_entry.grid(row=4, column=1)
        
        #off screen button
        add_data = Button(frame4, text="Add", width=11, height=1, anchor=W, command=add_data_)
        back = Button(frame4, text="back", width=11, height=1, anchor=W, command=user_frames)
        
        
        
        #on screen button
        add_data.grid(row=6, column=2)
        back.grid(row=6, column=0)
        
        #off screen feedback bar
        feedback2 = Label(frame4, text="")        
        
        #on screen feedback bar
        feedback2.grid(row=5, columnspan=2)
        
def remove_data_frame():
        return

#===========================================SignIn and SignUp============================================
def signin():
        username = email.get()#Asks for username
        password = password2.get()#Asks for password    
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        find_user = ("SELECT *, oid FROM user WHERE usernames = ? AND passwords = ?")#Validates inputs for account
        c.execute(find_user,[(username),(password)])
        results = c.fetchall()#Fetches values from database
        
        if results:#Validates if the username/password is recognised
                conn = sqlite3.connect('users.db')
                c = conn.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS {}(website text, usernames text, passwords text)".format(username))
                conn.commit()
                conn.close() 
                
                user_frames()
        else:
                feedback1.configure(text="username not found", bg="red")                
                      
def New_user():
        password = password1.get()
        username = username1.get()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
    
        findUser = ("SELECT * FROM user WHERE usernames = ?")
        c.execute(findUser, [(username)])#Checks existence of username in database
        if c.fetchall():
                feedback.configure(text="username taken", bg="red")
                return
        else:
                feedback.configure(text="account created", bg="green")
                insertData = ('''INSERT INTO user(usernames, passwords)
                VALUES(?,?)''')#Inserts new account into databse
                c.execute(insertData, [(username),(password)])
                conn.commit()
                conn.close()
#===========================================FRAMES========================================================== 
def user_frames():
        frame1.grid_remove()
        frame2.grid_remove()
        userID=email.get()
        
        global frame3
        
        websitee=str("www.google.com")
        passwordss=str("sajjad")
        usernamess=str("hamid")
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()        
        
        """
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("DELETE from {} WHERE oid=1".format(userID))
              
        """
        
        frame3 = LabelFrame(root, height="800", width="300")
        frame3.grid(row=0, column=0, columnspan=2)
        
        #titles
        LOGED = Label(frame3, text="Loged In", padx=5, pady=5, font=("Times", "20", "bold"))
        LOGED.grid(row=0, column = 0,columnspan=5)
        USER_LABEL = Label(frame3, text=userID, font=("Times", "20", "bold"))
        USER_LABEL.grid(row=1, column=0, columnspan=5)       
        
        
        #off screen buttons
        add_data = Button(frame3, text="add password", width=11, height=1, anchor=W, command=add_data_frame)
        remove_data = Button(frame3, text="remove password", width=11, height=1, anchor=W, command=remove_data_frame)
        logout=Button(frame3, text="Sign Out",width=11,height=1, anchor=W, command=main_menu)
        
        #on screen buttons
        add_data.grid(row=3, column=0)
        remove_data.grid(row=3,column=4)
        logout.grid(row=3,column=1,columnspan=2)
        
        
        c.execute("SELECT * FROM {}".format(userID))
        re = c.fetchall()
        
        print_re=""
        for i in re:
                print_re += "   website = " + str(i[0]) +"\n"+ "email = " + str(i[1]) +"\n"+ "password = " + str(i[2] + "\n" +"\n")
        
        user_details=Label(frame3, text=print_re, bg="blue")
        user_details.grid(row=2, column=1, columnspan=2)
        
        conn.commit()
        conn.close()
        
        

def New_account():
        frame1.grid_remove()
        
        global frame2
        global username1
        global password1
        global feedback
    
        frame2 = LabelFrame(root, height="800", width="300")
        frame2.grid(row=0, column=0)

        website_title = Label(frame2, text="BDSC 2DIP", padx=5, pady=5, font=("Times", "20", "bold"))
        website_title.grid(row=0, columnspan=4)
        discription = Label(frame2, text="Create a new account for your 2DIP class")
        discription.grid(row=1, columnspan=4)

        # background Labels
        userName_label = Label(frame2, text="Username ")
        password_label = Label(frame2, text="Password ")

        # background Buttons
        sign_up = Button(frame2, text="Sign Up", width=8, height=1, anchor=W, command=New_user)
        back = Button(frame2, text="Back", width=8, height=1, anchor=W, command=main_menu)

        # background Entry boxes
        username1 = Entry(frame2, width=40)
        password1 = Entry(frame2, width=40)

        # on screen Labels
        userName_label.grid(row=5, column=0)
        password_label.grid(row=6, column=0)
    
        # on screen Entry Boxes
        username1.grid(row=5, column=1, columnspan=3)
        password1.grid(row=6, column=1, columnspan=3)
    
        # on screen Buttons
        sign_up.grid(row=8, column=3, pady=5)
        back.grid(row=8, column=0, pady=5)
    
        # feedback background
        feedback = Label(frame2, text="")
    
        # feedback on screen
        feedback.grid(row=8, column=1, columnspan=2)    
        
#=====================================================================================================
def main_menu():
        global feedback1
        global frame1
        global password2
        global email
        
        frame1.grid_remove()
        frame2.grid_remove()
        frame3.grid_remove()
        frame4.grid_remove()
        
        
        frame1 = LabelFrame(root, height="800", width="300")
        frame1.grid(row=0, column=0)
    
        website_title = Label(frame1, text="BDSC 2DIP", padx=5, pady=5, font=("Times", "20", "bold"))
        website_title.grid(row=0, column=0)
        discription = Label(frame1, text="this app is for 2DIP class login")
        discription.grid(row=1, column=0)
    
        # off screen code
        email = Entry(frame1, width=30)
        password2 = Entry(frame1, width=30)
        login = Button(frame1, text="Login", width=30, anchor=W, command=signin)
        new_account = Button(frame1, text="Creat New account", width=30, anchor=W, command=New_account)
    
        # on screen codes
        email.grid(row=2, column=0, padx=20, pady=15)
        email.insert(0, "Write username here please")
        password2.grid(row=3, column=0, padx=20)
        password2.insert(0, "Write password here please")
    
        login.grid(row=4, column=0, pady=10)
        new_account.grid(row=5, column=0, pady=4)
        
        feedback1 = Label(frame1, text="")
        feedback1.grid(row=6, column=0)    

root = Tk()
root.title("BDSC")
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
main_menu()
root.mainloop()