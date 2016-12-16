__author__ = 'jc449799'
#Function to check if the charecter is vowel or not
vowel = ['a', 'e', 'i', 'o', 'u']
def isvowel(charecter):
    if charecter in vowel:
        return True
    else:
        return False
#*************************************************************
#program to count number of vowels in the given string or name
name = input("Enter your name: ")
vowels=0
for i in name.lower():
    if isvowel(i):
        vowels += 1
print("out of {} letters, {} has {} vowels".format(len(name),name, vowels))
