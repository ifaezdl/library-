
class library:
   def __init__(self,i=1,books={},reserved=[],rescount=0):
        self.i=i
        self.books=books
        self.reserved=reserved
        self.rescount=rescount


   def regbook(self):
        isbn = int(input("enter isbn :"))
        name = input("enter book name : ")
        author = input("enter author name : ")
        agegroup = int(input("enter agegroup: "))
        status = bool(input("enter status :"))
        book={   "isbn":isbn,
                 "name":name,
                 "author":author,
                 "age group":agegroup,
                 "status":status}
        self.books.update({"book"+str(self.i):book})
        self.i+=1

   def list(self):
        for x,y in self.books.items():
            print(x," : ",y)

   def delbook(self):
       isbndel=int(input("enter isbn for delete the book from library :"))
       for x in dict(self.books):
           if isbndel==self.books[x]["isbn"]:
                self.books.pop(x)



   def reserve(self):
        isbnreserve=int(input("enter isbn for reserving book: "))
        for x in dict(self.books):
            if self.books[x]["isbn"]==isbnreserve and self.books[x]["status"]==1:
                        self.rescount+=1
                        self.reserved.append(isbnreserve)
                        self.books[x]["status"]=0
                        print(self.reserved)
            elif self.books[x]["status"]==0:
                        print("the book doesnt exist")


   def returnbook(self):
        isbnreturn=int(input("enter isbn for returning : "))
        for x in dict(self.books):
            if self.books[x]["isbn"]==isbnreturn and self.books[x]["status"]==0:
                self.rescount-=1
                self.reserved.remove(isbnreturn)
                self.books[x]["status"]=1
                print(self.reserved)
            elif self.books[x]["status"]==1:
                print("the book doesnt reserved ")


   def delbook(self):
        isbndel=int(input(""
                          "enter isbn for deleting: "))
        for x in dict(self.books):
            if isbndel==self.books[x]["isbn"]:
             self.books.pop(x)

   def search(self):
        type=input("enter book name :")
        keyword=input("enter author name: ")
        for x in dict(self.books):
            if self.books[x]["name"]==type or self.books[x]["author"]==keyword:
                print(self.books[x]["isbn"])

   def report(self,a=0,b=0,c=0):
       for x in dict(self.books):
           if self.books[x]["age group"]<=17:
               a+=1
           elif self.books[x]["age group"]>=18 and self.books[x]["age group"]<=20:
               b+=1
           elif self.books[x]["age group"]>=21:
               c+=1
       import matplotlib.pyplot as plt
       import numpy as np
       x=np.array(["1 to 17","18 to 20","21 to ..."])
       y= np.array([a,b,c])
       plt.bar(x,y)
       plt.show()




class mylib(library):
   def __init__(self,userage=0):
            super().__init__(books={},reserved=[],rescount=0)
            self.userage=userage

   def ageok(self):
       isbnageok=int(input("enter book isbn :"))
       self.userage=int(input("enter your age for analising:"))
       for x in dict(self.books):
           if self.books[x]["isbn"]==isbnageok and self.books[x]["age group"]==self.userage:
             return True

   def reservee(self):
       x=self.ageok()
       if x==True:
           self.reserve()
           print("you reserved book")
       else:
           print("yoy cant reserve this book")

   def menu(self):
       number=int(input("key 1 :register \n"
                        "key 2 : delete book\n"
                        "key 3 : show books \n"
                        "key 4 : search \n"
                        "key 5 : reserve \n"
                        "key 6: return book  \n"
                        "key 7 : report\n"
                        "key 8 : exit \n"
                        "enter your number:"))
       if number==1:
           self.regbook()
           self.menu()
       elif number==2:
           self.delbook()
           self.menu()
       elif number==3:
           self.list()
           self.menu()
       elif number==4:
           self.search()
           self.menu()
       elif number==5:
           self.reservee()
           self.menu()
       elif number==6:
           self.returnbook()
           self.menu()
       elif number==7:
           self.report()
           self.menu()
       elif number==8:
           quit()
       else:
           self.menu()




obj=mylib()
obj.menu()


