def countWord():
    fileName = input("Enter the file name")
    f = open(fileName,"r")
    noOfWords = 0
    for line in f:

        print(line)
        words = line.split()
        noOfWords = noOfWords+len(words)
    
    print(noOfWords)
    

countWord()
