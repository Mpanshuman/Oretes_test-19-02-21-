import sys

''' Taking inputs'''
number_of_chocolate = int(input('Enter Number of chocolate:'))
amount = int(input('Enter amount:'))
price_of_choco_price = list(map(int,input('price of chocolate with spaces:').split()))

john = 0
sean = 0

if number_of_chocolate < 2:
    print('Number of chocolate needs to be min 2')
    sys.exit()

elif number_of_chocolate == 2:
    if price_of_choco_price[0] + price_of_choco_price[1] == amount:
        john = 0
        sean = 1
        print(john,sean)
        sys.exit()
    print('They will not buy any chocolate')
    sys.exit()
    
else:
    ''' sorting the input prices for chocolate'''
    price_of_choco = sorted(price_of_choco_price)
    i = 0
    
    '''finding the chocolate price that is greater than or equal to the amount jhon and sean have '''

    for cprice in price_of_choco:
        if cprice >= amount:
            break
        i+=1
    
    '''checking whether there are any two chocolate price which sum is equal to the amount that jhon and sean have '''
    for price in range(i):
        
        for price_j in range(i):

            if price_of_choco[price]+price_of_choco[price_j] == amount:
                
                john = price_of_choco_price.index(price_of_choco[price])
                sean = price_of_choco_price.index(price_of_choco[price_j])
                break
        
    
    if sean==0 and john == 0 :
        print("They won't any chocolate")
    else:
        print(john,sean)