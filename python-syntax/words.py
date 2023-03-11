my_words = ["egg", "hello", "hey", "elementary", "goodbye", "yo", "element", "yes"]

def print_upper_words(words, must_start_with = ['e']):
    '''Print out every word in a words list that starts with the specified letter or letters. 
       Default starting letter is "E".
       Printed words will be ALL-CAPS'''
    print("")
    for word in words:
        if (word[0].upper() in must_start_with) or (word[0].lower() in must_start_with):
            print(word.upper())

print_upper_words(my_words)
print_upper_words(my_words, "h")
print_upper_words(my_words, must_start_with={"h", "y"})