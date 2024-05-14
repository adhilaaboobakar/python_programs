
# input : tom jerry tom thr tom
# output : 3


def count_words(text):

    words=text.split(" ")
    count=0
    for w in words:
        if words.count(w)>1:
            count+=1
    return count

print(count_words("tom hii tom huu tom hii"))