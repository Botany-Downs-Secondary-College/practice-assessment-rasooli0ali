from tkinter import*
from random import*


def Screen1():
    global frame1
    
    frame3.grid_remove()
    frame2.grid_remove()
    
    frame1=LabelFrame(root,height="800",width="300",bg="light blue")
    frame1.grid(row=0,column=0)
    Titlelabel=Label(frame1,bg="black",fg="white",width=30,height=2,padx=30,pady=10,
                      text="Savings Plan! ",font=("Time","14","bold italic"))
    Titlelabel.grid(columnspan=3)
    
    
    button1=Button(frame1,text="Next",anchor=W,command=Screen2)
    button1.grid(row=1,column=1)
    
    button1=Button(frame1,text="home",anchor=W,command=Screen1)
    
    
   
def Screen2():
    global frame2
    global answer_entry
    global GUI_item_entry
    global name_feedback
    
    
    frame1.grid_remove()
    frame3.grid_remove()
    
    frame2=LabelFrame(root,height="800",width="300",bg="light blue")
    frame2.grid(row=0,column=0)  
    
    name_GUI=Label(frame2,text="Hello, What is your name? ",width=40,height=3,bg="red")
    name_GUI.grid(row=1,column=1,sticky=W)
    
    answer_entry=Entry(frame2,width=47)
    answer_entry.grid(row=2,column=1,sticky=W) 
    
    item_GUI=Label(frame2,text="What do you want to buy? ",width=40,height=3,bg="red")
    item_GUI.grid(row=3,column=1,sticky=W)
    
    GUI_item_entry=Entry(frame2,width=47)
    GUI_item_entry.grid(row=4,column=1,sticky=W)    
    
    button2=Button(frame2,text="home",anchor=W,command=Screen1)
    button2.grid(row=6,column=0) 
    
    button1=Button(frame2,text="Next",anchor=W,command=check_name,relief=RIDGE)
    button1.grid(row=6,column=5)
    
    name_feedback=Label(frame2,text="",height=3)
    name_feedback.grid(row=7,column=1)      


def Screen3():
    global frame3
    global W_income_entry
    global W_expenses_entry
    global time_entry

    frame2.grid_remove()
    frame1.grid_remove()
    
    frame3=LabelFrame(root,height="800",width="300",bg="light blue")
    frame3.grid(row=0,column=0)
    
    GUI_W_income=Label(frame3,text="What is your weekly income? $:? ",width=40,height=3,bg="red")
    GUI_W_income.grid(row=1,column=1,sticky=W)    
    W_income_entry=Entry(frame3,width=47)
    W_income_entry.grid(row=2,column=1,sticky=W)   
    
    GUI_W_expenses=Label(frame3,text="How much is your weekly expenses? :$ ",width=40,height=3,bg="red")
    GUI_W_expenses.grid(row=3,column=1,sticky=W)    
    W_expenses_entry=Entry(frame3,width=47)
    W_expenses_entry.grid(row=4,column=1,sticky=W)  
    
    GUI_time=Label(frame3,text="How many weeks do you have to save? :  ",width=40,height=3,bg="red")
    GUI_time.grid(row=5,column=1,sticky=W)    
    time_entry=Entry(frame3,width=47)
    time_entry.grid(row=6,column=1,sticky=W) 
    
    button2=Button(frame3,text="home",anchor=W,command=Screen1)
    button2.grid(row=7,column=0) 
    
    button1=Button(frame3,text="Next",anchor=W,command=Screen4)
    button1.grid(row=7,column=5)
    
    feedback=Label(frame2,text="",height=3)
    feedback.grid(row=8,column=1)
def Screen4():
    frame3.grid_remove()
    frame4=LabelFrame(root,height="800",width="300",bg="light blue")
    frame4.grid(row=0,column=0)
    
    button2=Button(frame4,text="home",anchor=W,command=Screen1)
    button2.grid(row=7,column=0) 
        
    button1=Button(frame4,text="Next",anchor=W,command=Screen4)
    button1.grid(row=7,column=5)    

def check_name():
    if answer_entry.get()=="":
        name_feedback.configure(text="please enter your name")
        answer_entry.focus()
        answer_entry.delete(0,END)
    elif answer_entry.get().isalpha()==False:
        name_feedback.configure(text="please enter text")
        answer_entry.delete(0, END)
        answer_entry.focus()
    elif GUI_item_entry.get()=="":
        name_feedback.configure(text="please enter your item name")
        GUI_item_entry.focus()
        GUI_item_entry.delete(0, END)
    elif GUI_item_entry.get().isalpha()==False:
        name_feedback.configure(text="please enter text")
        GUI_item_entry.delete(0, END)
        GUI_item_entry.focus()  
    else:
        frame2.grid_remove()
        frame3.grid(row=1,columnspan=4)
        Screen3()

def check_user_needs():
    if W_income_entry.get()=="":
        feedback.configure(text="please enter income")
        W_income_entry.focus()
        W_income_entry.delete(0,END)
    elif W_income_entry.get().isdigit()==False:
        
        
        



root = Tk()
root.title("Frames")
root.geometry("462x235+850+0")
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)
frame4=Frame(root)
Screen1()
root.mainloop()

