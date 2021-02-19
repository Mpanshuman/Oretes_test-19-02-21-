book1 = [500,250,22]
book2 = [148,55,10]
book3 = [207,199,31]
choise = input('Enter your choise page,price,chapter?:')
book1_dict  = {'page':book1[0],'price':book1[1],'chapter':book1[2]}
book2_dict  = {'page':book2[0],'price':book2[1],'chapter':book2[2]}
book3_dict  = {'page':book3[0],'price':book3[1],'chapter':book3[2]} 
lis_book = [book1_dict,book2_dict,book3_dict]
def sort_books(choise):
    print (sorted(lis_book, key = lambda i: i[choise]))

if __name__ == "__main__":
    sort_books(choise)