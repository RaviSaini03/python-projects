import os
class library:

    def __init__(self, nameOfBook, priceOfBook):
        self.nameOfBook = nameOfBook
        self.priceOfBook = priceOfBook

#function to load the book inventory when buyer want to buy books
def load_books():
    if os.path.exists("book_inventory.txt"):
        with open("book_inventory.txt", 'r') as file:
            bookName = []
            bookPrice = []
            for line in file:
                #check if the file is not empty
                if line.strip():
                    name, price = line.strip().split(',')
                    bookName.append(name)
                    bookPrice.append(int(price))
                 # If the file is empty (no books saved by incharge), return default books
            if not bookName and not bookPrice:
                return ["Ice and Fire", "Physics", "Maths", "Chemistry"], [90, 80, 70, 50]
            return bookName, bookPrice
    else:
        # If file doesn't exist, return default books
        return ["Ice and Fire", "Physics", "Maths", "Chemistry"], [90, 80, 70, 50]
    
bookName, bookPrice = load_books()

# Function to save book inventory to a file
def save_books(bookName, bookPrice):
    with open("book_inventory.txt", 'w') as file:
        for name, price in zip(bookName, bookPrice):
            file.write(f"{name},{price}\n")

userInput = int(input("Are you a buyer or incharge? \nEnter 1 for buyer or 0 for incharge "))

if(userInput == 0):
    user = int(input("If you are Incharge of Library then write the secret code: "))
else:
    user = 3457
    print("Your Welcome Sir, Which book do you want to buy.\n\n")

if(user == 3456):
    repeat = "yes"
    while repeat == "yes":

        listedBook = input("Enter the name of Book: ")
        listedPrice =  int(input("Enter the price of Book: "))


        class Mlibrary(library):

            def bookNamePriceAppend(self):
                bookName.append(self.nameOfBook)
                bookPrice.append(self.priceOfBook)

        library_instance = Mlibrary(listedBook, listedPrice)
        library_instance.bookNamePriceAppend()

        # Save the updated book inventory to the file
        save_books(bookName, bookPrice)

        repeat = input("Do you Want to do more entries of Books (yes/no): ").strip().lower()

else:
    print("List of Books in Library:\n")
    for i, bookname in enumerate(bookName):
        print(f"{i+1}. {bookname} - Price: ${bookPrice[i]}")

    #make a dictionary by bookName and bookPrice lists
    bookInventory = dict(zip(bookName, bookPrice))

    totalCost = 0
    more = 'yes'

    while more == 'yes':
        buyerEntry = input("Enter the name of book You want to purchase: ")

        if buyerEntry in bookInventory:
            totalCost += bookInventory[buyerEntry]
        else:
            print("Sorry! this book is not available.\n")

        more = input("Do you want to buy more Books (yes/no): ")

    print(f"\n\nYour Total is: ${totalCost}")
    print("Thanks For visiting Sir.")