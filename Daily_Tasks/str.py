def merge_strings(string1, string2):
    merged_string = ''
    len1 = len(string1)
    len2 = len(string2)
    max_len = max(len1, len2)
    

    for i in range(max_len):
        if i < len1:
            merged_string += string1[i]
        if i < len2:
            merged_string += string2[i]

    return merged_string

# Example usage:
string1 = "abcd"
string2 = "efg"
merged = merge_strings(string1, string2)
print(merged)
