import mysql.connector as m
from prettytable import PrettyTable
from getpass_asterisk.getpass_asterisk import getpass_asterisk
import os
import time

os.system('pip install prettytable mysql_connector getpass-asterisk')
os.system('cls')

sql_host=[]
sql_user=[]
sql_password=[]
sql_database=[]

def connect():
        os.system('cls')
        try:
                print("               Enter MySql/MariaDB Credentials :-                                             ")
                print()
                try:
                        cred_host = input("$~ Host: ")
                        sql_host.append(cred_host)
                        cred_user = input("$~ User: ")
                        sql_user.append(cred_user)
                        cred_password = getpass_asterisk("$~ Password: ")
                        sql_password.append(cred_password)
                        cred_database = input("$~ Database: ")
                        sql_database.append(cred_database)
                        print()
                        con=m.connect(host=sql_host[0],user=sql_user[0],password=sql_password[0])
                        if con.is_connected:
                                print("[...] Connected Successfully")
                except Exception as e:
                        print(str(e))
                cur=con.cursor()
                cur.execute('''show databases;''')
                data = cur.fetchall()
                for i in data:
                        for j in i:
                                if sql_database[0] == j:
                                        data_exist = True
                                        break
                if not data_exist:
                        d=input(f"[+] {sql_database[0]} Database doesn't exist ,want to create(type: y): ")
                        if d.lower() == 'y':
                                cur.execute(f'''create database {sql_database[0]};''')
                                print("[...] Database created successfully...")
                                print()
                        else:
                                pass
                                                      
        except Exception as e:
                print(str(e))  
        time.sleep(2)                     
        os.system('cls')

def create():
        data_exist = False
        os.system('cls')
        try:
                print("               CREATE TABLES :-                                             ")
                print()
                print("       1➔ Create table Book                       ")
                print("       2➔ Create table Seller                      ")
                print("       3➔ Create table Buyer                       ")
                print("       4➔ Exit                                     ")
                while True:
                        con=m.connect(host=sql_host[0],user=sql_user[0],password=sql_password[0],database = sql_database[0])
                        cur=con.cursor()
                        ch=int(input("[+] Enter The No ➔ "))
                        if ch==1:
                                cur.execute('''show tables;''')
                                data = cur.fetchall()
                                for i in data:
                                        for j in i:
                                                if j == 'book':
                                                        data_exist = True
                                                        print("Table Exist!")
                                                        print()
                                                        break
                                                else:
                                                        continue
                                if data_exist != True:
                                        d=input(f"[+] Table doesn't exist ,want to create(type: y): ")
                                        if d.lower() == 'y':
                                                cur.execute("""create table if not exists book(
                                                                No int primary key,
                                                                title varchar(120),
                                                                author varchar(120),
                                                                price decimal(30),
                                                                quantity int );               
                                                            """)
                                                print("[...] Table created successfully...")
                                                print()
                                        else:
                                                pass
                             
                        elif ch==2:
                                cur.execute('''show tables;''')
                                data = cur.fetchall()
                                for i in data:
                                        for j in i:
                                                if j == 'seller':
                                                                data_exist = True
                                                                print("Table Exist!")
                                                                print()
                                                                break
                                                else:
                                                        continue              
                                if data_exist != True:
                                        d=input(f"[+] Table doesn't exist ,want to create(type: y): ")
                                        if d.lower() == 'y':
                                                cur.execute("""create table if not exists seller(
                                                                        No int primary key,
                                                                        Title varchar(120),
                                                                        Author varchar(120),
                                                                        price decimal(30),
                                                                        Quantity int ,
                                                                        Seller_Name varchar(120),
                                                                        SellerNumber int );
                                                        """)
                                                print("[...] Table created successfully...")
                                                print()
                                        else:
                                                pass


                        elif ch==3:
                                cur.execute('''show tables;''')
                                data = cur.fetchall()
                                for i in data:
                                        for j in i:
                                                if j == 'buyer':
                                                                data_exist = True
                                                                print("Table Exist!")
                                                                print()
                                                                break
                                                else:
                                                        continue
                                if data_exist != True:
                                        d=input(f"[+] Table doesn't exist ,want to create(type: y): ")
                                        if d.lower() == 'y':
                                                cur.execute("""create table if not exists buyer(
                                                                        No int primary key,
                                                                        Title varchar(120),
                                                                        Author varchar(120),
                                                                        price decimal(30),
                                                                        Quantity int ,
                                                                        Buyer_Name varchar(120),
                                                                        BuyerNumber int,
                                                                        Buyer_Email varchar(120));
                                                        """)
                                                print("[...] Table created successfully...")
                                                print()
                                        else:
                                                pass
                                else:
                                        pass
                                
                        elif ch==4:
                                break
        except Exception as e:
                print(str(e))
        time.sleep(2)                     
        os.system('cls')

