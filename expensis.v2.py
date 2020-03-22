def user_name(): 
   while True:
      name = input("what is is your name? :").strip()
      if name and name.isalpha():  
         break # leave the loop if done  
      elif name and name.isdigit():
         print("Name must be Alphabet characters only!")  
      else:  
         print ("Please enter something")

user_name()

item=""
item=input("what do you want to buy:")
while True:
   try:
      target=float(input("How much do money do you need to save ? $"))
      w_income = float(input("Hello, What is your weekly income? $:"))
      w_expenses = float(input("How much is your weekly expenses? :$"))
      time=int(input("How many weeks do you have to save? : "))
      break
   except ValueError:
      print("Please enter a valid number e.g. 2.500")
        
w_deposit=w_income-w_expenses
deposit_target=target/time

if deposit_target > w_deposit:
   deposit_needed=deposit_target-w_deposit
   print("You need save up this much more weekly :${} ".format(deposit_needed))
else:
   print("This is how much you need to save per week {}".format(deposit_target))