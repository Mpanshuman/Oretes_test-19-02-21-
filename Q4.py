size = int(input('Enter Number of input:'))
list_of_word = list(input('Enter the words with spaces:').split())

# getting the unique words from the list
unique_list = list(set(list_of_word))


if __name__ == "__main__":
    for word in unique_list:
        print(word, len(word), list_of_word.count(word))