class Book:

    def __init__(self, bookid, bookname, bookprice):

        self.__bookid = bookid
        self.__bookname = bookname 
        self.__bookprice = bookprice

    def set_bookid(self, bookid):
        self.__bookid = bookid

    def set_bookname(self, bookname): 
        self.__bookname = bookname

    def set_bookprice(self, bookprice): 
        self.__bookprice = bookprice

    def get_bookid(self): 
        return self.__bookid

    def get_bookname(self): 
        return self.__bookname

    def get_bookprice(self): 
        return self.__bookprice
    def __str__(self):
        return "Book_ID:"+str(self.__bookid)+" "+"BOOK_Name:"+self.__bookname+" "+"BOOK_Price:"+str(self.__bookprice)
     
# Creating and storing objects in list books = []
books=[]
n = int(input('How many records you want to enter?'))

for i in range(n):
    bookid= int(input('Enter BOOKID number:')) 
    bookname = input('Enter book name: ')
    bookprice = int(input('Enter book price:'))
    print() # print blank line
    book = Book(bookid,bookname,bookprice)
    books.append(book)

# Display books details

print('Books detail:\n')

for book in books:
    print('BOOK_ID: ', book.get_bookid())
    print('BOOK_Name:' , book.get_bookname())
    print('BOOK_Price: ', book.get_bookprice())
    print()

# Search the book

bookid= int(input('Enter Bookid   to search: '))

for book in books:


    if book.get_bookid() ==bookid:

        print(book)

        break

else: print('Record not found')



# Delete the book

bookid= int(input('\nEnter BookId to deletebook: '))

for book in books:


    if book.get_bookid() == bookid:

        books.remove(book)
        print('Record deleted')
        break
#update the price
bookid=int(input("Enter book id update price"))
for book in books:
    if book.get_bookid()==bookid:
        new_price=int(input("Enter the new price"))
        #book.set_price(new_price)
        book.set_bookprice(new_price)
        print("updated successfully")
        print(new_price)
        break
else:
    print("book not found")


