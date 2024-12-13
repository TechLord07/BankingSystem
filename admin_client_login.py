import mysql.connector as ms #for MySql
import sys


#connecting mysql
con=ms.connect(host="localhost",user="Arnav",password="13975",database="Banque_de_Vista")

if con.is_connected():
     pass

else:
     print("Error in Connection.")  

cur=con.cursor()



#logging Admin
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
                              return("Login failed")
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
                              return("Login failed")
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
              return(Account_number[0][0])
              break
