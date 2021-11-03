
file = open("text.txt","r") #creat object | r- read
content = file.read()

word = input(" enter a word to search : ")
if word in content:
    print(f" the word {word} is in Text")
else:
    print("Not Found")
