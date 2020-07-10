def countSentenseInCount(word, exceptSentense):
    words = sentense.split()
    yield [len(word) for word in words if word != "the"]
sentense = "the quick brown for jumps over the lazy dog"
for i in countSentenseInCount(sentense,"the"):
    print(str(i))