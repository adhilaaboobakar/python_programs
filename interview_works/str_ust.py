
# 1. A program to convert the first character uppercase in a sentence and 
# if apart from the first character if any other character is in Uppercase then convert it into Lowercase.



# text="heLLoKKk"
# res=text.capitalize()
# print(res)



def convert_text(text):

    result=text.capitalize()
    result=result[0]+result[1:].lower()
    return result

print(convert_text("heLLojppoPK"))



# def convert_text(text):
#     result = text.capitalize()
#     result = result[0] + result[1:].lower()
#     return result

# print(convert_text("heLLojK"))  # Output: "Hellojk"

   