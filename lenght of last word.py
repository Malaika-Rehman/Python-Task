sentence = input("Enter a sentence: ")
words = sentence.strip().split()
if words:
    last_word = words[-1]
    print("Last word is:", last_word)
    print("Length of last word:", len(last_word))
else:
    print("No words found in the input.")