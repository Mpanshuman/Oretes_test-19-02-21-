size = int(input('Enter Number of input:'))
alice = list(map(int,input('Enter marks of alice with spaces:').split()))
bob = list(map(int,input('Enter marks of bob with spaces:').split()))

alice_point = 0
bob_point = 0

# comparing marks of alice and bob and assiging points
for i in range(5):
    if alice[i] < bob[i]:
        bob_point +=1
    elif alice[i] > bob[i]:
        alice_point +=1


if __name__ == "__main__":
    
    if alice_point > bob_point:
        print('alice won')
    elif bob_point > alice_point:
        print('bob won')
    else:
        print('draw') 