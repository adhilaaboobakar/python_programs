# print the names that starting with @ from the sentence

tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"

words=tweets.split(" ")
print(words)

for w in words:
    if w.startswith("@"):
        print(w)