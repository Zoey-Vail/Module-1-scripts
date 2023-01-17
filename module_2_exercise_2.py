word = input("Enter a word: ")
r = len(word)
newWord = ""
for l in range(r):
    if word[l].islower():
        newWord += word[l]
for a in range(r):
    if word[a].isupper():
        newWord += word[a]
print(newWord)