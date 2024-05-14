


# text="hellou"


def vowel_swap(text):

    vowels="aeiou"
    result=""
    for ch in text:
        if ch in vowels:
            if ch=="u":
                result+="a"
            else:
                result+=vowels[vowels.index(ch)+1]

        else:
            result+=ch

    return result

print(vowel_swap("hellou"))
