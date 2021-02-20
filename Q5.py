number_of_book =int(input('Enter Number of books:'))
book_list = []
lis_book = []

for books in range(number_of_book):
    book_list.append(list(map(int,input('Enter attributes with spaces:').split())))

choice = input('Enter your choice page,price,chapter?:')

# converting the attributes of the book into dictionary

for book_num,book in enumerate(book_list):
    lis_book.append(dict({'page':book[0],'price':book[1],'chapter':book[2]}))
    
# sorting the dict based on the choice given by the user

def sort_books(choice):
    print (sorted(lis_book, key = lambda i: i[choice]))

if __name__ == "__main__":
    sort_books(choice)