def add_book():
        os.system('cls')
        try:
                print("                              Insert Records :-                              ")
                print()
                print("       1➔ Insert into Book                         ")
                print("       2➔ Insert into Seller                       ")
                print("       3➔ Insert into Buyer                        ")
                print("       4➔ Exit                                     ")
                print()
                con=m.connect(host=sql_host[0],user=sql_user[0],password=sql_password[0],database = sql_database[0])
                cur=con.cursor()
                while True:
                        
                        ch=int(input("Enter The No ➔ "))
                        if ch==1:
                                No=int(input("Enter the book no ➔ "))
                                title = input("Enter the book title ➔ ")
                                author = input("Enter the author name ➔ ")
                                price = float(input("Enter the book price ➔ "))
                                quantity = int(input("Enter the book quantity ➔ "))

                                book=(No,title,author, price, quantity)

                                query = """
                                INSERT INTO book (No,title, author, price, quantity)
                                VALUES (%s,%s, %s, %s, %s)
                                """
                                values = (No,title,author,price,quantity)
                                cur.execute(query, values)
                                con.commit()
                                print(end='\n')
                                print("Book added successfully!")
                                print(end='\n')

                        elif ch==2:
                                No=int(input("Enter the book no ➔ "))
                                Title = input("Enter the book title ➔ ")
                                Author = input("Enter the author name ➔ ")
                                Price = float(input("Enter the book price ➔ "))
                                Quantity = int(input("Enter the book quantity ➔ "))
                                Seller_Name=input("Enter the Seller Name ➔ ")
                                SellerNumber=int(input("Enter the Seller Number ➔ "))

                                book=(No,Title,Author, Price, Quantity,Seller_Name,SellerNumber)

                                query = """
                                INSERT INTO seller (No,Title, Author, Price, Quantity,Seller_Name,SellerNumber)
                                VALUES (%s,%s, %s, %s, %s,%s,%s)
                                """
                                values = (No,Title,Author,Price,Quantity,Seller_Name,SellerNumber)
                                cur.execute(query, values)
                                con.commit()
                                print(end='\n')
                                print("Book added successfully!")
                                print(end='\n')

                        elif ch==3:
                                No=int(input("Enter the book no ➔ "))
                                Title = input("Enter the book title ➔ ")
                                Writer = input("Enter the author name ➔ ")
                                Price = float(input("Enter the book price ➔ "))
                                Quantity = int(input("Enter the book quantity ➔ "))
                                BuyerName=input("Enter the Buyer Name ➔ ")
                                BuyerNumber=int(input("Enter the Buyer Number ➔ "))
                                Buyer_Email=input("Entre the  Buyer Email ➔")

                                book=(No,Title,Writer, Price, Quantity,BuyerName,BuyerNumber,Buyer_Email)

                                query = """
                                INSERT INTO buyer (No,Title, Writer, Price, Quantity,BuyerName,BuyerNumber,Buyer_Email)
                                VALUES (%s,%s, %s, %s, %s,%s,%s,%s)
                                """
                                values = (No,Title,Writer,Price,Quantity,BuyerName,BuyerNumber,Buyer_Email)
                                cur.execute(query, values)
                                con.commit()
                                print(end='\n')
                                print("Book added successfully!")
                                print(end='\n')

                        elif ch==4:
                                break
        except Exception as e:
                print(str(e))
        time.sleep(2)                     
        os.system('cls')
     
