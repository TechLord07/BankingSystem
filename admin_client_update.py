#update module
import mysql.connector as ms
    
con=ms.connect(host="localhost",user="Arnav",password="13975",database="Banque_de_Vista")

if con.is_connected():
     pass

else:
     print("Error in Connection.")  

cur=con.cursor()



def Admin_update(ser_no):

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

             return

        else:

             print("Please enter a valid integer!!!")



def Client_update(acc_no):

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

             return

        else:

             print("Please enter a valid integer!!!")        
 
          
             
        
