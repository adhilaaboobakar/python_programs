

# remove the vowels from the end of the string,if there is no vowel return same string

# input: hello
# output :hell

# input:dAEIOU
# output:d

def remove_vowels_from_end(text):
    vowels = "aeiouAEIOU"
    return text.rstrip(vowels)

# Test cases
print(remove_vowels_from_end("hello"))  # Output: hell
print(remove_vowels_from_end("dAEIOU"))  # Output: d
print(remove_vowels_from_end("abcde"))  # Output: abcd
print(remove_vowels_from_end("abcd"))   # Output: abcd
