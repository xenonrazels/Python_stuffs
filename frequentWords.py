from collections import Counter
def frequent(name):
    with open(name) as file:
        return Counter(file.read().split()) #here split is used so it can take file and then read by counting word.Space is used as divider

print("The frequent words are")

print("File name")
name=input("Enter the file name :> ")
print(frequent(name))