def display():
        os.system('cls')
        try:
                print("                           CHOOSE TABLE FROM BELOW To See Records :-                                                     !!!")
                print()
                print("       1➔ Book                  ")
                print("       2➔ Seller                ")
                print("       3➔ Buyer                 ")
                print("       4➔ Exit                  ")
                con=m.connect(host=sql_host[0],user=sql_user[0],password=sql_password[0],database = sql_database[0])
                cur=con.cursor()
                while True:
                        
                        print(end='\n')
                        ch=int(input("Enter the No ➔ "))
                        print(end='\n')
                        if ch==1:
                                query = "SELECT  *  FROM book"
                                cur.execute(query)
                                rows = cur.fetchall()
                                table = PrettyTable()
                                table.field_names = [desc[0] for desc in cur.description]
                                for row in rows:
                                        table.add_row(row)
                                        print(table)
                                        print(end='\n')

                        elif ch==2:
                                query = "SELECT  *  FROM seller"
                                cur.execute(query,)
                                rows = cur.fetchall()
                                table = PrettyTable()
                                table.field_names = [desc[0] for desc in cur.description]
                                for row in rows:
                                        table.add_row(row)
                                        print(table)
                                        print(end='\n')

                        elif ch==3:
                                query = "SELECT  *  FROM buyer"
                                cur.execute(query,)
                                rows = cur.fetchall()
                                table = PrettyTable()
                                table.field_names = [desc[0] for desc in cur.description]
                                for row in rows:
                                        table.add_row(row)
                                        print(table)
                                        print(end='\n')

                        elif ch==4:
                                break
        except Exception as e:
                print(str(e))
        time.sleep(2)                     
        os.system('cls')

                

def search_book():
        os.system('cls')
        try:
                print("                      CHOOSE TABLE FROM BELOW To Search :-                    ")
                print()
                print("       1➔ Book                  ")
                print("       2➔ Seller                ")
                print("       3➔ Buyer                 ")
                print("       4➔ Exit                  ")
                print(end='\n')
                con=m.connect(host=sql_host[0],user=sql_user[0],password=sql_password[0],database = sql_database[0])
                cur=con.cursor()
                while True:
                        ch=int(input("Enter the No ➔ "))
                        print(end='\n')

                        if ch==1:
                                print("")
                                print("       1➔ Search by No,Price,Quantity                                    ")
                                print("       2➔ Search by Title,Author,                                        ")
                                print('')
                                ch=int(input("Enter the No  ➔ "))
                                print(end='\n')
                                if ch==1:
                                        title = int(input("Enter the No \ price \ quantity to search ➔ "))
                                        query = "SELECT * FROM book WHERE %s"
                                        value = (title,)
                                        cur.execute(query, value)
                                        book_data = cur.fetchone()
                                        if book_data:
                                                book = (book_data[0],book_data[1], book_data[2], book_data[3], book_data[4])
                                                print(book)
                                        else:
                                                print("Book not found in the inventory.")
                                                print(end='\n')

                                elif ch==2:
                                        title = input("Enter the  title \ author  to search ➔ ")
                                        query = "SELECT * FROM book WHERE %s"
                                        value = (title,)
                                        cur.execute(query, value)
                                        book_data = cur.fetchone()
                                        if book_data:
                                                book = (book_data[0],book_data[1], book_data[2], book_data[3], book_data[4])
                                                print(book)
                                        else:
                                                print("Book not found in the inventory.")
                                                print(end='\n')

                        elif ch==2:
                                print("")
                                print("       1➔ Search by No,Price,Quantity,SellerNumber                                                 ")
                                print("       2➔ Search by Title,Author,Seller_Name                                                       ")
                                print('')
                                ch=int(input("Enter the No  ➔ "))
                                print(end='\n')
                                if ch==1:
                                        title = int(input("Enter the No \ price \ quantity \ seller number to search ➔ "))
                                        query = "SELECT * FROM seller  where %s"
                                        value = (title,)
                                        cur.execute(query, value)
                                        book_data = cur.fetchone()
                                        if book_data:
                                                book = (book_data[0],book_data[1], book_data[2], book_data[3], book_data[4], book_data[5] )
                                                print(book)
                                        else:
                                                print("Book not found in the inventory.")
                                                print(end='\n')

                                elif ch==2:
                                        title = int(input("Enter the title \ author \seller_name to search ➔ "))
                                        query = "SELECT * FROM seller  where %s"
                                        value = (title,)
                                        cur.execute(query, value)
                                        book_data = cur.fetchone()
                                        if book_data:
                                                book = (book_data[0],book_data[1], book_data[2], book_data[3], book_data[4], book_data[5] )
                                                print(book)
                                        else:
                                                print("Book not found in the inventory.")
                                                print(end='\n')

                        elif ch==3:
                                print("")
                                print("       1➔ Search by BookNo,BuyerNumber,Price,Quantity                                                          ")
                                print("       2➔ Search by Title,Writer,BuyerName,BuyerEmail                                                          ")
                                print('')
                                ch=int(input("Enter the No  ➔ "))
                                print(end='\n')
                                if ch==1:
                                        title=int(input("Enter the book No , buyer number , price , quantity to search ➔ "))
                                        query = "SELECT * FROM buyer WHERE  %s"
                                        value = (title,)
                                        cur.execute(query, value)
                                        book_data = cur.fetchone()
                                        if book_data:
                                                book = (book_data[0],book_data[1], book_data[2], book_data[3], book_data[4], book_data[5],book_data[6],book_data[7] )
                                                print(book)
                                        else:
                                                print("Book not found in the inventory.")
                                                print(end='\n')


                                elif ch==2:
                                        title=input("Enter the buyer Name , title , writer , buyer Email  to search ➔ ")
                                        query = "SELECT * FROM buyer WHERE  %s"
                                        value = (title,)
                                        cur.execute(query, value)
                                        book_data = cur.fetchone()
                                        if book_data:
                                                book = (book_data[0],book_data[1], book_data[2], book_data[3], book_data[4], book_data[5],book_data[6],book_data[7] )
                                                print(book)
                                        else:
                                                print("Book not found in the inventory.")
                                                print(end='\n')

                        elif ch==4:
                                break
        except Exception as e:
                print(str(e))
        time.sleep(2)                     
        os.system('cls')                      

