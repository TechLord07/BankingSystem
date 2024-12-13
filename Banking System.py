import mysql.connector as ms
import sys
import random                #for Acc no
from tabulate import tabulate

con=ms.connect(host="localhost",user="Arnav",password="13975",database="Banque_de_Vista")

if con.is_connected():
     pass

else:
     print("Error in Connection.")  

cur=con.cursor()


    
try:
     query="create table Admin_register(Service_number int primary key ,\
     Staff_name varchar(100) not null,Admin_username varchar(100) unique key,\
     Password varchar(15) not null,Phone_number char(10) not null unique key,\
     Department varchar(100) not null,Address varchar(500) not null);"
     cur.execute(query)
     con.commit()
     
except:
     pass

try:
     query="create table Client_register(Account_number int primary key,\
     Client_name varchar(100) not null,Client_username varchar(100) unique key,\
     Password varchar(15) not null,Phone_number char(10) not null unique key,\
     PIN int not null,Address varchar(500) not null);"
     cur.execute(query)
     con.commit()
except:
     pass

try:
     query="create table Savings_Account(Account_number int primary key ,\
     Amount int );"
     cur.execute(query)
     con.commit()
     
except:
     pass

try:
     query="create table FD_Account(Account_number int not null  ,\
     Principal float, Interest float default(7), Time_Period float,\
     Return_Amt float);"
     cur.execute(query)
     con.commit()
     
except:
     pass

try:
     query="create table Loan_Account(Account_number int not null ,\
     Principal float, Interest float default(13), Time_Period float,\
     Repayment_Amt float, Collateral varchar(200));"
     cur.execute(query)
     con.commit()
     
except:
     pass

try:
     query="create table Salary_Account(Account_number int primary key ,\
     Organisation_name varchar(200), Total_Salary float,\
     Tax float default (15), Total_TaxedAmt float, Inhand_Sal float);"
     cur.execute(query)
     con.commit()
     
except:
     pass



print('*'*50)
print("\tWELCOME TO BANQUE DE VISTA")
print('*'*50)
input("Press any key to cotinue")

