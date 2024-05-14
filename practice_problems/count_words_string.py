# count the number of words in a string
# str=dog and cat are the pets living in a house
def word_count(string):
    words=string.split(" ")
    count=len(words)
    return count
    
print(word_count("haii helo heiy ghu"))