def update():
        os.system('cls')
        try:
                con=m.connect(host=sql_host[0],user=sql_user[0],password=sql_password[0],database = sql_database[0])
                cur=con.cursor()
                def init():
                        while True:
                                print("")
                                print("               CHOOSE TABLE FROM BELOW To Update Records :-                                             ")
                                print("")
                                print("")
                                print("       1➔ Book                  ")
                                print("       2➔ Seller                ")
                                print("       3➔ Buyer                 ")
                                print("       4➔ Exit                  ")
                                print("")
                                print(end='\n')
                                ch=int(input("Enter the No ➔ "))
                                print(end='\n')
                                if ch==1:
                                        while True:
                                        
                                                print("1➔ Change No " )
                                                print("2➔ Change Title ") 
                                                print("3➔ Change Author ")
                                                print("4➔ Change Price  ")
                                                print("5➔ Change Quantity ") 
                                                print("6➔ Exit  ")
                                                print()
                                                ch=int(input("Enter The No ➔ " ))
                                                print()
                                                if ch==1:
                                                        q=int(input("Enter the No ➔ "))
                                                        w=int(input("Enter the New No ➔ "))
                                                        s="""update book set No = '%s' where No = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==2:
                                                        q=input("Enter the Title ➔ ")
                                                        w=input("Enter the New Title ➔ ")
                                                        s="""update book set title = %s where title = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==3:
                                                        q=input("Enter the Author to change  ➔ ")
                                                        w=input("Enter the New Author ➔ ")
                                                        s="""update book set author = %s where author = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==4:
                                                        while True:
                                                                print("")
                                                                print("           1➔ Increase Price                         ")
                                                                print("           2➔ Decrease Price                         ")
                                                                print("           3➔ Exit                                   ")
                                                                print("")
                                                                ch=int(input("Enter the No ➔ "))
                                                                print()
                                                                def increment():
                                                                        q=input("Enter the Title ➔ ")
                                                                        w=float(input("Enter the Price to increase ➔ "))
                                                                        s="""update book set price = price+%s where title = %s"""
                                                                        value=(w,q)
                                                                        cur.execute(s,value)
                                                                        con.commit()
                                                                        if cur.rowcount==0:
                                                                                print()
                                                                                print("[...]  No Such Records Exist")
                                                                                print()
                                                                        else:
                                                                                print()
                                                                                print("[...]  Updated Successfully")
                                                                                print()
                                
                                                                def decrement():
                                                                        q=input("Enter the Title ➔ ")
                                                                        w=eval(input("Enter the Price to increase ➔ "))
                                                                        s="""update book set price = price-%s where title = %s"""
                                                                        value=(w,q)
                                                                        cur.execute(s,value)
                                                                        con.commit()
                                                                        if cur.rowcount==0:
                                                                                print()
                                                                                print("[...]  No Such Records Exist")
                                                                                print()
                                                                        else:
                                                                                print()
                                                                                print("[...]  Updated Successfully")
                                                                                print()
                                                                if ch==1:
                                                                        increment()
                                                                elif ch==2:
                                                                        decrement()
                                                                elif ch==3:
                                                                        break

                                                elif ch==5:
                                                        q=input("Enter the Title ➔ ")
                                                        w=int(input("Enter the Quantity to Update ➔ "))
                                                        s="""update book set quantity = %s where title = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()


                                                elif ch==6:
                                                        break
                                elif ch==2:
                                        while True:
                                                print("")
                                                print("     1➔ Change No            ")
                                                print("     2➔ Change Title         ")
                                                print("     3➔ Change Author        ")
                                                print("     4➔ Change Price         ")
                                                print("     5➔ Change Quantity      ")
                                                print("     6➔ Change Seller_Name   ")
                                                print("     7➔ Change SellerNumber  ")
                                                print("     8➔ Exit                 ")
                                                print("")
                                                ch=int(input("Enter The No ➔ " ))
                                                print()
                                                if ch==1:
                                                        q=int(input("Enter the No ➔ "))
                                                        w=int(input("Enter the New No ➔ "))
                                                        s="""update seller set No = '%s' where No = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()
                                                
                                                elif ch==2:
                                                        q=input("Enter the Title ➔ ")
                                                        w=input("Enter the New Title ➔ ")
                                                        s="""update seller set title = %s where title = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==3:
                                                        q=input("Enter the Author to change  ➔ ")
                                                        w=input("Enter the New Author ➔ ")
                                                        s="""update seller set author = %s where author = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==4:
                                                        while True:
                                                                print("")
                                                                print("           1➔ Increase Price                         ")
                                                                print("           2➔ Decrease Price                         ")
                                                                print("           3➔ Exit                                   ")
                                                                print("")
                                                                ch=int(input("Enter the No ➔ "))
                                                                print()
                                                                def increment():
                                                                        q=input("Enter the Title ➔ ")
                                                                        w=float(input("Enter the Price to increase ➔ "))
                                                                        s="""update seller set price = price+%s where title = %s"""
                                                                        value=(w,q)
                                                                        cur.execute(s,value)
                                                                        con.commit()
                                                                        if cur.rowcount==0:
                                                                                print()
                                                                                print("[...]  No Such Records Exist")
                                                                                print()
                                                                        else:
                                                                                print()
                                                                                print("[...]  Updated Successfully")
                                                                                print()
                                
                                                                def decrement():
                                                                        q=input("Enter the Title ➔ ")
                                                                        w=eval(input("Enter the Price to increase ➔ "))
                                                                        s="""update seller set price = price-%s where title = %s"""
                                                                        value=(w,q)
                                                                        cur.execute(s,value)
                                                                        con.commit()
                                                                        if cur.rowcount==0:
                                                                                print()
                                                                                print("[...]  No Such Records Exist")
                                                                                print()
                                                                        else:
                                                                                print()
                                                                                print("[...]  Updated Successfully")
                                                                                print()
                                                                if ch==1:
                                                                        increment()
                                                                elif ch==2:
                                                                        decrement()
                                                                elif ch==3:
                                                                        break

                                                elif ch==5:
                                                        q=input("Enter the Title ➔ ")
                                                        w=int(input("Enter the Quantity to Update ➔ "))
                                                        s="""update seller set quantity = %s where title = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()


                                                elif ch==6:
                                                        q=input("Enter the Title ➔ ")
                                                        w=int(input("Enter the Quantity to Update ➔ "))
                                                        s="""update seller set Seller_Name = %s where Seller_Name = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==7:
                                                        q=input("Enter the SellerNumber ➔ ")
                                                        w=int(input("Enter the Number to Update ➔ "))
                                                        s="""update seller set SellerNumber = %s where SellerNumber = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==8:
                                                        break

                                                        

                                                
                                elif ch==3:
                                        while True:
                                                print("1➔ Change No " )
                                                print("2➔ Change Title ") 
                                                print("3➔ Change Author ")
                                                print("4➔ Change Price  ")
                                                print("5➔ Change Quantity ")
                                                print("6➔ Change BuyerName")
                                                print("7➔ Change BuyerNumber")
                                                print("8➔ Change Buyer_Email")
                                                print("9➔ Exit  ")
                                                print()
                                                ch=int(input("Enter The No ➔ " ))
                                                print()
                                                if ch==1:
                                                        q=int(input("Enter the No ➔ "))
                                                        w=int(input("Enter the New No ➔ "))
                                                        s="""update buyer set No = '%s' where No = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()
                                                
                                                elif ch==2:
                                                        q=input("Enter the Title ➔ ")
                                                        w=input("Enter the New Title ➔ ")
                                                        s="""update buyer set title = %s where title = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==3:
                                                        q=input("Enter the Author to change  ➔ ")
                                                        w=input("Enter the New Author ➔ ")
                                                        s="""update buyer set author = %s where author = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==4:
                                                        while True:
                                                                print("")
                                                                print("           1➔ Increase Price                         ")
                                                                print("           2➔ Decrease Price                         ")
                                                                print("           3➔ Exit                                   ")
                                                                print("")
                                                                ch=int(input("Enter the No ➔ "))
                                                                print()
                                                                def increment():
                                                                        q=input("Enter the Title ➔ ")
                                                                        w=float(input("Enter the Price to increase ➔ "))
                                                                        s="""update buyer set price = price+%s where title = %s"""
                                                                        value=(w,q)
                                                                        cur.execute(s,value)
                                                                        con.commit()
                                                                        if cur.rowcount==0:
                                                                                print()
                                                                                print("[...]  No Such Records Exist")
                                                                                print()
                                                                        else:
                                                                                print()
                                                                                print("[...]  Updated Successfully")
                                                                                print()
                                
                                                                def decrement():
                                                                        q=input("Enter the Title ➔ ")
                                                                        w=eval(input("Enter the Price to increase ➔ "))
                                                                        s="""update buyer set price = price-%s where title = %s"""
                                                                        value=(w,q)
                                                                        cur.execute(s,value)
                                                                        con.commit()
                                                                        if cur.rowcount==0:
                                                                                print()
                                                                                print("[...]  No Such Records Exist")
                                                                                print()
                                                                        else:
                                                                                print()
                                                                                print("[...]  Updated Successfully")
                                                                                print()
                                                                if ch==1:
                                                                        increment()
                                                                elif ch==2:
                                                                        decrement()
                                                                elif ch==3:
                                                                        break

                                                elif ch==5:
                                                        q=input("Enter the Title ➔ ")
                                                        w=int(input("Enter the Quantity to Update ➔ "))
                                                        s="""update buyer set quantity = %s where title = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()


                                                elif ch==6:
                                                        q=input("Enter the BuyerName ➔ ")
                                                        w=int(input("Enter the New BuyerName ➔ "))
                                                        s="""update buyer set BuyerName = %s where BuyerName = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==7:
                                                        q=int(input("Enter the BuyerNumber ➔ "))
                                                        w=int(input("Enter the New Number ➔ "))
                                                        s="""update buyer set BuyerNumber = %s where BuyerNumber = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()

                                                elif ch==8:
                                                        q=input("Enter the Buyer_Email ➔ ")
                                                        w=int(input("Enter the New Email ➔ "))
                                                        s="""update buyer set Buyer_Email = %s where Buyer_Email = %s"""
                                                        value=(w,q)
                                                        cur.execute(s,value)
                                                        con.commit()
                                                        if cur.rowcount==0:
                                                                print()
                                                                print("[...]  No Such Records Exist")
                                                                print()
                                                        else:
                                                                print()
                                                                print("[...]  Updated Successfully")
                                                                print()


                                                elif ch==9:
                                                        break

                                elif ch==4:
                                        break
                init()
        except Exception as e:
                print(str(e))
        time.sleep(2)                     
        os.system('cls')        
    
