Word1=input("Enter Word1: ")
Word2=input("Enter Word2: ")

if sorted(Word1)==sorted(Word2):
    print("Anagram")
else:
    print("Not Anagram")