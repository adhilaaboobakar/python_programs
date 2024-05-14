source_word="myself"
target_word="self"

source_word_lst=[ ch for ch in source_word]
target_word_lst=[ ch for ch in target_word]


for ch in target_word_lst:
    if ch in source_word_lst:
        source_word_lst.remove(ch)
    else:
        print("not a kangaroo word")
        break
else:
    print("kangaroo word")

# for else block
# in this block ,if break works,then else not works. if break not works,then else in for works