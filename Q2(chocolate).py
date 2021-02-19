''' Taking inputs'''
number_of_chocolate = int(input('Enter Number of chocolate:'))
amount = int(input('Enter amount:'))
price_of_choco_price = list(map(int,input('price of chocolate with spaces:').split()))

john = 0
sean = 0

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
    
    if price_of_choco[price] + price_of_choco[price+1] == amount:
       
        john = price_of_choco_price.index(price_of_choco[price])
        sean = price_of_choco_price.index(price_of_choco[price+1])
        break

if sean==0 and john == 0 :
    print("They won't any chocolate")
else:
    print(john,sean)