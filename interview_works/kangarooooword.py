# kangarooo word



source_string = "chicken"
target_string = "henn"

word_count = {}

# Count the occurrences of each character in the source string
for ch in source_string:
    if ch in word_count:
        word_count[ch] += 1
    else:
        word_count[ch] = 1

# Initialize flag for kangaroo word
is_kangaroo_word = True

# Iterate through each character in the target string
for ch in target_string:
    # If the character is present in the word count and has more than 1 occurrence
    if ch in word_count and word_count[ch] > 1:
        # Decrement the count of the character in the word count
        word_count[ch] -= 1
    else:
        # If the character is not present or doesn't have enough occurrences, set flag to False and break the loop
        is_kangaroo_word = False
        break

# Print the result
print("kangaroo word" if is_kangaroo_word else "not kangaroo word")
