
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

word_index = 0
joey_index = 0

while word_index < len(word1) and joey_index < len(word2):
    if word1[word_index] == word2[joey_index]:
        joey_index += 1
    word_index += 1

if joey_index == len(word2):
    print(f"{word2} is a kangaroo word in {word1}")
else:
    word_index = 0
    joey_index = 0

    while word_index < len(word2) and joey_index < len(word1):
        if word2[word_index] == word1[joey_index]:
            joey_index += 1
        word_index += 1

    if joey_index == len(word1):
        print(f"{word1} is a kangaroo word in {word2}")
    else:
        print("These words are not kangaroo words of each other.")