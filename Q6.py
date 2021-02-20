import re

sentence = input('Enter The Sentence:')

output = ''
# condition to check any special character
special_character_check = re.compile('[@_!#$%^&*()<>?/\|}{~:.]')
# condition to check any small character 
small_character_check = re.compile('[a-z]')
# condition to check any capital character
capital_character_check = re.compile('[A-Z]')
# condition to check any digits
digit_check = re.compile('[0-9]')

list_compile = [special_character_check,small_character_check,capital_character_check,digit_check]


# find all the matching conditions  and appending the results to a list
matches = []
for r in list_compile:
   matches += re.findall( r, sentence)

if __name__ == "__main__":
    for characters in matches:
        output+=characters
    
    print(output+str(len(re.findall("[ \s]+", sentence))))