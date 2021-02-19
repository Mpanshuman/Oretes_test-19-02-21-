sentence = input('Enter The Sentence:')
count = 0
# list of words without space
words = [word for word in sentence if word!=' ']
# list of space
count_space = [word for word in sentence if word==' ']

special_character = []
lowercase_word = []
uppercase_word = []
odd_digits = []
even_digits = []
output = ''

for word in words:
    if(word >= 'a' and word <= 'z'):
        lowercase_word.append(word)
    elif(word >= 'A' and word <= 'Z'):
        uppercase_word.append(word)
    elif(word >= '0' and word <= '9'):
        
        if int(word)%2 == 0:
            even_digits.append(word)
        else:
            odd_digits.append(word)
    
    else:
        special_character.append(word)
output_list = (special_character+lowercase_word+uppercase_word+odd_digits+even_digits+[len(count_space),])

for word in output_list:
    output = output+str(word)

if __name__ == "__main__":
    print(output)