while True:
    print("1. Admin login")

    print("2. Client login")

    print("3. Admin Register")

    print("4. Client Register")

    print("5. Exit")

    login_type=int(input("Choose the login type(corresponding integer):- "))


    
    if login_type==1:
        print("-"*25,"ADMIN LOGIN","-"*25)
        while True:
             Admin_username=input("Enter your username:- ")
             Password=input("Enter your password:- ")

             #cross check with database
                  #Password
             query="select Password from Admin_register where Admin_username=%s"
             cur.execute(query,(Admin_username,))
             allow_Admin_pass=cur.fetchall()
                  #Username
             query="select Admin_username from Admin_register where Password=%s"
             cur.execute(query,(Password,))
             allow_Admin_username=cur.fetchall()

              #sub-menu if logging unsucessful
             if allow_Admin_username==[] or allow_Admin_pass==[]:
                  print("Incorrect Username or Password!")
                  while True:
                       print("1. Forgot Username or password")
                       print("2. Retry")
                       print("3. Exit")
                       reject_Admin=int(input("Enter the choice(corresponding integer):- "))
                        #Forgotten Password and username
                       if reject_Admin==1:
                            forgot_Serno=int(input("Enter your Service number:- "))
                            forgot_Phone=int(input("Enter your Phone number:- "))
                             
                             #fetching username
                            query="select Admin_username from Admin_register where Service_number=%s and Phone_number=%s"
                            cur.execute(query,(forgot_Serno,forgot_Phone,))
                            forgot_Adm_username=cur.fetchall()
                            con.commit()
     
                             #fetching password
                            query="select Password from Admin_register where Service_number=%s and Phone_number=%s"
                            cur.execute(query,(forgot_Serno,forgot_Phone,))
                            forgot_Adm_password=cur.fetchall()
                            con.commit()
                             #displaying results
                            try:
                                 print("Your username is",forgot_Adm_username[0][0],"and your password is",forgot_Adm_password[0][0])
                                 break
                            except:
                                  print("No such Admin exists. Try registering before logging in.")
                                  Adm_logged=0
                        #to re-enter the details
                       elif reject_Admin==2:
                            break
                        
                        #taking to 1st page interface
                       elif reject_Admin==3:
                            sys.exit()
     
                             #avoiding error
                       else:
                             print("Enter a valid integer!!!")
     
              #logging succesful
             elif allow_Admin_pass[0][0]==Password:
                  query="select Staff_name from Admin_register where Admin_username=%s"
                  cur.execute(query,(Admin_username,))
                  Admin_name=cur.fetchall()
                  con.commit()
                  
                  print("WELCOME",Admin_name[0][0],"to the Banque de Coester Vista Portal")

                  query="select Service_number from Admin_register where Admin_username=%s"
                  cur.execute(query,(Admin_username,))
                  Service_number=cur.fetchall()
                  con.commit()
                  ser_no=Service_number[0][0]
                  Adm_logged=1
                  break

        if Adm_logged!=0:
             while True:
                  print("1. View personal details")
                  print("2. Update your details")
                  print("3. View client personal details")
                  print("4. View all savings accounts details")
                  print("5. View all fd account details")
                  print("6. View all loan account details")
                  print("7. View all salary account details")
                  print("8. Sign Out")
                  print("9. Delete Account")
                  log_task=int(input("Enter your choice:- "))


                  
                  if log_task==1:
                      print("-"*25,"PERSONAL DETAILS","-"*25)
                      query="SELECT * FROM admin_register where Service_number=%s;"
                      cur.execute(query,(Service_number[0][0],))
                      data=cur.fetchall()
                      con.commit()
                      print(tabulate(data, headers=["ServiceNo","Name","Username","Password","PhoneNo","Department","Address"],tablefmt='grid')) 


                  elif log_task==2:
                       while True:

                            print("-"*25,"UPDATE DATA","-"*25) 

                            print("1. Staff name")

                            print("2. Admin username")

                            print("3. Password")

                            print("4. Phone number")

                            print("5. Department")

                            print("6. Address")

                            print("7. Exit")

                            update_type=int(input("Choose the data which you want to update(corresponding integer):- "))

                            if update_type==1:

                                 while True:
                                      Staff_name_new=input("Enter new name:- ")
                                      len_staff=len(Staff_name_new)

                                       #fixing number of digits
                                      if len_staff<=100:
                                           
                                       #not null
                                           if len_staff==0:
                                                print("This field cannot be left empty!")

                                           else:
                                                 query="update Admin_register SET Staff_name=%s WHERE Service_number=%s"
                                                 cur.execute(query,(Staff_name_new,ser_no))
                                                 con.commit()

                                                 print("Staff name has been updated.")
                                                 break
                                            
                                       #avoiding errors
                                      else:
                                           print("Maximum characters allowed = 100")

                                
                            elif update_type==2:

                                 while True:
                                      Admin_username_new=input("Enter new Username:- ")
                                      len_username=len(Admin_username_new)

                                      #fixing number of digits
                                      if len_username<=100:

                                           #not null
                                           if len_username==0:
                                                print("This field cannot be left empty!")

                                           #cross with database
                                           else:
                                                #check for uniqueness
                                                query="select Admin_username from Admin_register where Admin_username=%s" #uniqueness
                                                cur.execute(query,(Admin_username_new,))
                                                exist_Admin_username=cur.fetchall()

                                                #if unique
                                                if exist_Admin_username==[]:
                                                    query="update Admin_register SET Admin_username=%s WHERE Service_number=%s"
                                                    cur.execute(query,(Admin_username_new,ser_no))
                                                    con.commit()

                                                    print("Username has been updated")
                                                    break

                                                #if already exists
                                                else:
                                                    print("Username alredy exists. Try another.")
                                                con.commit()
                                      
                                      else:
                                           print("Maximum characters allowed = 100")
                                      
                            elif update_type==3:

                                 while True:

                                      Password_new=input("Enter new Password:- ")
                                      len_pass=len(Password_new)

                                      #fixing number of digits
                                      if len_pass<=15:
                                           if len_pass==0:
                                                print("This field cannot be left empty!")

                                           elif len_pass<=5:
                                                print("Password too weak. Min length= 6")

                                           else:
                                                #confirm password
                                                check_password=input("Enter the password again:- ")

                                                if check_password==Password:
                                                    query="update Admin_register SET Password=%s WHERE Service_number=%s"
                                                    cur.execute(query,(Password_new,ser_no))
                                                    con.commit()

                                                    print("Password has been updated")
                                                    break
                                                else:
                                                    print("Password doesn't match, Try again.")
                                      
                                      else:
                                           print("The password should be of less than or equal to 15 characters.") 
                                 
                            elif update_type==4:

                                 while True:

                                      Phone_number_new=int(input("Enter new Phone Number:- "))

                                      #constraining possibilities
                                      if Phone_number_new in range(1000000000,10000000000):

                                             #check for uniqueness
                                             query="select Phone_number from Admin_register where Phone_number=%s" #uniqueness
                                             cur.execute(query,(Phone_number_new,))
                                             exist_phone_number=cur.fetchall()

                                             #if unique
                                             if exist_phone_number==[]:
                                                   query="update Admin_register SET Phone_number=%s WHERE Service_number=%s"
                                                   cur.execute(query,(Phone_number_new,ser_no))
                                                   con.commit()

                                                   print("Phone number has been updated")
                                                   break

                                             #if already exists
                                             else:
                                                  print("Account with this phone number alredy exists. Try another.")
                                             con.commit()
                                      #fixing number of digits
                                      else:
                                           print("The phone number should be of 10 digits.")
                                     
                            elif update_type==5:

                                 while True:
                                      Department_new=input("Enter new Department:- ")
                                      len_dept=len(Department_new)

                                       #fixing number of digits
                                      if len_dept<=100:

                                           #not null
                                           if len_dept==0:
                                                print("This field cannot be left empty!")
                                           else:
                                                query="update Admin_register SET Department=%s WHERE Service_number=%s"
                                                cur.execute(query,(Department_new,ser_no))
                                                con.commit()

                                                print("Department has been updated")
                                                break
                                       
                                      else:
                                           print("Maximum characters allowed = 100")                  
                                      
                            elif update_type==6:

                                 Address_new=input("Enter new Address:- ")
                                 len_add=len(Address_new)

                                 #fixing number of digits
                                 if len_add<=500:
                                       
                                      #not null
                                      if len_add==0:
                                           print("This field cannot be left empty!")
                                      else:
                                           query="update Admin_register SET Address=%s WHERE Service_number=%s"
                                           cur.execute(query,(Address_new,ser_no))
                                           con.commit()

                                           print("Address has been updated")
                                           break
                                 else:
                                      print("Address cannot be of more than 500 characters.")
                                 
                            elif update_type==7:

                                 break

                            else:

                                 print("Please enter a valid integer!!!")

                  elif log_task==3:
                      query="SELECT * FROM Client_register"
                      cur.execute(query,)
                      cln_data=cur.fetchall()
                
                      print(tabulate(cln_data, headers=["Account_number","Client_name","Client_username","Password","PhoneNo","PIN","Address"],tablefmt='grid'))

                  elif log_task==4:
                      query="SELECT * FROM Savings_account"
                      cur.execute(query,)
                      cln_sav=cur.fetchall()
                      print(tabulate(cln_sav, headers=["Account_number","Amount"],tablefmt='grid'))
                      

                      

                  elif log_task==5:
                      query="SELECT * FROM fd_account"
                      cur.execute(query,)
                      cln_fd=cur.fetchall()
                      print(tabulate(cln_fd, headers=["Account_number","Principal","Interest","Time Period","Return Amount"],tablefmt='grid'))

                      

                  elif log_task==6:
                      query="SELECT * FROM Loan_account"
                      cur.execute(query,)
                      cln_loan=cur.fetchall()
                      print(tabulate(cln_loan, headers=["Account_number","Principal","Interest","Time Period","Repayment Amount","Collateral"],tablefmt='grid'))




                  elif log_task==7:
                      query="SELECT * FROM Salary_account"
                      cur.execute(query,)
                      cln_sal=cur.fetchall()
                      print(tabulate(cln_sal, headers=["Account_number","Organisation","Total Salary","Tax","Total Taxed Amount","Inhand salary"],tablefmt='grid'))



                  elif log_task==8:
                       print("You have been signed out!")
                       sys.exit()


                  
                  elif log_task==9:
                      print("-"*25,"DELETING ACCOUNT","-"*25)
                      uname=input("Enter Admin username to be deleted:")
                      query="DELETE FROM Admin_register WHERE Admin_username=%s;"
                      cur.execute(query,(uname,))
                      con.commit()
                      print("Account Deleted Successfully.")
                      break
                  else:
                      print("Wrong input!!!")



    elif login_type==2:
        print("-"*25,"CLIENT LOGIN","-"*25)
        while True:
          Client_username=input("Enter your username:- ")
          Password=input("Enter your password:- ")

           #cross check with database
              #Password
          query="select Password from Client_register where Client_username=%s"
          cur.execute(query,(Client_username,))
          allow_Client_pass=cur.fetchall()
              #Username
          query="select Client_username from Client_register where Password=%s"
          cur.execute(query,(Password,))
          allow_Client_username=cur.fetchall()
         
          #sub-menu if logging unsucessful
          if allow_Client_username==[] or allow_Client_pass==[]:
              print("Incorrect Username or Password!")
              print("1. Forgot Username or password")
              print("2. Retry")
              print("3. Exit")

              while True:
                   reject_Client=int(input("Enter the choice(corresponding integer):- "))
                    #Forgotten Password and username
                   if reject_Client==1:
                        forgot_Acc=int(input("Enter your Account number:- "))
                        forgot_Phone=int(input("Enter your Phone number:- "))
                         
                         #fetching username
                        query="select Client_username from Client_register where Account_number=%s and Phone_number=%s"
                        cur.execute(query,(forgot_Acc,forgot_Phone,))
                        forgot_Cln_username=cur.fetchall()
                        con.commit()
 
                         #fetching password
                        query="select Password from Client_register where Account_number=%s and Phone_number=%s"
                        cur.execute(query,(forgot_Acc,forgot_Phone,))
                        forgot_Cln_password=cur.fetchall()
                        con.commit()
                         #displaying results
                        try:
                             print("Your username is",forgot_Cln_username[0][0],"and your password is",forgot_Cln_password[0][0])
                             break
                        except:
                              print("No such Admin exists. Try registering before logging in.")
                              Cln_logged=0
                    #to re-enter the details
                   elif reject_Client==2:
                        break
                    
                    #taking to 1st page interface
                   elif reject_Client==3:
                        sys.exit()
 
                         #avoiding error
                   else:
                         print("Enter a valid integer!!!")
 
          #logging succesful
          elif allow_Client_pass[0][0]==Password:
              query="select Client_name from Client_register where Client_username=%s"
              cur.execute(query,(Client_username,))
              Client_name=cur.fetchall()
              con.commit()
              
              print("WELCOME",Client_name[0][0],"to the Banque de Coester Vista Portal")
              query="select Account_number from Client_register where Client_username=%s"
              cur.execute(query,(Client_username,))
              Account_number=cur.fetchall()
              con.commit()

              acc_no=Account_number[0][0]
              Cln_logged=1
              break
            
        if Cln_logged!=0:
             while True:
                  print("1. View personal details")
                  print("2. Update your details")
                  print("3. Manage accounts")
                  print("4. Sign Out")
                  print("5. Delete Account")
                  log_task=int(input("Enter your choice:- "))

                  
                  if log_task==1:
                      print("-"*25,"PERSONAL DETAILS","-"*25)
                      query="SELECT * FROM client_register where Account_number=%s;"
                      cur.execute(query,(Account_number[0][0],))
                      data=cur.fetchall()
                      con.commit()
                      print(tabulate(data, headers=["Account_number","Client_name","Client_username","Password","PhoneNo","PIN","Address"],tablefmt='grid'))


                  elif log_task==2:
                       while True:

                            print("-"*25,"UPDATE DATA","-"*25) 

                            print("1. Client name")

                            print("2. Client username")

                            print("3. Password")

                            print("4. Phone number")

                            print("5. PIN")

                            print("6. Address")

                            print("7. Exit")

                            update_type=int(input("Choose the data which you want to update(corresponding integer):- "))

                            if update_type==1:

                                 while True:
                                      Client_name_new=input("Enter new name:- ")
                                      len_client=len(Client_name_new)

                                       #fixing number of digits
                                      if len_client<=100:
                                           
                                       #not null
                                           if len_client==0:
                                                print("This field cannot be left empty!")

                                           else:
                                                 query="update Client_register SET Client_name=%s WHERE Account_number=%s"
                                                 cur.execute(query,(Client_name_new,acc_no))
                                                 con.commit()

                                                 print("Client name has been updated.")
                                                 break
                                            
                                       #avoiding errors
                                      else:
                                           print("Maximum characters allowed = 100")

                                
                            elif update_type==2:

                                 while True:
                                      Client_username_new=input("Enter new Username:- ")
                                      len_username=len(Client_username_new)

                                      #fixing number of digits
                                      if len_username<=100:

                                           #not null
                                           if len_username==0:
                                                print("This field cannot be left empty!")

                                           #cross with database
                                           else:
                                                #check for uniqueness
                                                query="select Client_username from Client_register where Client_username=%s" #uniqueness
                                                cur.execute(query,(Client_username_new,))
                                                exist_Client_username=cur.fetchall()

                                                #if unique
                                                if exist_Client_username==[]:
                                                    query="update Client_register SET Client_username=%s WHERE Account_number=%s"
                                                    cur.execute(query,(Client_username_new,acc_no))
                                                    con.commit()

                                                    print("Username has been updated")
                                                    break

                                                #if already exists
                                                else:
                                                    print("Username alredy exists. Try another.")
                                                con.commit()
                                      
                                      else:
                                           print("Maximum characters allowed = 100")
                                      
                            elif update_type==3:

                                 while True:

                                      Password_new=input("Enter new Password:- ")
                                      len_pass=len(Password_new)

                                      #fixing number of digits
                                      if len_pass<=15:
                                           if len_pass==0:
                                                print("This field cannot be left empty!")

                                           elif len_pass<=5:
                                                print("Password too weak. Min length= 6")

                                           else:
                                                #confirm password
                                                check_password=input("Enter the password again:- ")

                                                if check_password==Password_new:
                                                    query="update Client_register SET Password=%s WHERE Account_number=%s"
                                                    cur.execute(query,(Password_new,acc_no))
                                                    con.commit()

                                                    print("Password has been updated")
                                                    break
                                                else:
                                                    print("Password doesn't match, Try again.")
                                      
                                      else:
                                           print("The password should be of less than or equal to 15 characters.") 
                                 
                            elif update_type==4:

                                 while True:

                                      Phone_number_new=int(input("Enter new Phone Number:- "))

                                      #constraining possibilities
                                      if Phone_number_new in range(1000000000,10000000000):

                                             #check for uniqueness
                                             query="select Phone_number from Client_register where Phone_number=%s" #uniqueness
                                             cur.execute(query,(Phone_number_new,))
                                             exist_phone_number=cur.fetchall()

                                             #if unique
                                             if exist_phone_number==[]:
                                                   query="update Client_register SET Phone_number=%s WHERE Account_number=%s"
                                                   cur.execute(query,(Phone_number_new,acc_no))
                                                   con.commit()

                                                   print("Phone number has been updated")
                                                   break

                                             #if already exists
                                             else:
                                                  print("Account with this phone number alredy exists. Try another.")
                                             con.commit()
                                      #fixing number of digits
                                      else:
                                           print("The phone number should be of 10 digits.")
                                     
                            elif update_type==5:

                                 while True:
                                      PIN_new=int(input("Enter the new 4-digit PIN:- "))
                                      
                                      #constrainging possibilities
                                      if PIN_new in range(1000,10000):
                                           confirm_pin=int(input("Confirm the PIN:- "))

                                           #conform pin
                                           if confirm_pin==PIN_new:
                                               query="update Client_register SET PIN=%s WHERE Account_number=%s"
                                               cur.execute(query,(PIN_new,acc_no))
                                               con.commit()

                                               print("PIN has been updated")
                                               break
                                           else:
                                               print("PIN does not match. Try Again")
                                      #fixing number of digits
                                      else:
                                           print("The pin should be of 4 digits only.")                  
                                      
                            elif update_type==6:

                                 Address_new=input("Enter new Address:- ")
                                 len_add=len(Address_new)

                                 #fixing number of digits
                                 if len_add<=500:
                                       
                                      #not null
                                      if len_add==0:
                                           print("This field cannot be left empty!")
                                      else:
                                           query="update Client_register SET Address=%s WHERE Account_number=%s"
                                           cur.execute(query,(Address_new,acc_no))
                                           con.commit()

                                           print("Address has been updated")
                                           break
                                 else:
                                      print("Address cannot be of more than 500 characters.")
                                 
                            elif update_type==7:

                                 break

                            else:

                                 print("Please enter a valid integer!!!")


                  elif log_task==3:
                      print("-"*25,"MANAGE ACCOUNTS","-"*25)
                      while True:
                          print("1. Savings Account")
                          print("2. Fixed Deposit(Simple interest)")
                          print("3. Loan(Simple Interest)")
                          print("4. Salary Account")
                          print("5. Money Transfer")
                          print("6. Exit")

                          acc_type=int(input("Enter your choice(1-5):- "))

                          if acc_type==1:
                              print("-"*25,"SAVINGS ACCOUNT","-"*25)
                              print("1. Add Money")
                              print("2. Check Balance")
                              print("3. Exit")
                              func=int(input("Enter your choice:- "))
                              if func==1:
                                  amt=float(input("Enter total amount to be added:- "))
                                  try:
                                      query="insert into savings_account values(%s,%s)"
                                      cur.execute(query,(acc_no,amt))
                                      con.commit()
                                  except:
                                      query="update savings_account set amount=amount+%s where account_number=%s"
                                      cur.execute(query,(amt,acc_no))
                                      con.commit()
                                  print("Amount added successfully!!!")
                              elif func==2:
                                  query="SELECT SUM(AMOUNT) FROM savings_account WHERE Account_number=%s"
                                  cur.execute(query,(acc_no,))
                                  bal=cur.fetchall()
                                  con.commit()
                                  print("The total balance is",bal[0][0])
                              elif func==3:
                                  break
                              else:
                                  print("Wrong input!!!")

                          elif acc_type==2:
                              print("-"*25,"FIXED DEPOSIT","-"*25)
                              print("1. Create fixed deposit")
                              print("2. View fixed deposits")
                              print("3. EXIT")
                              func=int(input("Enter your choice:- "))
                              if func==1:
                                  prin=int(input("Enter principal amount:- "))
                                  time=float(input("Enter total time period(in years):- "))
                                  query="insert into fd_account values(%s,%s,%s,%s,%s)"
                                  cur.execute(query,(acc_no,prin,time,7,prin+7*prin*time/100))
                                  con.commit()
                                  print("FD created successfully!!!")
                              elif func==2:
                                  query="SELECT * FROM fd_account where Account_number=%s"
                                  cur.execute(query,(acc_no,))
                                  ret_amt=cur.fetchall()
                                  con.commit()
                                  print(tabulate(ret_amt, headers=["Account_number","Principal","Interest","Time Period","Return Amount"],tablefmt='grid'))

                              elif func==3:
                                  break
                              else:
                                  print("Wrong input!!!")                                
                              
                              
                          elif acc_type==3:                             
                              print("-"*25,"LOAN","-"*25)
                              print("1. Apply for loan")
                              print("2. View loan details")
                              print("3. EXIT")
                              func=int(input("Enter your choice:- "))
                              if func==1:
                                  prin=int(input("Enter principal amount:- "))
                                  time=float(input("Enter total time period for repayment(in years):- "))
                                  coll=input("Mention a collateral(with estimated value):- ")
                                  query="insert into loan_account values(%s,%s,%s,%s,%s,%s)"
                                  cur.execute(query,(acc_no,prin,13,time,prin+13*prin*time/100,coll))
                                  con.commit()
                                  print("Loan Sanctioned!!!")
                              elif func==2:
                                  query="SELECT * FROM loan_account where Account_number=%s"
                                  cur.execute(query,(acc_no,))
                                  rep_amt=cur.fetchall()
                                  con.commit()
                                  print(tabulate(rep_amt, headers=["Account_number","Principal","Interest","Time Period","Repayment Amount","Collateral"],tablefmt='grid'))

                              elif func==3:
                                  break
                              else:
                                  print("Wrong input!!!")      
                              
                          elif acc_type==4:
                              print("-"*25,"SALARY ACCOUNT","-"*25)
                              print("1. Add salary details")
                              print("2. View salary details")
                              print("3. EXIT")
                              func=int(input("Enter your choice:- "))
                              if func==1:
                                  org=input("Name of organisation:- ")
                                  t_sal=float(input("Enter total salary:- "))
                                  taxpay=0.15*t_sal
                                  in_sal=t_sal-taxpay
                                  query="insert into salary_account values(%s,%s,%s,%s,%s,%s)"
                                  cur.execute(query,(acc_no,org,t_sal,15,taxpay,in_sal))
                                  con.commit()
                                  print("Salary Details added!!!")
                              elif func==2:
                                  query="SELECT * FROM salary_account where Account_number=%s"
                                  cur.execute(query,(acc_no,))
                                  det=cur.fetchall()
                                  con.commit()
                                  print(tabulate(det, headers=["Account_number","Organisation","Total Salary","Tax","Total Taxed Amount","Inhand salary"],tablefmt='grid'))

                              elif func==3:
                                  break
                              else:
                                  print("Wrong input!!!")

                          elif acc_type==5:
                              print("-"*25,"MONEY TRANSFER","-"*25)
                              to_acc=int(input("Enter account number of recipient:- "))
                              to_amt=float(input("Enter amount to be sent:- "))
                              pin_conf=int(input("Enter your PIN:- "))
                              query="select PIN from Client_register where Client_username=%s"
                              cur.execute(query,(Client_username,))
                              pin_pass=cur.fetchall()
                              con.commit()
                              
                              if pin_pass[0][0]==pin_conf:
                                  query="update savings_account set amount=amount-%s where account_number=%s"
                                  cur.execute(query,(to_amt,acc_no))
                                  con.commit()
                                  query="update savings_account set amount=amount+%s where account_number=%s"
                                  cur.execute(query,(to_amt,to_acc))
                                  con.commit()
                                  print("Amount transferred successfully!!!")
                                 
                              else:
                                  print("Incorrect PIN!!!")
                                  
                              
                          elif acc_type==6:
                              break
                              
                          else:
                              print("Wrong Choice!!!")

                                

                  elif log_task==4:
                       print("You have been signed out!")
                       sys.exit()

                  
                  elif log_task==5:
                      print("-"*25,"DELETING ACCOUNT","-"*25)
                      uname=input("Enter Client username to be deleted:")
                      query="DELETE FROM Client_register WHERE Client_username=%s;"
                      cur.execute(query,(uname,))
                      con.commit()
                      print("Account Deleted Successfully.")
                      break

                  else:
                      print("Wrong input!!!")
     
        

    elif login_type==3:
        print("-"*25,"ADMIN REGISTRATION","-"*25)
        #Service_number
        while True:
            
            Service_number=int(input("Enter your Service ID number(in 4 digits):- "))
            
            #constraining possibilities
            if Service_number in range(1000,10000):

                 #check for uniqueness
                 query="select Service_number from Admin_register where Service_number=%s"
                 cur.execute(query,(Service_number,))
                 exist_Service_number=cur.fetchall()

                 #if unique
                 if exist_Service_number==[]:
                     break

                 #if already exists
                 else:
                     print("Account with this Service number alredy exists. Try another.")
                 con.commit()

            #fixing number of digits
            else:
                 
                 print("Please use 4 digits.")

        #Staff_name
        while True:
             Staff_name=input("Enter your name:- ")
             len_staff=len(Staff_name)

             #fixing number of digits
             if len_staff<=100:
             #not null
                  if len_staff==0:
                       print("This field cannot be left empty!")

                  else:
                       break
                       
             #avoiding errors
             else:
                  print("Maximum characters allowed = 100")

        #Admin_username
        while True:
            Admin_username=input("Enter a username:- ")
            len_username=len(Admin_username)

            #fixing number of digits
            if len_username<=100:

                 #not null
                 if len_username==0:
                      print("This field cannot be left empty!")

                 #cross with database
                 else:
                      #check for uniqueness
                      query="select Admin_username from Admin_register where Admin_username=%s" #uniqueness
                      cur.execute(query,(Admin_username,))
                      exist_Admin_username=cur.fetchall()

                      #if unique
                      if exist_Admin_username==[]:
                          print("Username accepted")
                          break

                      #if already exists
                      else:
                          print("Username alredy exists. Try another.")
                      con.commit()
            
            else:
                 print("Maximum characters allowed = 100")

        #Password
        while True:
            Password=input("Set password (min 6, max 15 characters):- ")
            len_pass=len(Password)

            #fixing number of digits
            if len_pass<=15:
                 if len_pass==0:
                      print("This field cannot be left empty!")

                 elif len_pass<=5:
                      print("Password too weak. Min length= 6")

                 else:
                      #confirm password
                      check_password=input("Enter the password again:- ")

                      if check_password==Password:
                          print("Password created")
                          break
                      else:
                          print("Password doesn't match, Try again.")
            
            else:
                 print("The password should be of less than or equal to 15 characters.") 

        #Phone_number
        while True:
            Phone_number=int(input("Enter a 10 digit phone number:- "))
            
            #constraining possibilities
            if Phone_number in range(1000000000,10000000000):

                   #check for uniqueness
                   query="select Phone_number from Admin_register where Phone_number=%s" #uniqueness
                   cur.execute(query,(Phone_number,))
                   exist_phone_number=cur.fetchall()

                   #if unique
                   if exist_phone_number==[]:
                        break

                   #if already exists
                   else:
                        print("Account with this phone number alredy exists. Try another.")
                   con.commit()
            #fixing number of digits
            else:
                 print("The phone number should be of 10 digits.")
                 

        #Department
        while True:         
             Department=input("Enter the department you serve:- ")
             len_dept=len(Department)

             #fixing number of digits
             if len_dept<=100:

                  #not null
                  if len_dept==0:
                       print("This field cannot be left empty!")
                  else:
                       break
             
             else:
                  print("Maximum characters allowed = 100")
        #Address
        while True:
             Address=input("Please enter your Address:- ")
             len_add=len(Address)

             #fixing number of digits
             if len_add<=500:
                  
                  #not null
                  if len_add==0:
                       print("This field cannot be left empty!")
                  else:
                       break
             else:
                  print("Address cannot be of more than 500 characters.")

        print("Please remember the details for future references!")
        query="Insert into Admin_register values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(Service_number,Staff_name,Admin_username,Password,Phone_number,Department,Address,))
        con.commit()
        print("Your user account has been created. Go to the login page.")

        

    elif login_type==4:
        print("-"*25,"CLIENT REGISTRATION","-"*25)
        #Account_number
        while True:
            Account_number=random.randint(10000,99999)

            #check for uniqueness
            query="select Account_number from Client_register where Account_number=%s" #uniqueness
            cur.execute(query,(Account_number,))
            exist_Account_number=cur.fetchall()

            #if unique
            if exist_Account_number==[]:
                print("Your Account number is",Account_number)
                print("You are requested to note this for future reference")
                break

            #if already exists
            else:
                pass
            con.commit()

        #Client_name
        while True:
             Client_name=input("Enter your name:- ")
             len_client=len(Client_name)

             #fixing number of digits
             if len_client<=100:
                  
                  #not null
                  if len_client==0:
                       print("This field cannot be left empty!")
                  else:
                       break
             else:
                  print("Maximum characters allowed = 100")


        #Client_username
        while True:
            Client_username=input("Enter a username:- ")
            len_username=len(Client_username)

            #fixing number of digits
            if len_username<=100:

                 #not null
                 if len_username==0:
                      print("This field cannot be left empty!")
                 else:

                      #check for uniqueness
                      query="select Client_username from Client_register where Client_username=%s" #uniqueness
                      cur.execute(query,(Client_username,))
                      exist_client_username=cur.fetchall()

                      #if unique
                      if exist_client_username==[]:
                          print("Username accepted")
                          break

                      #if already exists
                      else:
                          print("Username alredy exists. Try another.")
                      con.commit()
                 
            else:
                 print("Maximum characters allowed = 100")

        #Password
        while True:
            Password=input("Set password (min 6, max 15 characters):- ")
            len_pass=len(Password)

            #fixing number of digits
            if len_pass<=15:

              #not null
              if len_pass==0:
                   print("This field cannot be left empty!")
              else:
                   #confirm password
                   check_password=input("Enter the password again:- ")
                   if check_password==Password:
                        print("Password created")
                        break
                   else:
                        print("Password doesn't match, Try again.")
            else:
                   print("The password should be of less than or equal to 15 characters.") 

        #Phone_number
        while True:
            Phone_number=int(input("Enter a 10 digit phone number:- "))
            
            #constraining possibilities
            if Phone_number in range(1000000000,10000000000):

                 #check for uniqueness
                 query="select Phone_number from Client_register where Phone_number=%s" #uniqueness
                 cur.execute(query,(Phone_number,))
                 exist_phone_number=cur.fetchall()

                 #if unique
                 if exist_phone_number==[]:
                     break

                 #if already exists
                 else:
                     print("Account with this phone number alredy exists. Try another.")
                 con.commit()

            #fixing number of digits
            else:
                 print("The phone number should be of 10 digits.")

        #PIN
        while True:
            PIN=int(input("Enter a 4-digit PIN for permitting future transactions:- "))
            
            #constrainging possibilities
            if PIN in range(1000,10000):
                 confirm_pin=int(input("Confirm the PIN:- "))

                 #conform pin
                 if confirm_pin==PIN:
                     print("PIN created")
                     break
                 else:
                     print("PIN does not match. Try Again")
            #fixing number of digits
            else:
                 print("The pin should be of 4 digits only.")

        #Address
        while True:
             Address=input("Please enter your Address:- ")
             len_add=len(Address)
             #fixing number of digits
             if len_add<=500:

              #not null
                  if len_add==0:
                       print("This field cannot be left empty!")
                  else:
                       break
             else:
                   print("Address cannot be of more than 500 characters.")
        print("Please remember the details for future references!")

        query="Insert into Client_register values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(Account_number,Client_name,Client_username,Password,Phone_number,PIN,Address,))
        con.commit()
        print("Your user account has been created. Go to the login page.")



    elif login_type==5:
        print("Thank You!!!")
        input()
        sys.exit()
        


    else:
        print("Please enter a valid integer!!!")
        
        