def delete():
        os.system('cls')
        try:
                con=m.connect(host=sql_host[0],user=sql_user[0],password=sql_password[0],database = sql_database[0])
                cur=con.cursor()
                while True:
                        print("")
                        print("       1➔ Delete From Book                         ")
                        print("       2➔ Delete From Seller                       ")
                        print("       3➔ Delete From Buyer                        ")
                        print("       4➔ Exit                                     ")
                        print("")
                        ch=int(input("Enter The No➔"))
                        print(end='\n')
                        if ch==1:
                                print("")
                                print("       1➔ Search by No,Price,Quantity                                    ")
                                print("       2➔ Search by Title,Author,                                        ")
                                print('')
                                ch=int(input("Enter the No  ➔ "))
                                print(end='\n')
                                if ch==1:
                                        q=int(input("Enter the No \ price \ quantity ➔ "))
                                        s='''delete from book where %s'''
                                        value=(q,)
                                        cur.execute(s,value)
                                        con.commit()
                                        if cur.rowcount==0:
                                                print("[...]  No Such Records Exist")
                                        else:
                                                print("[...]  Row Deleted")
                                                print(end='\n')

                                elif ch==2:
                                        q=int(input("Enter the Title \ author ➔ "))
                                        s='''delete from book where %s'''
                                        value=(q,)
                                        cur.execute(s,value)
                                        con.commit()
                                        if cur.rowcount==0:
                                                print("[...]  No Such Records Exist")
                                        else:
                                                print("[...]  Row Deleted")
                                                print(end='\n')

                        elif ch==2:
                                print("")
                                print("       1➔ Search by No,Price,Quantity,SellerNumber                                                 ")
                                print("       2➔ Search by Title,Author,Seller_Name                                                       ")
                                print('')
                                ch=int(input("Enter the No  ➔ "))
                                print(end='\n')
                                if ch==1:
                                        q=int(input("Enter the No \ price \ quantity \ Seller Number ➔ "))
                                        s='''delete from book where %s'''
                                        value=(q,)
                                        cur.execute(s,value)
                                        con.commit()
                                        if cur.rowcount==0:
                                                print("[...]  No Such Records Exist")
                                        else:
                                                print("[...]  Row Deleted")
                                                print(end='\n')
                                elif ch==2:
                                        q=int(input("Enter the Title \ author \ Seller_Name ➔ "))
                                        s='''delete from seller where %s'''
                                        value=(q,)
                                        cur.execute(s,value)
                                        con.commit()
                                        if cur.rowcount==0:
                                                print("[...]  No Such Records Exist")
                                        else:
                                                print("[...]  Row Deleted")
                                                print(end='\n')
                                        

                        elif ch==3:
                                print("")
                                print("       1➔ Search by BookNo,BuyerNumber,Price,Quantity                                                          ")
                                print("       2➔ Search by Title,Writer,BuyerName,BuyerEmail                                                          ")
                                print('')
                                ch=int(input("Enter the No  ➔ "))
                                print(end='\n')
                                if ch==1:
                                        q=int(input("Enter the No \ buyer number \ price \ quantity ➔ "))
                                        s='''delete from buyer where %s'''
                                        value=(q,)
                                        cur.execute(s,value)
                                        con.commit()
                                        if cur.rowcount==0:
                                                print("[...]  No Such Records Exist")
                                        else:
                                                print("[...]  Row Deleted")
                                                print(end='\n')

                                elif ch==2:
                                        q=int(input("Enter the Title \ writer \ buyer name \ buyer email ➔ "))
                                        s='''delete from buyer where %s'''
                                        value=(q,)
                                        cur.execute(s,value)
                                        con.commit()
                                        if cur.rowcount==0:
                                                print("[...]  No Such Records Exist")
                                        else:
                                                print("[...]  Row Deleted")
                                                print(end='\n')

                                        

                        elif ch==4:
                                break
        except Exception as e:
                print(str(e))
        time.sleep(2)                     
        os.system('cls')
                                                 
while True:
        try:
                print('''                ♱   WELCOME  TO  BOOK SHOP  MANAGEMENT  SYSTEM   ♱                            ''')
                print()
                print()
                print("1➔ Connect Mysql")
                print("2➔ Create Tables")
                print("3➔ INSERT Into Record")
                print("4➔ DISPLAY Record")
                print("5➔ UPDATE Record")
                print("6➔ DELETE Record")
                print("7➔ SEARCH Book")
                print("8➔ EXIT")
                print(end='\n')
                ch=int(input("Enter The Number ➔ "))
                print()
                if ch==1:
                        connect()
                elif ch==2:
                        create()
                elif ch==3:
                        add_book()
                elif ch==4:
                        display()
                elif ch==5:
                        update()
                elif ch==6:
                        delete()
                elif ch==7:
                        search_book()
                elif ch==8:
                        print(end='\n')
                        print("THANK YOU FOR VISITING")
                        break
        except Exception as e:
                print(str(e))