import random                #for Acc no
import mysql.connector as ms #for MySql


#connecting mysql
con=ms.connect(host="localhost",user="Arnav",password="13975",database="Banque_de_Vista")

if con.is_connected():
     pass

else:
     print("Error in Connection.")  

cur=con.cursor()



#registering admin
def Admin_register():

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

     return(Service_number,Staff_name,Admin_username,Password,Phone_number,Department,Address)

     

#registering client 
def Client_register():

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
    return(Account_number,Client_name,Client_username,Password,Phone_number,PIN,Address)


'''#logging Admin
def Admin_login():

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
                   print("3. Go back to main menu")
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
                              return("Login failed")
                    #to re-enter the details
                   elif reject_Admin==2:
                        break
                    
                    #taking to 1st page interface
                   elif reject_Admin==3:
                        return("Login failed")
 
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

              #global log
              #log='Success'
              query="select Service_number from Admin_register where Admin_username=%s"
              cur.execute(query,(Admin_username,))
              Service_number=cur.fetchall()
              con.commit()
              return(Service_number[0][0])



#logging client
def Client_login():

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
              print("3. Go back to main menu")

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
                              return("Login failed")
                    #to re-enter the details
                   elif reject_Client==2:
                        break
                    
                    #taking to 1st page interface
                   elif reject_Client==3:
                        return("Login failed")
 
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
              return(Account_number[0][0])
              break'''
                      
                 
    


