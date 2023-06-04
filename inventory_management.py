import mysql.connector as myconn
from tabulate import tabulate

def show_data():
    mycon.execute("SELECT * FROM warehouse;")
    data = mycon.fetchall()
    return data
def insert():
    name = input('enter the name of item : ')
    quant = int(input('enter the quantity : '))
    category = input("choose kg or l or pcs : ")
    sql = "INSERT INTO warehouse VALUES (%s, %s, %s, %s);" 
    val = (0,name,quant,category)
    mycon.execute(sql,val)
    conn.commit()  
    return True
def update():
    id = int(input('enter the unique id of item : '))
    use = int(input('enter the amount you want to use : '))
    sql = "SELECT QUANTITY from warehouse WHERE (id = %s);"
    val = [id]
    query =  mycon.execute(sql,val)
    num = mycon.fetchone()
    if int(num[0])>use:
        new_qt = int(num[0])-use
        _sql = 'UPDATE warehouse SET QUANTITY = %s WHERE (id = %s);'
        _val = (new_qt,id)
        query1 = mycon.execute(_sql,_val)
        conn.commit()
        a = 'list updated'
    else:
        a = 'insufficient amount'
        return a

def update2():
    id = int(input('\nenter the id of the product : '))
    name = input("enter the new name of item : ")
    quant = int(input("enter the new amount of item : "))
    category = input("enter the new category of item : ")
    sql = "UPDATE warehouse SET NAME = %s , QUANTITY = %s, CATEGORY = %s WHERE (id = %s);"
    val = (name,quant,category,id)
    query = mycon.execute(sql,val)
    conn.commit()
    return True  
    
conn = myconn.connect(user='root',host='localhost',password='1234', port='3307',database='inventory')
mycon = conn.cursor() 

while True:
    choice = input("\nenter what function wanna perform \n 1: insert data \n 2: see all data \n 3: update data \n 4: use items \n 5:exit :\n ")

    if choice== '1':
        insert()
        print("inventory updated...\n")
    elif choice== '2':
        x=show_data()
        print(tabulate(x, headers=["unique id", "name", "quantity", "category"], tablefmt="fancy_grid"))
        print('\n')
    elif choice == '3':
        update2()
        print('upadted')
    elif choice=='4':
        x=update()
        print(x)
    else:
        break

conn.close()