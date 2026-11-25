import mysql.connector

def get_db_connection():
    try:
        connection=mysql.connector.connect(host="localhost",user="root",password="sandra",database="library__db")
        return connection
    except Exception:
        print("connection failed")
        return None

def create(title,author,pages,price,languages):
    conn=get_db_connection()
    if conn is None:
        return 
    try:
        cursor=conn.cursor()
        query="insert into Book(title,author,pages,price,languages) values(%s,%s,%s,%s,%s)"
        data=(title,author,pages,price,languages)
        cursor.execute(query,data)
        conn.commit()
    except Exception:
        print("Creation of new book failed")
    finally:
        cursor.close()
        conn.close()

def read():
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="select title,author,pages,price,languages from Book"
        cursor.execute(query)
        records=cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records are found")

    except Exception:
        print("failed to read all book names")

    finally:
        cursor.close()
        conn.close()

def retreive(book_id):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query = "select title,author,pages,price,languages from Book where book_id=%s"
        cursor.execute(query,(book_id,))
        record=cursor.fetchone()
        if record:
            print(record)
        else:
            print("no record found")

    except Exception:
        print("No record found with this book_id")

    finally:
        cursor.close()
        conn.close()

def update(book_id,title,author,pages,price,languages):
    conn=get_db_connection()
    if conn is None:
        return 
    try:
        cursor=conn.cursor()
        query="update Book set title=%s,author=%s,pages=%s,price=%s,languages=%s where book_id=%s"
        data=(title,author,pages,price,languages,book_id)
        cursor.execute(query,data)
        conn.commit()
        if cursor.rowcount > 0:
            print("Book_id",book_id,"updated successfully")
        else:
            print("no book found with the book_id",book_id,"given")
    
    except Exception:
        print("Updating the record failed")

    finally:
        cursor.close()
        conn.close()

def delete(book_id):
    conn=get_db_connection()
    if conn is None:
        return
    try:
        cursor=conn.cursor()
        query="delete from Book where book_id=%s"
        cursor.execute(query,(book_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("the book with id",book_id,"is deleted successfully")
        else:
            print("The book with id",book_id,"is not found")

    except Exception:
        print("Deleting the record failed")

    finally:
        cursor.close()
        conn.close()

while True:
    print("LIBRARY MANAGEMENT SYSTEM (MYSQL)")
    print("1. Create Book")
    print("2. Read All Books")
    print("3. Retrieve Book by ID")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")
    ch=int(input("Enter the numbers choice from (1-6):"))

    if ch == 1:
        title=input("Enter the title of the book:")
        author=input("Enter the author of the book:")
        pages=int(input("Enter the no. of pages of the book:"))
        price=float(input("Enter the price of the book:"))
        languages=input("Enter the language of the book published in:")

        create(title,author,pages,price,languages)

    elif ch == 2:
        read()

    elif ch == 3:
        book_id=int(input("Enter the id to retreive the record:"))
        retreive(book_id)

    elif ch == 4:
        book_id=int(input("Enter the id to update the record:"))
        title=input("Enter the title of the book:")
        author=input("Enter the author of the book:")
        pages=int(input("Enter the no. of pages of the book:"))
        price=float(input("Enter the price of the book:"))
        languages=input("Enter the language of the book published in:")
        update(book_id,title,author,pages,price,languages)

    elif ch == 5:
        book_id=int(input("Enter the id to delete the record:"))
        delete(book_id)

    else:
        exit()
