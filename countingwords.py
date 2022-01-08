intro=input("Who are u? ")
print(intro)
wordcount=1
charactercount=0
for i in intro:
    charactercount+=1
    if(i==" "):
        wordcount+=1
print("number of words in the string")
print(wordcount)
print("number of character in the string")
print(charactercount)