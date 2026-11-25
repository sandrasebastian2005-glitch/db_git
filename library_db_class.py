import mysql.connector

class Library_db:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="sandra",database="library__db")
        except Exception:
            print("connection failed")
            self.conn=None

    def create(self,title,author,pages,price,languages):
        if self.conn is None:
            return
        try:
            cursor=self.conn.cursor()
            query="insert into Book (title,author,pages,price,languages) values(%s,%s,%s,%s,%s)"
            data=(title,author,pages,price,languages)
            cursor.execute(query,data)
            self.conn.commit()
            print("book added successfully")
        
        except Exception:
            print("creation failed")

        finally:
            cursor.close()

    def read(self):
        if self.conn is None:
            return
        try:
            cursor=self.conn.cursor()
            query="select title,author,pages,price,languages from Book"
            cursor.execute(query)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print("no records found")

        except Exception:
            print("reading the records failed")

        finally:
            cursor.close()

    def retrieve(self,book_id):
        if self.conn is None:
            return
        try:
            cursor=self.conn.cursor()
            query="select title,author,pages,price,languages from Book where book_id=%s"
            cursor.execute(query,(book_id,))
            record=cursor.fetchone()
            if record:
                print(record)
            else:
                print("no record with this book_id")

        except Exception:
            print("retreiving the record failed")

        finally:
            cursor.close()

    def update(self,book_id,title,author,pages,price,languages):
        if self.conn is None:
            return
        try:
            cursor=self.conn.cursor()
            query="update Book set title=%s,author=%s,pages=%s,price=%s,languages=%s where book_id=%s"
            data=(title,author,pages,price,languages,book_id)
            cursor.execute(query,data)
            self.conn.commit()
            if cursor.rowcount > 0:
                print("updated successfully")
            else:
                print("such a book_id doesn't exist")

        except Exception:
            print("updation failed")

        finally:
            cursor.close()

    def delete(self,book_id):
        if self.conn is None:
            return
        try:
            cursor=self.conn.cursor()
            query="delete from Book where book_id=%s"
            cursor.execute(query,(book_id,))
            self.conn.commit()
            if cursor.rowcount > 0:
                print("delete successfully")
            else:
                print("such a book_id doesn't exist")

        except Exception:
            print("deletion failed")

        finally:
            cursor.close()        

b=Library_db()
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

        b.create(title,author,pages,price,languages)

    elif ch == 2:
        b.read()

    elif ch == 3:
        book_id=int(input("Enter the id to retreive the record:"))
        b.retrieve(book_id)

    elif ch == 4:
        book_id=int(input("Enter the id to update the record:"))
        title=input("Enter the title of the book:")
        author=input("Enter the author of the book:")
        pages=int(input("Enter the no. of pages of the book:"))
        price=float(input("Enter the price of the book:"))
        languages=input("Enter the language of the book published in:")
        b.update(book_id,title,author,pages,price,languages)

    elif ch == 5:
        book_id=int(input("Enter the id to delete the record:"))
        b.delete(book_id)

    else:
        exit()
