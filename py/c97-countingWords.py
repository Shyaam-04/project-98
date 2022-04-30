intro = input("Enter you introduction here: ")
wordCount = 0
charCount = 0

for i in intro:
    charCount = charCount+1
    if(i==" "):
        wordCount=wordCount+1

print("Number of words= ")
print(wordCount)
print("Number of characters= ")
print(charCount)